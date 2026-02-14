# Mobile Development Deep Dive

## React Native (Production-Grade)

### Project Structure (Expo)
```
mobile-app/
├── app/                      # Expo Router (file-based routing)
│   ├── (auth)/
│   │   ├── login.tsx
│   │   ├── register.tsx
│   │   └── _layout.tsx
│   ├── (tabs)/
│   │   ├── index.tsx         # Home
│   │   ├── explore.tsx
│   │   ├── create.tsx
│   │   ├── notifications.tsx
│   │   ├── profile.tsx
│   │   └── _layout.tsx
│   ├── post/[id].tsx
│   ├── user/[username].tsx
│   ├── _layout.tsx           # Root layout
│   └── +not-found.tsx
├── components/
│   ├── ui/                   # Reusable UI components
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Avatar.tsx
│   │   └── index.ts
│   ├── feed/
│   │   ├── PostCard.tsx
│   │   ├── PostList.tsx
│   │   └── Stories.tsx
│   └── profile/
│       ├── ProfileHeader.tsx
│       └── PostGrid.tsx
├── lib/
│   ├── api.ts               # API client
│   ├── auth.ts              # Auth utilities
│   ├── storage.ts           # Secure storage
│   └── utils.ts
├── hooks/
│   ├── useAuth.ts
│   ├── usePosts.ts
│   └── useNotifications.ts
├── stores/
│   ├── auth.ts              # Zustand store
│   └── app.ts
├── constants/
│   └── theme.ts
├── app.json
├── tsconfig.json
└── package.json
```

### Navigation (Expo Router)
```tsx
// app/_layout.tsx
import { Stack } from 'expo-router'
import { ThemeProvider } from '@react-navigation/native'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { StatusBar } from 'expo-status-bar'
import { useColorScheme } from 'react-native'
import { GestureHandlerRootView } from 'react-native-gesture-handler'
import { darkTheme, lightTheme } from '@/constants/theme'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5,
      gcTime: 1000 * 60 * 30,
    },
  },
})

export default function RootLayout() {
  const colorScheme = useColorScheme()
  const theme = colorScheme === 'dark' ? darkTheme : lightTheme
  
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <QueryClientProvider client={queryClient}>
        <ThemeProvider value={theme}>
          <Stack screenOptions={{ headerShown: false }}>
            <Stack.Screen name="(auth)" />
            <Stack.Screen name="(tabs)" />
            <Stack.Screen
              name="post/[id]"
              options={{
                presentation: 'modal',
                animation: 'slide_from_bottom',
              }}
            />
          </Stack>
          <StatusBar style="auto" />
        </ThemeProvider>
      </QueryClientProvider>
    </GestureHandlerRootView>
  )
}

// app/(tabs)/_layout.tsx
import { Tabs } from 'expo-router'
import { Home, Search, PlusSquare, Bell, User } from 'lucide-react-native'
import { useTheme } from '@react-navigation/native'

export default function TabLayout() {
  const { colors } = useTheme()
  
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: colors.primary,
        tabBarInactiveTintColor: colors.text,
        tabBarStyle: {
          backgroundColor: colors.card,
          borderTopColor: colors.border,
        },
        headerShown: false,
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color, size }) => <Home size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="explore"
        options={{
          title: 'Explore',
          tabBarIcon: ({ color, size }) => <Search size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="create"
        options={{
          title: 'Create',
          tabBarIcon: ({ color, size }) => <PlusSquare size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="notifications"
        options={{
          title: 'Activity',
          tabBarIcon: ({ color, size }) => <Bell size={size} color={color} />,
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profile',
          tabBarIcon: ({ color, size }) => <User size={size} color={color} />,
        }}
      />
    </Tabs>
  )
}
```

### High-Performance List
```tsx
// components/feed/PostList.tsx
import { useCallback, useMemo } from 'react'
import { View, RefreshControl } from 'react-native'
import { FlashList } from '@shopify/flash-list'
import { useInfiniteQuery } from '@tanstack/react-query'
import { PostCard } from './PostCard'
import { StoriesRow } from './Stories'
import { api } from '@/lib/api'
import type { Post } from '@/types'

const ITEM_HEIGHT = 500 // Approximate height for optimization

export function PostList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
    isLoading,
    refetch,
    isRefetching,
  } = useInfiniteQuery({
    queryKey: ['feed'],
    queryFn: ({ pageParam }) => api.posts.getFeed({ cursor: pageParam }),
    getNextPageParam: (lastPage) => lastPage.nextCursor,
    initialPageParam: undefined as string | undefined,
  })
  
  const posts = useMemo(
    () => data?.pages.flatMap((page) => page.data) ?? [],
    [data]
  )
  
  const renderItem = useCallback(
    ({ item, index }: { item: Post; index: number }) => (
      <PostCard post={item} index={index} />
    ),
    []
  )
  
  const keyExtractor = useCallback((item: Post) => item.id, [])
  
  const onEndReached = useCallback(() => {
    if (hasNextPage && !isFetchingNextPage) {
      fetchNextPage()
    }
  }, [hasNextPage, isFetchingNextPage, fetchNextPage])
  
  const ListHeaderComponent = useMemo(() => <StoriesRow />, [])
  
  const ListEmptyComponent = useMemo(
    () => (
      <View className="flex-1 items-center justify-center p-8">
        <Text className="text-gray-500">No posts yet</Text>
      </View>
    ),
    []
  )
  
  if (isLoading) {
    return <FeedSkeleton />
  }
  
  return (
    <FlashList
      data={posts}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      estimatedItemSize={ITEM_HEIGHT}
      onEndReached={onEndReached}
      onEndReachedThreshold={0.5}
      ListHeaderComponent={ListHeaderComponent}
      ListEmptyComponent={ListEmptyComponent}
      refreshControl={
        <RefreshControl
          refreshing={isRefetching}
          onRefresh={refetch}
          tintColor="#0095f6"
        />
      }
      showsVerticalScrollIndicator={false}
      // Performance optimizations
      removeClippedSubviews
      drawDistance={ITEM_HEIGHT * 3}
    />
  )
}
```

### Animations with Reanimated
```tsx
// components/feed/PostCard.tsx
import { memo, useCallback } from 'react'
import { View, Text, Image, Pressable, Dimensions } from 'react-native'
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
  withSequence,
  withTiming,
  runOnJS,
} from 'react-native-reanimated'
import { Gesture, GestureDetector } from 'react-native-gesture-handler'
import { Heart } from 'lucide-react-native'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { api } from '@/lib/api'
import type { Post } from '@/types'

const { width: SCREEN_WIDTH } = Dimensions.get('window')
const AnimatedHeart = Animated.createAnimatedComponent(Heart)

interface PostCardProps {
  post: Post
  index: number
}

export const PostCard = memo(function PostCard({ post, index }: PostCardProps) {
  const queryClient = useQueryClient()
  const heartScale = useSharedValue(0)
  const heartOpacity = useSharedValue(0)
  const likeButtonScale = useSharedValue(1)
  
  const [isLiked, setIsLiked] = useState(post.isLikedByMe)
  const [likeCount, setLikeCount] = useState(post.likeCount)
  
  const likeMutation = useMutation({
    mutationFn: () => api.posts.toggleLike(post.id),
    onMutate: () => {
      const newLiked = !isLiked
      setIsLiked(newLiked)
      setLikeCount((prev) => (newLiked ? prev + 1 : prev - 1))
    },
    onError: () => {
      setIsLiked(isLiked)
      setLikeCount(likeCount)
    },
  })
  
  const animateHeart = useCallback(() => {
    'worklet'
    heartScale.value = withSequence(
      withSpring(1.2, { damping: 10 }),
      withSpring(0, { damping: 15 })
    )
    heartOpacity.value = withSequence(
      withTiming(1, { duration: 100 }),
      withTiming(0, { duration: 500 })
    )
  }, [])
  
  const animateLikeButton = useCallback(() => {
    'worklet'
    likeButtonScale.value = withSequence(
      withSpring(1.3, { damping: 10 }),
      withSpring(1, { damping: 15 })
    )
  }, [])
  
  const doubleTap = Gesture.Tap()
    .numberOfTaps(2)
    .onEnd(() => {
      if (!isLiked) {
        animateHeart()
        animateLikeButton()
        runOnJS(likeMutation.mutate)()
      }
    })
  
  const heartAnimatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: heartScale.value }],
    opacity: heartOpacity.value,
  }))
  
  const likeButtonAnimatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: likeButtonScale.value }],
  }))
  
  return (
    <View className="border-b border-gray-200 dark:border-gray-800">
      {/* Header */}
      <View className="flex-row items-center gap-3 px-4 py-3">
        <Image
          source={{ uri: post.user.avatarUrl }}
          className="w-8 h-8 rounded-full"
        />
        <View className="flex-1">
          <Text className="font-semibold text-sm dark:text-white">
            {post.user.username}
          </Text>
          {post.location && (
            <Text className="text-xs text-gray-500">{post.location}</Text>
          )}
        </View>
        <Pressable className="p-2">
          <Text>•••</Text>
        </Pressable>
      </View>
      
      {/* Media with double tap */}
      <GestureDetector gesture={doubleTap}>
        <View className="relative">
          <Image
            source={{ uri: post.media[0].url }}
            style={{ width: SCREEN_WIDTH, aspectRatio: 1 }}
            resizeMode="cover"
          />
          
          {/* Heart overlay animation */}
          <Animated.View
            className="absolute inset-0 items-center justify-center"
            style={heartAnimatedStyle}
          >
            <AnimatedHeart
              size={100}
              color="#fff"
              fill="#fff"
              style={{ shadowColor: '#000', shadowOpacity: 0.3, shadowRadius: 10 }}
            />
          </Animated.View>
        </View>
      </GestureDetector>
      
      {/* Actions */}
      <View className="px-4 py-3">
        <View className="flex-row items-center gap-4 mb-2">
          <Pressable
            onPress={() => {
              animateLikeButton()
              likeMutation.mutate()
            }}
          >
            <Animated.View style={likeButtonAnimatedStyle}>
              <Heart
                size={24}
                color={isLiked ? '#ef4444' : '#000'}
                fill={isLiked ? '#ef4444' : 'transparent'}
              />
            </Animated.View>
          </Pressable>
          {/* Other action buttons... */}
        </View>
        
        <Text className="font-semibold text-sm dark:text-white">
          {likeCount.toLocaleString()} likes
        </Text>
        
        {post.caption && (
          <Text className="text-sm dark:text-white mt-1">
            <Text className="font-semibold">{post.user.username}</Text>{' '}
            {post.caption}
          </Text>
        )}
      </View>
    </View>
  )
})
```

### Push Notifications
```typescript
// lib/notifications.ts
import * as Notifications from 'expo-notifications'
import * as Device from 'expo-device'
import { Platform } from 'react-native'
import { api } from './api'

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
  }),
})

export async function registerForPushNotifications(): Promise<string | null> {
  if (!Device.isDevice) {
    console.log('Push notifications require a physical device')
    return null
  }
  
  // Check existing permissions
  const { status: existingStatus } = await Notifications.getPermissionsAsync()
  let finalStatus = existingStatus
  
  // Request if not granted
  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync()
    finalStatus = status
  }
  
  if (finalStatus !== 'granted') {
    console.log('Push notification permission denied')
    return null
  }
  
  // Get Expo push token
  const token = await Notifications.getExpoPushTokenAsync({
    projectId: process.env.EXPO_PROJECT_ID,
  })
  
  // Platform-specific setup
  if (Platform.OS === 'android') {
    await Notifications.setNotificationChannelAsync('default', {
      name: 'default',
      importance: Notifications.AndroidImportance.MAX,
      vibrationPattern: [0, 250, 250, 250],
      lightColor: '#0095F6',
    })
  }
  
  // Register token with backend
  await api.notifications.registerToken(token.data)
  
  return token.data
}

export function useNotifications() {
  const notificationListener = useRef<Notifications.Subscription>()
  const responseListener = useRef<Notifications.Subscription>()
  
  useEffect(() => {
    registerForPushNotifications()
    
    // Handle notifications received while app is foregrounded
    notificationListener.current = Notifications.addNotificationReceivedListener(
      (notification) => {
        console.log('Notification received:', notification)
      }
    )
    
    // Handle notification interactions
    responseListener.current = Notifications.addNotificationResponseReceivedListener(
      (response) => {
        const data = response.notification.request.content.data
        
        // Navigate based on notification type
        switch (data.type) {
          case 'like':
            router.push(`/post/${data.postId}`)
            break
          case 'comment':
            router.push(`/post/${data.postId}?comment=${data.commentId}`)
            break
          case 'follow':
            router.push(`/user/${data.username}`)
            break
          case 'message':
            router.push(`/messages/${data.conversationId}`)
            break
        }
      }
    )
    
    return () => {
      notificationListener.current?.remove()
      responseListener.current?.remove()
    }
  }, [])
}
```

### Secure Storage & Auth
```typescript
// lib/auth.ts
import * as SecureStore from 'expo-secure-store'
import { create } from 'zustand'
import { api } from './api'

const TOKEN_KEY = 'auth_token'
const REFRESH_TOKEN_KEY = 'refresh_token'

interface AuthState {
  user: User | null
  isLoading: boolean
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => Promise<void>
  refreshToken: () => Promise<void>
  checkAuth: () => Promise<void>
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  isLoading: true,
  isAuthenticated: false,
  
  login: async (email, password) => {
    const response = await api.auth.login({ email, password })
    
    await SecureStore.setItemAsync(TOKEN_KEY, response.accessToken)
    await SecureStore.setItemAsync(REFRESH_TOKEN_KEY, response.refreshToken)
    
    set({
      user: response.user,
      isAuthenticated: true,
    })
  },
  
  logout: async () => {
    await SecureStore.deleteItemAsync(TOKEN_KEY)
    await SecureStore.deleteItemAsync(REFRESH_TOKEN_KEY)
    
    set({
      user: null,
      isAuthenticated: false,
    })
  },
  
  refreshToken: async () => {
    const refreshToken = await SecureStore.getItemAsync(REFRESH_TOKEN_KEY)
    if (!refreshToken) throw new Error('No refresh token')
    
    const response = await api.auth.refresh({ refreshToken })
    
    await SecureStore.setItemAsync(TOKEN_KEY, response.accessToken)
    await SecureStore.setItemAsync(REFRESH_TOKEN_KEY, response.refreshToken)
  },
  
  checkAuth: async () => {
    set({ isLoading: true })
    
    try {
      const token = await SecureStore.getItemAsync(TOKEN_KEY)
      if (!token) {
        set({ isLoading: false, isAuthenticated: false })
        return
      }
      
      const user = await api.auth.me()
      set({ user, isAuthenticated: true, isLoading: false })
    } catch (error) {
      // Try refresh
      try {
        await get().refreshToken()
        const user = await api.auth.me()
        set({ user, isAuthenticated: true, isLoading: false })
      } catch {
        await get().logout()
        set({ isLoading: false })
      }
    }
  },
}))

// API interceptor for auth
api.interceptors.request.use(async (config) => {
  const token = await SecureStore.getItemAsync(TOKEN_KEY)
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      try {
        await useAuthStore.getState().refreshToken()
        return api(error.config)
      } catch {
        await useAuthStore.getState().logout()
      }
    }
    throw error
  }
)
```

---

## Flutter (Production-Grade)

### Project Structure
```
flutter_app/
├── lib/
│   ├── main.dart
│   ├── app/
│   │   ├── app.dart
│   │   └── routes.dart
│   ├── features/
│   │   ├── auth/
│   │   │   ├── data/
│   │   │   │   ├── repositories/
│   │   │   │   └── sources/
│   │   │   ├── domain/
│   │   │   │   ├── entities/
│   │   │   │   └── usecases/
│   │   │   └── presentation/
│   │   │       ├── providers/
│   │   │       ├── screens/
│   │   │       └── widgets/
│   │   ├── feed/
│   │   ├── profile/
│   │   └── messages/
│   ├── core/
│   │   ├── constants/
│   │   ├── errors/
│   │   ├── network/
│   │   ├── storage/
│   │   └── utils/
│   └── shared/
│       ├── widgets/
│       └── providers/
├── test/
├── pubspec.yaml
└── analysis_options.yaml
```

### Riverpod State Management
```dart
// lib/features/feed/presentation/providers/feed_provider.dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:freezed_annotation/freezed_annotation.dart';

part 'feed_provider.freezed.dart';

@freezed
class FeedState with _$FeedState {
  const factory FeedState({
    @Default([]) List<Post> posts,
    @Default(false) bool isLoading,
    @Default(false) bool isLoadingMore,
    String? error,
    String? nextCursor,
  }) = _FeedState;
}

@riverpod
class FeedNotifier extends _$FeedNotifier {
  @override
  FeedState build() {
    _loadInitialPosts();
    return const FeedState(isLoading: true);
  }
  
  Future<void> _loadInitialPosts() async {
    try {
      final result = await ref.read(feedRepositoryProvider).getFeed();
      state = state.copyWith(
        posts: result.data,
        nextCursor: result.nextCursor,
        isLoading: false,
      );
    } catch (e) {
      state = state.copyWith(
        error: e.toString(),
        isLoading: false,
      );
    }
  }
  
  Future<void> loadMore() async {
    if (state.isLoadingMore || state.nextCursor == null) return;
    
    state = state.copyWith(isLoadingMore: true);
    
    try {
      final result = await ref.read(feedRepositoryProvider).getFeed(
        cursor: state.nextCursor,
      );
      state = state.copyWith(
        posts: [...state.posts, ...result.data],
        nextCursor: result.nextCursor,
        isLoadingMore: false,
      );
    } catch (e) {
      state = state.copyWith(isLoadingMore: false);
    }
  }
  
  Future<void> refresh() async {
    state = state.copyWith(isLoading: true);
    await _loadInitialPosts();
  }
  
  void likePost(String postId) {
    state = state.copyWith(
      posts: state.posts.map((post) {
        if (post.id == postId) {
          return post.copyWith(
            isLiked: !post.isLiked,
            likeCount: post.isLiked ? post.likeCount - 1 : post.likeCount + 1,
          );
        }
        return post;
      }).toList(),
    );
    
    // Fire and forget API call
    ref.read(feedRepositoryProvider).toggleLike(postId);
  }
}

// Usage in widget
@riverpod
class FeedScreen extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final feedState = ref.watch(feedNotifierProvider);
    
    if (feedState.isLoading) {
      return const Center(child: CircularProgressIndicator());
    }
    
    return RefreshIndicator(
      onRefresh: () => ref.read(feedNotifierProvider.notifier).refresh(),
      child: ListView.builder(
        itemCount: feedState.posts.length + 1,
        itemBuilder: (context, index) {
          if (index == feedState.posts.length) {
            if (feedState.nextCursor != null) {
              ref.read(feedNotifierProvider.notifier).loadMore();
              return const Padding(
                padding: EdgeInsets.all(16),
                child: Center(child: CircularProgressIndicator()),
              );
            }
            return const SizedBox.shrink();
          }
          
          return PostCard(
            post: feedState.posts[index],
            onLike: () => ref
                .read(feedNotifierProvider.notifier)
                .likePost(feedState.posts[index].id),
          );
        },
      ),
    );
  }
}
```

### Custom Animations
```dart
// lib/shared/widgets/animated_like_button.dart
import 'package:flutter/material.dart';

class AnimatedLikeButton extends StatefulWidget {
  final bool isLiked;
  final VoidCallback onTap;
  final double size;
  
  const AnimatedLikeButton({
    super.key,
    required this.isLiked,
    required this.onTap,
    this.size = 24,
  });
  
  @override
  State<AnimatedLikeButton> createState() => _AnimatedLikeButtonState();
}

class _AnimatedLikeButtonState extends State<AnimatedLikeButton>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 200),
      vsync: this,
    );
    
    _scaleAnimation = TweenSequence<double>([
      TweenSequenceItem(
        tween: Tween(begin: 1.0, end: 1.3)
            .chain(CurveTween(curve: Curves.easeOut)),
        weight: 50,
      ),
      TweenSequenceItem(
        tween: Tween(begin: 1.3, end: 1.0)
            .chain(CurveTween(curve: Curves.easeIn)),
        weight: 50,
      ),
    ]).animate(_controller);
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  void _handleTap() {
    widget.onTap();
    if (!widget.isLiked) {
      _controller.forward(from: 0);
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: _handleTap,
      child: AnimatedBuilder(
        animation: _scaleAnimation,
        builder: (context, child) {
          return Transform.scale(
            scale: _scaleAnimation.value,
            child: Icon(
              widget.isLiked ? Icons.favorite : Icons.favorite_border,
              color: widget.isLiked ? Colors.red : Colors.black,
              size: widget.size,
            ),
          );
        },
      ),
    );
  }
}

// Double tap to like animation overlay
class DoubleTapLikeOverlay extends StatefulWidget {
  final Widget child;
  final VoidCallback onDoubleTap;
  
  const DoubleTapLikeOverlay({
    super.key,
    required this.child,
    required this.onDoubleTap,
  });
  
  @override
  State<DoubleTapLikeOverlay> createState() => _DoubleTapLikeOverlayState();
}

class _DoubleTapLikeOverlayState extends State<DoubleTapLikeOverlay>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;
  late Animation<double> _opacityAnimation;
  bool _showHeart = false;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );
    
    _scaleAnimation = TweenSequence<double>([
      TweenSequenceItem(
        tween: Tween(begin: 0.0, end: 1.2)
            .chain(CurveTween(curve: Curves.elasticOut)),
        weight: 60,
      ),
      TweenSequenceItem(
        tween: Tween(begin: 1.2, end: 0.0)
            .chain(CurveTween(curve: Curves.easeIn)),
        weight: 40,
      ),
    ]).animate(_controller);
    
    _opacityAnimation = Tween<double>(begin: 1.0, end: 0.0).animate(
      CurvedAnimation(
        parent: _controller,
        curve: const Interval(0.6, 1.0),
      ),
    );
    
    _controller.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        setState(() => _showHeart = false);
      }
    });
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  void _handleDoubleTap() {
    widget.onDoubleTap();
    setState(() => _showHeart = true);
    _controller.forward(from: 0);
  }
  
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onDoubleTap: _handleDoubleTap,
      child: Stack(
        alignment: Alignment.center,
        children: [
          widget.child,
          if (_showHeart)
            AnimatedBuilder(
              animation: _controller,
              builder: (context, child) {
                return Opacity(
                  opacity: _opacityAnimation.value,
                  child: Transform.scale(
                    scale: _scaleAnimation.value,
                    child: const Icon(
                      Icons.favorite,
                      color: Colors.white,
                      size: 100,
                      shadows: [
                        Shadow(
                          color: Colors.black26,
                          blurRadius: 20,
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
        ],
      ),
    );
  }
}
```

---

## Native iOS (SwiftUI)

### Modern SwiftUI Architecture
```swift
// ContentView.swift
import SwiftUI

@main
struct InstagramCloneApp: App {
    @StateObject private var authViewModel = AuthViewModel()
    
    var body: some Scene {
        WindowGroup {
            if authViewModel.isAuthenticated {
                MainTabView()
                    .environmentObject(authViewModel)
            } else {
                LoginView()
                    .environmentObject(authViewModel)
            }
        }
    }
}

// MainTabView.swift
struct MainTabView: View {
    @State private var selectedTab = 0
    
    var body: some View {
        TabView(selection: $selectedTab) {
            FeedView()
                .tabItem {
                    Image(systemName: selectedTab == 0 ? "house.fill" : "house")
                }
                .tag(0)
            
            ExploreView()
                .tabItem {
                    Image(systemName: "magnifyingglass")
                }
                .tag(1)
            
            CreatePostView()
                .tabItem {
                    Image(systemName: "plus.square")
                }
                .tag(2)
            
            NotificationsView()
                .tabItem {
                    Image(systemName: selectedTab == 3 ? "heart.fill" : "heart")
                }
                .tag(3)
            
            ProfileView()
                .tabItem {
                    Image(systemName: "person")
                }
                .tag(4)
        }
        .tint(.primary)
    }
}

// FeedView.swift
struct FeedView: View {
    @StateObject private var viewModel = FeedViewModel()
    
    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVStack(spacing: 0) {
                    // Stories
                    StoriesRowView()
                    
                    Divider()
                    
                    // Posts
                    ForEach(viewModel.posts) { post in
                        PostCardView(post: post)
                            .onAppear {
                                if post.id == viewModel.posts.last?.id {
                                    Task { await viewModel.loadMore() }
                                }
                            }
                    }
                    
                    if viewModel.isLoadingMore {
                        ProgressView()
                            .padding()
                    }
                }
            }
            .refreshable {
                await viewModel.refresh()
            }
            .navigationTitle("Instagram")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button(action: {}) {
                        Image(systemName: "camera")
                    }
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button(action: {}) {
                        Image(systemName: "paperplane")
                    }
                }
            }
        }
        .task {
            await viewModel.loadInitialPosts()
        }
    }
}

// PostCardView.swift
struct PostCardView: View {
    let post: Post
    @State private var isLiked: Bool
    @State private var likeCount: Int
    @State private var showHeartAnimation = false
    
    init(post: Post) {
        self.post = post
        _isLiked = State(initialValue: post.isLikedByMe)
        _likeCount = State(initialValue: post.likeCount)
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Header
            HStack {
                AsyncImage(url: URL(string: post.user.avatarUrl)) { image in
                    image
                        .resizable()
                        .scaledToFill()
                } placeholder: {
                    Circle()
                        .fill(Color.gray.opacity(0.3))
                }
                .frame(width: 32, height: 32)
                .clipShape(Circle())
                
                VStack(alignment: .leading, spacing: 2) {
                    Text(post.user.username)
                        .font(.subheadline)
                        .fontWeight(.semibold)
                    
                    if let location = post.location {
                        Text(location)
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                }
                
                Spacer()
                
                Button(action: {}) {
                    Image(systemName: "ellipsis")
                }
            }
            .padding(.horizontal)
            .padding(.vertical, 8)
            
            // Image with double tap
            ZStack {
                AsyncImage(url: URL(string: post.media.first?.url ?? "")) { image in
                    image
                        .resizable()
                        .scaledToFit()
                } placeholder: {
                    Rectangle()
                        .fill(Color.gray.opacity(0.3))
                        .aspectRatio(1, contentMode: .fit)
                }
                .onTapGesture(count: 2) {
                    if !isLiked {
                        withAnimation(.spring(response: 0.3, dampingFraction: 0.6)) {
                            isLiked = true
                            likeCount += 1
                            showHeartAnimation = true
                        }
                        
                        // Hide heart after delay
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                            withAnimation {
                                showHeartAnimation = false
                            }
                        }
                        
                        // API call
                        Task { await PostService.shared.toggleLike(postId: post.id) }
                    }
                }
                
                // Heart animation overlay
                if showHeartAnimation {
                    Image(systemName: "heart.fill")
                        .font(.system(size: 80))
                        .foregroundColor(.white)
                        .shadow(color: .black.opacity(0.3), radius: 10)
                        .transition(.scale.combined(with: .opacity))
                }
            }
            
            // Actions
            HStack(spacing: 16) {
                Button(action: toggleLike) {
                    Image(systemName: isLiked ? "heart.fill" : "heart")
                        .font(.title2)
                        .foregroundColor(isLiked ? .red : .primary)
                        .scaleEffect(isLiked ? 1.1 : 1.0)
                        .animation(.spring(response: 0.3), value: isLiked)
                }
                
                Button(action: {}) {
                    Image(systemName: "bubble.right")
                        .font(.title2)
                }
                
                Button(action: {}) {
                    Image(systemName: "paperplane")
                        .font(.title2)
                }
                
                Spacer()
                
                Button(action: {}) {
                    Image(systemName: "bookmark")
                        .font(.title2)
                }
            }
            .padding(.horizontal)
            .padding(.top, 8)
            
            // Likes
            Text("\(likeCount) likes")
                .font(.subheadline)
                .fontWeight(.semibold)
                .padding(.horizontal)
                .padding(.top, 4)
            
            // Caption
            if let caption = post.caption {
                HStack {
                    Text(post.user.username)
                        .fontWeight(.semibold) +
                    Text(" \(caption)")
                }
                .font(.subheadline)
                .padding(.horizontal)
                .padding(.top, 2)
            }
            
            // Timestamp
            Text(post.createdAt.timeAgo())
                .font(.caption)
                .foregroundColor(.secondary)
                .padding(.horizontal)
                .padding(.top, 4)
                .padding(.bottom, 12)
        }
    }
    
    private func toggleLike() {
        withAnimation(.spring(response: 0.3, dampingFraction: 0.6)) {
            isLiked.toggle()
            likeCount += isLiked ? 1 : -1
        }
        
        Task { await PostService.shared.toggleLike(postId: post.id) }
    }
}

// FeedViewModel.swift
@MainActor
class FeedViewModel: ObservableObject {
    @Published var posts: [Post] = []
    @Published var isLoading = false
    @Published var isLoadingMore = false
    @Published var error: Error?
    
    private var nextCursor: String?
    private let postService = PostService.shared
    
    func loadInitialPosts() async {
        isLoading = true
        defer { isLoading = false }
        
        do {
            let result = try await postService.getFeed()
            posts = result.data
            nextCursor = result.nextCursor
        } catch {
            self.error = error
        }
    }
    
    func loadMore() async {
        guard !isLoadingMore, let cursor = nextCursor else { return }
        
        isLoadingMore = true
        defer { isLoadingMore = false }
        
        do {
            let result = try await postService.getFeed(cursor: cursor)
            posts.append(contentsOf: result.data)
            nextCursor = result.nextCursor
        } catch {
            self.error = error
        }
    }
    
    func refresh() async {
        await loadInitialPosts()
    }
}
```

---

## Performance Optimization Tips

### React Native
```typescript
// 1. Use FlashList over FlatList
// 2. Memoize components with React.memo
// 3. Use useCallback for event handlers
// 4. Use useMemo for expensive computations
// 5. Enable Hermes engine
// 6. Use react-native-fast-image
// 7. Implement skeleton screens
// 8. Use Reanimated for animations (runs on UI thread)
```

### Flutter
```dart
// 1. Use const constructors
// 2. Implement shouldRebuild for CustomPainter
// 3. Use ListView.builder for long lists
// 4. Cache network images (cached_network_image)
// 5. Use compute() for heavy tasks
// 6. Profile with DevTools
// 7. Minimize rebuilds with Selector
// 8. Use RepaintBoundary wisely
```

### iOS
```swift
// 1. Use @MainActor for UI updates
// 2. Implement pagination with LazyVStack
// 3. Use AsyncImage with caching
// 4. Profile with Instruments
// 5. Use Task { } for async work
// 6. Implement pull-to-refresh with .refreshable
// 7. Use @StateObject for view model lifecycle
// 8. Optimize images with thumbnails
```

This reference provides production-ready mobile development patterns used by top apps. Each implementation is optimized for performance and user experience.
