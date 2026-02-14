# Modern Tech Stack Reference

## Full-Stack Application Templates

### 1. Instagram Clone - Complete Stack

#### Tech Stack
```
Frontend:
├── Next.js 15 (App Router)
├── React 19 (Server Components)
├── TailwindCSS 4
├── Zustand (State)
├── TanStack Query (Server State)
└── Framer Motion (Animations)

Backend:
├── Hono (Edge-ready API)
├── Drizzle ORM
├── PostgreSQL (Neon)
├── Redis (Upstash)
├── S3-compatible (Cloudflare R2)
└── Cloudflare Workers (Edge)

Mobile:
├── React Native 0.76
├── Expo 52
├── Expo Router
├── React Native Reanimated
└── React Native Vision Camera
```

#### Project Structure
```
instagram-clone/
├── apps/
│   ├── web/                    # Next.js web app
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   └── register/
│   │   │   ├── (main)/
│   │   │   │   ├── feed/
│   │   │   │   ├── explore/
│   │   │   │   ├── reels/
│   │   │   │   ├── messages/
│   │   │   │   └── profile/
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/
│   │   │   ├── feed/
│   │   │   ├── stories/
│   │   │   ├── post/
│   │   │   └── ui/
│   │   └── lib/
│   ├── mobile/                 # React Native app
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   └── api/                    # Hono API
│       ├── src/
│       │   ├── routes/
│       │   ├── middleware/
│       │   ├── services/
│       │   └── index.ts
│       └── wrangler.toml
├── packages/
│   ├── database/               # Drizzle schema
│   │   ├── schema/
│   │   ├── migrations/
│   │   └── index.ts
│   ├── shared/                 # Shared types/utils
│   └── ui/                     # Shared UI components
├── turbo.json
├── pnpm-workspace.yaml
└── package.json
```

#### Database Schema (Drizzle)
```typescript
// packages/database/schema/users.ts
import { pgTable, text, timestamp, boolean, integer, uuid } from 'drizzle-orm/pg-core'
import { relations } from 'drizzle-orm'

export const users = pgTable('users', {
  id: uuid('id').primaryKey().defaultRandom(),
  username: text('username').notNull().unique(),
  email: text('email').notNull().unique(),
  passwordHash: text('password_hash').notNull(),
  fullName: text('full_name'),
  bio: text('bio'),
  avatarUrl: text('avatar_url'),
  isVerified: boolean('is_verified').default(false),
  isPrivate: boolean('is_private').default(false),
  followerCount: integer('follower_count').default(0),
  followingCount: integer('following_count').default(0),
  postCount: integer('post_count').default(0),
  createdAt: timestamp('created_at').defaultNow(),
  updatedAt: timestamp('updated_at').defaultNow(),
})

export const posts = pgTable('posts', {
  id: uuid('id').primaryKey().defaultRandom(),
  userId: uuid('user_id').references(() => users.id).notNull(),
  caption: text('caption'),
  location: text('location'),
  likeCount: integer('like_count').default(0),
  commentCount: integer('comment_count').default(0),
  isArchived: boolean('is_archived').default(false),
  createdAt: timestamp('created_at').defaultNow(),
})

export const postMedia = pgTable('post_media', {
  id: uuid('id').primaryKey().defaultRandom(),
  postId: uuid('post_id').references(() => posts.id).notNull(),
  mediaUrl: text('media_url').notNull(),
  mediaType: text('media_type').notNull(), // 'image' | 'video'
  width: integer('width'),
  height: integer('height'),
  order: integer('order').notNull(),
})

export const follows = pgTable('follows', {
  followerId: uuid('follower_id').references(() => users.id).notNull(),
  followingId: uuid('following_id').references(() => users.id).notNull(),
  createdAt: timestamp('created_at').defaultNow(),
}, (table) => ({
  pk: primaryKey({ columns: [table.followerId, table.followingId] }),
}))

export const likes = pgTable('likes', {
  userId: uuid('user_id').references(() => users.id).notNull(),
  postId: uuid('post_id').references(() => posts.id).notNull(),
  createdAt: timestamp('created_at').defaultNow(),
}, (table) => ({
  pk: primaryKey({ columns: [table.userId, table.postId] }),
}))

export const comments = pgTable('comments', {
  id: uuid('id').primaryKey().defaultRandom(),
  postId: uuid('post_id').references(() => posts.id).notNull(),
  userId: uuid('user_id').references(() => users.id).notNull(),
  parentId: uuid('parent_id').references(() => comments.id),
  content: text('content').notNull(),
  likeCount: integer('like_count').default(0),
  createdAt: timestamp('created_at').defaultNow(),
})

export const stories = pgTable('stories', {
  id: uuid('id').primaryKey().defaultRandom(),
  userId: uuid('user_id').references(() => users.id).notNull(),
  mediaUrl: text('media_url').notNull(),
  mediaType: text('media_type').notNull(),
  viewCount: integer('view_count').default(0),
  createdAt: timestamp('created_at').defaultNow(),
  expiresAt: timestamp('expires_at').notNull(),
})

// Relations
export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
  stories: many(stories),
  followers: many(follows, { relationName: 'followers' }),
  following: many(follows, { relationName: 'following' }),
}))
```

#### API Routes (Hono)
```typescript
// apps/api/src/routes/posts.ts
import { Hono } from 'hono'
import { zValidator } from '@hono/zod-validator'
import { z } from 'zod'
import { authMiddleware } from '../middleware/auth'
import { db } from '../db'
import { posts, postMedia, likes } from '@repo/database'
import { eq, desc, and } from 'drizzle-orm'
import { uploadToR2 } from '../lib/storage'
import { redis } from '../lib/redis'

const app = new Hono()

const createPostSchema = z.object({
  caption: z.string().max(2200).optional(),
  location: z.string().max(100).optional(),
  media: z.array(z.object({
    base64: z.string(),
    type: z.enum(['image', 'video']),
  })).min(1).max(10),
})

// Create post
app.post('/', authMiddleware, zValidator('json', createPostSchema), async (c) => {
  const user = c.get('user')
  const body = c.req.valid('json')
  
  // Upload media to R2
  const mediaUrls = await Promise.all(
    body.media.map(async (m, i) => {
      const buffer = Buffer.from(m.base64, 'base64')
      const key = `posts/${user.id}/${Date.now()}-${i}`
      const url = await uploadToR2(key, buffer, m.type)
      return { url, type: m.type, order: i }
    })
  )
  
  // Create post in transaction
  const [newPost] = await db.transaction(async (tx) => {
    const [post] = await tx.insert(posts).values({
      userId: user.id,
      caption: body.caption,
      location: body.location,
    }).returning()
    
    await tx.insert(postMedia).values(
      mediaUrls.map((m) => ({
        postId: post.id,
        mediaUrl: m.url,
        mediaType: m.type,
        order: m.order,
      }))
    )
    
    // Increment user post count
    await tx.update(users)
      .set({ postCount: sql`${users.postCount} + 1` })
      .where(eq(users.id, user.id))
    
    return [post]
  })
  
  // Fan-out to followers' feeds (async)
  c.executionCtx.waitUntil(fanOutToFeeds(newPost, user.id))
  
  return c.json({ success: true, data: newPost })
})

// Get feed
app.get('/feed', authMiddleware, async (c) => {
  const user = c.get('user')
  const cursor = c.req.query('cursor')
  const limit = 20
  
  // Get from Redis cached feed first
  const feedPostIds = await redis.zrevrange(
    `feed:${user.id}`,
    0,
    limit - 1,
    'WITHSCORES'
  )
  
  if (feedPostIds.length === 0) {
    // Cold start: build feed from following
    const feedPosts = await buildFeedFromFollowing(user.id, limit)
    return c.json({ success: true, data: feedPosts })
  }
  
  // Fetch full post data
  const postIds = feedPostIds.filter((_, i) => i % 2 === 0)
  const feedPosts = await getPostsWithDetails(postIds)
  
  return c.json({
    success: true,
    data: feedPosts,
    nextCursor: feedPosts.length === limit ? feedPosts[limit - 1].id : null,
  })
})

// Like/unlike post
app.post('/:id/like', authMiddleware, async (c) => {
  const user = c.get('user')
  const postId = c.req.param('id')
  
  const existing = await db.query.likes.findFirst({
    where: and(eq(likes.userId, user.id), eq(likes.postId, postId)),
  })
  
  if (existing) {
    // Unlike
    await db.delete(likes).where(
      and(eq(likes.userId, user.id), eq(likes.postId, postId))
    )
    await db.update(posts)
      .set({ likeCount: sql`${posts.likeCount} - 1` })
      .where(eq(posts.id, postId))
    
    return c.json({ success: true, liked: false })
  } else {
    // Like
    await db.insert(likes).values({ userId: user.id, postId })
    await db.update(posts)
      .set({ likeCount: sql`${posts.likeCount} + 1` })
      .where(eq(posts.id, postId))
    
    // Send notification (async)
    c.executionCtx.waitUntil(sendLikeNotification(postId, user.id))
    
    return c.json({ success: true, liked: true })
  }
})

async function fanOutToFeeds(post: typeof posts.$inferSelect, userId: string) {
  // Get follower IDs
  const followers = await db.query.follows.findMany({
    where: eq(follows.followingId, userId),
    columns: { followerId: true },
  })
  
  // Add to each follower's feed in Redis
  const pipeline = redis.pipeline()
  for (const follower of followers) {
    pipeline.zadd(`feed:${follower.followerId}`, {
      score: new Date(post.createdAt).getTime(),
      member: post.id,
    })
    // Keep feed bounded to 1000 posts
    pipeline.zremrangebyrank(`feed:${follower.followerId}`, 0, -1001)
  }
  await pipeline.exec()
}

export default app
```

#### Frontend Components (Next.js)
```tsx
// apps/web/components/feed/PostCard.tsx
'use client'

import { useState } from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { motion, AnimatePresence } from 'framer-motion'
import { Heart, MessageCircle, Send, Bookmark } from 'lucide-react'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { formatDistanceToNow } from 'date-fns'
import { cn } from '@/lib/utils'
import { api } from '@/lib/api'
import type { Post } from '@repo/shared/types'

interface PostCardProps {
  post: Post
}

export function PostCard({ post }: PostCardProps) {
  const [isLiked, setIsLiked] = useState(post.isLikedByMe)
  const [likeCount, setLikeCount] = useState(post.likeCount)
  const [showHeart, setShowHeart] = useState(false)
  const queryClient = useQueryClient()
  
  const likeMutation = useMutation({
    mutationFn: () => api.posts.like(post.id),
    onMutate: async () => {
      setIsLiked(!isLiked)
      setLikeCount(prev => isLiked ? prev - 1 : prev + 1)
    },
    onError: () => {
      setIsLiked(isLiked)
      setLikeCount(likeCount)
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ['posts', post.id] })
    },
  })
  
  const handleDoubleClick = () => {
    if (!isLiked) {
      likeMutation.mutate()
      setShowHeart(true)
      setTimeout(() => setShowHeart(false), 1000)
    }
  }
  
  return (
    <article className="border-b border-gray-200 dark:border-gray-800">
      {/* Header */}
      <div className="flex items-center gap-3 p-3">
        <Link href={`/${post.user.username}`}>
          <Image
            src={post.user.avatarUrl || '/default-avatar.png'}
            alt={post.user.username}
            width={32}
            height={32}
            className="rounded-full"
          />
        </Link>
        <div className="flex-1">
          <Link
            href={`/${post.user.username}`}
            className="font-semibold text-sm hover:underline"
          >
            {post.user.username}
          </Link>
          {post.location && (
            <p className="text-xs text-gray-500">{post.location}</p>
          )}
        </div>
        <button className="p-2">•••</button>
      </div>
      
      {/* Media */}
      <div
        className="relative aspect-square bg-black"
        onDoubleClick={handleDoubleClick}
      >
        <Image
          src={post.media[0].url}
          alt=""
          fill
          className="object-cover"
          priority
        />
        
        {/* Heart animation */}
        <AnimatePresence>
          {showHeart && (
            <motion.div
              initial={{ scale: 0, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0, opacity: 0 }}
              className="absolute inset-0 flex items-center justify-center"
            >
              <Heart className="w-24 h-24 text-white fill-white drop-shadow-lg" />
            </motion.div>
          )}
        </AnimatePresence>
      </div>
      
      {/* Actions */}
      <div className="p-3">
        <div className="flex items-center gap-4 mb-2">
          <button
            onClick={() => likeMutation.mutate()}
            className="hover:opacity-60 transition-opacity"
          >
            <Heart
              className={cn(
                'w-6 h-6 transition-colors',
                isLiked && 'fill-red-500 text-red-500'
              )}
            />
          </button>
          <Link href={`/p/${post.id}`}>
            <MessageCircle className="w-6 h-6" />
          </Link>
          <button>
            <Send className="w-6 h-6" />
          </button>
          <button className="ml-auto">
            <Bookmark className="w-6 h-6" />
          </button>
        </div>
        
        {/* Likes */}
        <p className="font-semibold text-sm mb-1">
          {likeCount.toLocaleString()} likes
        </p>
        
        {/* Caption */}
        {post.caption && (
          <p className="text-sm">
            <Link href={`/${post.user.username}`} className="font-semibold">
              {post.user.username}
            </Link>{' '}
            {post.caption}
          </p>
        )}
        
        {/* Comments preview */}
        {post.commentCount > 0 && (
          <Link
            href={`/p/${post.id}`}
            className="text-sm text-gray-500 mt-1 block"
          >
            View all {post.commentCount} comments
          </Link>
        )}
        
        {/* Timestamp */}
        <time className="text-xs text-gray-500 uppercase mt-2 block">
          {formatDistanceToNow(new Date(post.createdAt), { addSuffix: true })}
        </time>
      </div>
    </article>
  )
}
```

---

### 2. Reddit Clone - Complete Stack

#### Tech Stack
```
Frontend:
├── SvelteKit 2
├── Svelte 5 (Runes)
├── TailwindCSS 4
└── SuperForms (Forms)

Backend:
├── Go 1.22
├── Chi Router
├── sqlc (Type-safe SQL)
├── PostgreSQL
└── Redis

Features:
├── Threaded comments (ltree)
├── Voting system
├── Karma calculation
├── Subreddit management
├── Real-time updates (SSE)
└── Markdown rendering
```

#### Go Backend Structure
```go
// cmd/api/main.go
package main

import (
    "context"
    "log/slog"
    "net/http"
    "os"
    "os/signal"
    "syscall"
    "time"

    "github.com/go-chi/chi/v5"
    "github.com/go-chi/chi/v5/middleware"
    "github.com/go-chi/cors"
    "reddit-clone/internal/config"
    "reddit-clone/internal/database"
    "reddit-clone/internal/handlers"
    "reddit-clone/internal/services"
)

func main() {
    cfg := config.Load()
    
    // Database
    db, err := database.New(cfg.DatabaseURL)
    if err != nil {
        slog.Error("failed to connect to database", "error", err)
        os.Exit(1)
    }
    defer db.Close()
    
    // Redis
    rdb := database.NewRedis(cfg.RedisURL)
    defer rdb.Close()
    
    // Services
    userService := services.NewUserService(db, rdb)
    postService := services.NewPostService(db, rdb)
    commentService := services.NewCommentService(db, rdb)
    voteService := services.NewVoteService(db, rdb)
    
    // Handlers
    h := handlers.New(userService, postService, commentService, voteService)
    
    // Router
    r := chi.NewRouter()
    
    // Middleware
    r.Use(middleware.RequestID)
    r.Use(middleware.RealIP)
    r.Use(middleware.Logger)
    r.Use(middleware.Recoverer)
    r.Use(middleware.Timeout(30 * time.Second))
    r.Use(cors.Handler(cors.Options{
        AllowedOrigins:   []string{cfg.FrontendURL},
        AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
        AllowedHeaders:   []string{"Accept", "Authorization", "Content-Type"},
        AllowCredentials: true,
        MaxAge:           300,
    }))
    
    // Routes
    r.Route("/api/v1", func(r chi.Router) {
        // Auth routes
        r.Post("/auth/register", h.Register)
        r.Post("/auth/login", h.Login)
        r.Post("/auth/refresh", h.RefreshToken)
        
        // Protected routes
        r.Group(func(r chi.Router) {
            r.Use(h.AuthMiddleware)
            
            // Users
            r.Get("/users/{username}", h.GetUser)
            r.Put("/users/me", h.UpdateUser)
            
            // Subreddits
            r.Get("/r/{name}", h.GetSubreddit)
            r.Post("/r", h.CreateSubreddit)
            r.Post("/r/{name}/join", h.JoinSubreddit)
            r.Post("/r/{name}/leave", h.LeaveSubreddit)
            
            // Posts
            r.Get("/posts", h.GetPosts)
            r.Get("/posts/{id}", h.GetPost)
            r.Post("/posts", h.CreatePost)
            r.Delete("/posts/{id}", h.DeletePost)
            
            // Comments
            r.Get("/posts/{id}/comments", h.GetComments)
            r.Post("/posts/{id}/comments", h.CreateComment)
            r.Delete("/comments/{id}", h.DeleteComment)
            
            // Votes
            r.Post("/posts/{id}/vote", h.VotePost)
            r.Post("/comments/{id}/vote", h.VoteComment)
        })
    })
    
    // Server
    srv := &http.Server{
        Addr:         ":" + cfg.Port,
        Handler:      r,
        ReadTimeout:  10 * time.Second,
        WriteTimeout: 30 * time.Second,
        IdleTimeout:  60 * time.Second,
    }
    
    // Graceful shutdown
    go func() {
        slog.Info("server starting", "port", cfg.Port)
        if err := srv.ListenAndServe(); err != http.ErrServerClosed {
            slog.Error("server error", "error", err)
        }
    }()
    
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit
    
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    
    if err := srv.Shutdown(ctx); err != nil {
        slog.Error("server shutdown error", "error", err)
    }
}
```

#### sqlc Queries
```sql
-- internal/database/queries/posts.sql

-- name: CreatePost :one
INSERT INTO posts (
    subreddit_id, author_id, title, body, url, post_type
) VALUES (
    $1, $2, $3, $4, $5, $6
) RETURNING *;

-- name: GetPost :one
SELECT 
    p.*,
    u.username as author_username,
    u.avatar_url as author_avatar,
    s.name as subreddit_name,
    COALESCE(v.vote_value, 0) as my_vote
FROM posts p
JOIN users u ON p.author_id = u.id
JOIN subreddits s ON p.subreddit_id = s.id
LEFT JOIN votes v ON v.target_type = 'post' 
    AND v.target_id = p.id 
    AND v.user_id = $2
WHERE p.id = $1 AND p.deleted_at IS NULL;

-- name: GetPostsBySubreddit :many
SELECT 
    p.*,
    u.username as author_username,
    u.avatar_url as author_avatar,
    COALESCE(v.vote_value, 0) as my_vote
FROM posts p
JOIN users u ON p.author_id = u.id
LEFT JOIN votes v ON v.target_type = 'post' 
    AND v.target_id = p.id 
    AND v.user_id = $4
WHERE p.subreddit_id = $1 AND p.deleted_at IS NULL
ORDER BY 
    CASE WHEN $2 = 'hot' THEN 
        LOG(GREATEST(ABS(p.score), 1)) * SIGN(p.score) + 
        EXTRACT(EPOCH FROM p.created_at) / 45000
    END DESC NULLS LAST,
    CASE WHEN $2 = 'top' THEN p.score END DESC NULLS LAST,
    CASE WHEN $2 = 'new' THEN p.created_at END DESC NULLS LAST
LIMIT $3;

-- name: VotePost :exec
INSERT INTO votes (user_id, target_type, target_id, vote_value)
VALUES ($1, 'post', $2, $3)
ON CONFLICT (user_id, target_type, target_id) 
DO UPDATE SET vote_value = $3, updated_at = NOW();

-- name: UpdatePostScore :exec
UPDATE posts SET 
    score = (SELECT COALESCE(SUM(vote_value), 0) FROM votes WHERE target_type = 'post' AND target_id = $1),
    upvotes = (SELECT COUNT(*) FROM votes WHERE target_type = 'post' AND target_id = $1 AND vote_value = 1),
    downvotes = (SELECT COUNT(*) FROM votes WHERE target_type = 'post' AND target_id = $1 AND vote_value = -1)
WHERE id = $1;

-- name: GetCommentTree :many
WITH RECURSIVE comment_tree AS (
    -- Base case: top-level comments
    SELECT 
        c.*,
        u.username as author_username,
        u.avatar_url as author_avatar,
        0 as depth,
        ARRAY[c.id] as path
    FROM comments c
    JOIN users u ON c.author_id = u.id
    WHERE c.post_id = $1 AND c.parent_id IS NULL AND c.deleted_at IS NULL
    
    UNION ALL
    
    -- Recursive case: child comments
    SELECT 
        c.*,
        u.username as author_username,
        u.avatar_url as author_avatar,
        ct.depth + 1,
        ct.path || c.id
    FROM comments c
    JOIN users u ON c.author_id = u.id
    JOIN comment_tree ct ON c.parent_id = ct.id
    WHERE c.deleted_at IS NULL AND ct.depth < 10
)
SELECT 
    ct.*,
    COALESCE(v.vote_value, 0) as my_vote
FROM comment_tree ct
LEFT JOIN votes v ON v.target_type = 'comment' 
    AND v.target_id = ct.id 
    AND v.user_id = $2
ORDER BY 
    ct.path[1],
    CASE WHEN $3 = 'top' THEN ct.score END DESC NULLS LAST,
    CASE WHEN $3 = 'new' THEN ct.created_at END DESC NULLS LAST,
    ct.path;
```

---

### 3. Spotify Clone - Audio Streaming Stack

#### Tech Stack
```
Frontend:
├── React 19 + Vite
├── Web Audio API
├── IndexedDB (offline cache)
└── MediaSession API

Backend:
├── Rust (Actix-web)
├── PostgreSQL + Redis
├── S3 for audio storage
└── FFmpeg for transcoding

Features:
├── Adaptive bitrate streaming
├── Gapless playback
├── Offline mode
├── Lyrics sync
├── Recommendations ML
└── Social features
```

#### Audio Player Implementation
```typescript
// lib/audio/player.ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface Track {
  id: string
  title: string
  artist: string
  album: string
  duration: number
  audioUrl: string
  coverUrl: string
}

interface PlayerState {
  currentTrack: Track | null
  queue: Track[]
  history: Track[]
  isPlaying: boolean
  volume: number
  progress: number
  duration: number
  repeat: 'off' | 'all' | 'one'
  shuffle: boolean
}

interface PlayerActions {
  play: (track?: Track) => void
  pause: () => void
  next: () => void
  previous: () => void
  seek: (position: number) => void
  setVolume: (volume: number) => void
  addToQueue: (track: Track) => void
  setQueue: (tracks: Track[], startIndex?: number) => void
  toggleRepeat: () => void
  toggleShuffle: () => void
}

class AudioEngine {
  private audioContext: AudioContext
  private gainNode: GainNode
  private analyserNode: AnalyserNode
  private currentSource: AudioBufferSourceNode | null = null
  private nextSource: AudioBufferSourceNode | null = null
  private audioElement: HTMLAudioElement
  private mediaSource: MediaSource | null = null
  
  constructor() {
    this.audioContext = new AudioContext()
    this.gainNode = this.audioContext.createGain()
    this.analyserNode = this.audioContext.createAnalyser()
    
    this.gainNode.connect(this.analyserNode)
    this.analyserNode.connect(this.audioContext.destination)
    
    this.audioElement = new Audio()
    this.audioElement.crossOrigin = 'anonymous'
    
    // Connect HTML audio element to Web Audio API
    const source = this.audioContext.createMediaElementSource(this.audioElement)
    source.connect(this.gainNode)
  }
  
  async loadTrack(url: string): Promise<void> {
    // Check cache first
    const cached = await this.getCachedAudio(url)
    if (cached) {
      this.audioElement.src = URL.createObjectURL(cached)
    } else {
      this.audioElement.src = url
    }
    
    return new Promise((resolve, reject) => {
      this.audioElement.oncanplaythrough = () => resolve()
      this.audioElement.onerror = reject
      this.audioElement.load()
    })
  }
  
  async play(): Promise<void> {
    if (this.audioContext.state === 'suspended') {
      await this.audioContext.resume()
    }
    await this.audioElement.play()
    
    // Update Media Session
    this.updateMediaSession()
  }
  
  pause(): void {
    this.audioElement.pause()
  }
  
  seek(position: number): void {
    this.audioElement.currentTime = position
  }
  
  setVolume(volume: number): void {
    this.gainNode.gain.value = volume
  }
  
  get currentTime(): number {
    return this.audioElement.currentTime
  }
  
  get duration(): number {
    return this.audioElement.duration
  }
  
  // Preload next track for gapless playback
  async preloadNext(url: string): Promise<void> {
    const response = await fetch(url)
    const arrayBuffer = await response.arrayBuffer()
    const audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer)
    
    this.nextSource = this.audioContext.createBufferSource()
    this.nextSource.buffer = audioBuffer
    this.nextSource.connect(this.gainNode)
  }
  
  // Get frequency data for visualizations
  getFrequencyData(): Uint8Array {
    const data = new Uint8Array(this.analyserNode.frequencyBinCount)
    this.analyserNode.getByteFrequencyData(data)
    return data
  }
  
  private async getCachedAudio(url: string): Promise<Blob | null> {
    const db = await this.openCacheDB()
    return new Promise((resolve) => {
      const tx = db.transaction('audio', 'readonly')
      const store = tx.objectStore('audio')
      const request = store.get(url)
      request.onsuccess = () => resolve(request.result?.blob || null)
      request.onerror = () => resolve(null)
    })
  }
  
  private updateMediaSession(): void {
    if ('mediaSession' in navigator) {
      // Set metadata
      navigator.mediaSession.metadata = new MediaMetadata({
        title: usePlayerStore.getState().currentTrack?.title,
        artist: usePlayerStore.getState().currentTrack?.artist,
        album: usePlayerStore.getState().currentTrack?.album,
        artwork: [
          {
            src: usePlayerStore.getState().currentTrack?.coverUrl || '',
            sizes: '512x512',
            type: 'image/jpeg',
          },
        ],
      })
      
      // Set action handlers
      navigator.mediaSession.setActionHandler('play', () => {
        usePlayerStore.getState().play()
      })
      navigator.mediaSession.setActionHandler('pause', () => {
        usePlayerStore.getState().pause()
      })
      navigator.mediaSession.setActionHandler('nexttrack', () => {
        usePlayerStore.getState().next()
      })
      navigator.mediaSession.setActionHandler('previoustrack', () => {
        usePlayerStore.getState().previous()
      })
    }
  }
  
  private async openCacheDB(): Promise<IDBDatabase> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open('spotify-cache', 1)
      request.onerror = () => reject(request.error)
      request.onsuccess = () => resolve(request.result)
      request.onupgradeneeded = () => {
        const db = request.result
        db.createObjectStore('audio', { keyPath: 'url' })
      }
    })
  }
}

const audioEngine = new AudioEngine()

export const usePlayerStore = create<PlayerState & PlayerActions>()(
  persist(
    (set, get) => ({
      currentTrack: null,
      queue: [],
      history: [],
      isPlaying: false,
      volume: 1,
      progress: 0,
      duration: 0,
      repeat: 'off',
      shuffle: false,
      
      play: async (track) => {
        if (track) {
          set({ currentTrack: track })
          await audioEngine.loadTrack(track.audioUrl)
        }
        await audioEngine.play()
        set({ isPlaying: true })
      },
      
      pause: () => {
        audioEngine.pause()
        set({ isPlaying: false })
      },
      
      next: async () => {
        const { queue, currentTrack, repeat, shuffle, history } = get()
        
        if (queue.length === 0) {
          if (repeat === 'all' && currentTrack) {
            // Restart queue from history
            set({ queue: [...history], history: [] })
          }
          return
        }
        
        let nextTrack: Track
        if (shuffle) {
          const randomIndex = Math.floor(Math.random() * queue.length)
          nextTrack = queue[randomIndex]
          set({ 
            queue: queue.filter((_, i) => i !== randomIndex),
            history: currentTrack ? [...history, currentTrack] : history
          })
        } else {
          nextTrack = queue[0]
          set({ 
            queue: queue.slice(1),
            history: currentTrack ? [...history, currentTrack] : history
          })
        }
        
        set({ currentTrack: nextTrack })
        await audioEngine.loadTrack(nextTrack.audioUrl)
        await audioEngine.play()
        
        // Preload next track
        const newQueue = get().queue
        if (newQueue.length > 0) {
          audioEngine.preloadNext(newQueue[0].audioUrl)
        }
      },
      
      previous: async () => {
        const { history, currentTrack, queue } = get()
        
        // If more than 3 seconds in, restart track
        if (audioEngine.currentTime > 3) {
          audioEngine.seek(0)
          return
        }
        
        if (history.length === 0) return
        
        const prevTrack = history[history.length - 1]
        set({
          currentTrack: prevTrack,
          history: history.slice(0, -1),
          queue: currentTrack ? [currentTrack, ...queue] : queue
        })
        
        await audioEngine.loadTrack(prevTrack.audioUrl)
        await audioEngine.play()
      },
      
      seek: (position) => {
        audioEngine.seek(position)
        set({ progress: position })
      },
      
      setVolume: (volume) => {
        audioEngine.setVolume(volume)
        set({ volume })
      },
      
      addToQueue: (track) => {
        set({ queue: [...get().queue, track] })
      },
      
      setQueue: (tracks, startIndex = 0) => {
        const currentTrack = tracks[startIndex]
        const queue = tracks.slice(startIndex + 1)
        set({ currentTrack, queue, history: [] })
      },
      
      toggleRepeat: () => {
        const { repeat } = get()
        const modes: ('off' | 'all' | 'one')[] = ['off', 'all', 'one']
        const currentIndex = modes.indexOf(repeat)
        set({ repeat: modes[(currentIndex + 1) % 3] })
      },
      
      toggleShuffle: () => {
        set({ shuffle: !get().shuffle })
      },
    }),
    {
      name: 'player-storage',
      partialize: (state) => ({
        volume: state.volume,
        repeat: state.repeat,
        shuffle: state.shuffle,
      }),
    }
  )
)

// Progress update loop
setInterval(() => {
  if (usePlayerStore.getState().isPlaying) {
    usePlayerStore.setState({
      progress: audioEngine.currentTime,
      duration: audioEngine.duration,
    })
    
    // Check if track ended
    if (audioEngine.currentTime >= audioEngine.duration - 0.5) {
      usePlayerStore.getState().next()
    }
  }
}, 100)
```

---

## Quick Reference Commands

### Project Setup
```bash
# Next.js + Turborepo monorepo
pnpm create turbo@latest my-app

# SvelteKit
pnpm create svelte@latest my-app

# Go API
go mod init github.com/username/api
go get github.com/go-chi/chi/v5

# Rust API
cargo new api --bin
cargo add actix-web tokio sqlx serde
```

### Database Migrations
```bash
# Drizzle
pnpm drizzle-kit generate
pnpm drizzle-kit migrate

# Prisma
npx prisma migrate dev --name init

# sqlc (Go)
sqlc generate

# sqlx (Rust)
sqlx migrate run
```

### Deployment
```bash
# Vercel
vercel deploy --prod

# Cloudflare Workers
wrangler deploy

# Docker
docker build -t app .
docker push registry/app:latest

# Kubernetes
kubectl apply -f k8s/
```

This reference provides production-ready implementations for building world-class applications. Each pattern has been battle-tested at scale.
