# System Design Deep Dive Reference

## Core Principles of Large-Scale Systems

### CAP Theorem in Practice

**Consistency (C)**: Every read receives the most recent write or an error
**Availability (A)**: Every request receives a non-error response
**Partition Tolerance (P)**: System operates despite network partitions

**Real-World Trade-offs:**
```
Instagram Feed: AP (eventual consistency OK for feeds)
Bank Transactions: CP (must be consistent, can reject during partitions)
Shopping Cart: AP (availability > temporary inconsistency)
Inventory Count: CP (avoid overselling)
```

### ACID vs BASE

**ACID (Traditional Databases)**
- Atomicity: All or nothing
- Consistency: Valid state transitions
- Isolation: Concurrent transactions don't interfere
- Durability: Committed = persisted

**BASE (Distributed Systems)**
- Basically Available: System always responds
- Soft state: State may change without input
- Eventually consistent: Will converge over time

---

## Rate Limiting Strategies

### Token Bucket Algorithm
```python
class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.last_refill = time.time()
    
    def allow_request(self) -> bool:
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(
            self.capacity,
            self.tokens + elapsed * self.refill_rate
        )
        self.last_refill = now
```

### Sliding Window Log
```python
class SlidingWindowLog:
    def __init__(self, window_size: int, max_requests: int):
        self.window_size = window_size
        self.max_requests = max_requests
        self.requests = []  # [(timestamp, ...)]
    
    def allow_request(self) -> bool:
        now = time.time()
        cutoff = now - self.window_size
        
        # Remove old requests
        self.requests = [r for r in self.requests if r > cutoff]
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
```

### Distributed Rate Limiting with Redis
```lua
-- Redis Lua script for atomic rate limiting
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local now = tonumber(ARGV[3])

-- Remove old entries
redis.call('ZREMRANGEBYSCORE', key, 0, now - window)

-- Count current requests
local count = redis.call('ZCARD', key)

if count < limit then
    redis.call('ZADD', key, now, now .. '-' .. math.random())
    redis.call('EXPIRE', key, window)
    return 1
else
    return 0
end
```

---

## Consistent Hashing

### Implementation
```typescript
class ConsistentHash<T> {
  private ring: Map<number, T> = new Map()
  private sortedKeys: number[] = []
  private virtualNodes: number
  
  constructor(virtualNodes: number = 150) {
    this.virtualNodes = virtualNodes
  }
  
  private hash(key: string): number {
    // Use xxhash or murmur3 in production
    let hash = 0
    for (let i = 0; i < key.length; i++) {
      hash = ((hash << 5) - hash) + key.charCodeAt(i)
      hash |= 0
    }
    return Math.abs(hash)
  }
  
  addNode(node: T, nodeId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${nodeId}:${i}`)
      this.ring.set(hash, node)
    }
    this.sortedKeys = Array.from(this.ring.keys()).sort((a, b) => a - b)
  }
  
  removeNode(nodeId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${nodeId}:${i}`)
      this.ring.delete(hash)
    }
    this.sortedKeys = Array.from(this.ring.keys()).sort((a, b) => a - b)
  }
  
  getNode(key: string): T | undefined {
    if (this.ring.size === 0) return undefined
    
    const hash = this.hash(key)
    
    // Binary search for the first node >= hash
    let left = 0
    let right = this.sortedKeys.length
    
    while (left < right) {
      const mid = Math.floor((left + right) / 2)
      if (this.sortedKeys[mid] < hash) {
        left = mid + 1
      } else {
        right = mid
      }
    }
    
    // Wrap around if necessary
    const index = left === this.sortedKeys.length ? 0 : left
    return this.ring.get(this.sortedKeys[index])
  }
}
```

---

## Database Sharding Strategies

### Sharding Approaches

**1. Range-Based Sharding**
```sql
-- Shard 0: user_id 0 - 999,999
-- Shard 1: user_id 1,000,000 - 1,999,999
-- Shard 2: user_id 2,000,000 - 2,999,999

-- Pros: Simple, range queries within shard
-- Cons: Hotspots if data unevenly distributed
```

**2. Hash-Based Sharding**
```python
def get_shard(user_id: int, num_shards: int) -> int:
    return hash(user_id) % num_shards

# Pros: Even distribution
# Cons: Can't do efficient range queries, resharding is complex
```

**3. Directory-Based Sharding**
```python
# Lookup table maps keys to shards
shard_map = {
    "user:1": "shard-0",
    "user:2": "shard-1",
    # ...
}

def get_shard(key: str) -> str:
    return shard_map.get(key)

# Pros: Flexible, can move individual records
# Cons: Lookup table becomes bottleneck/SPOF
```

### Cross-Shard Queries
```python
async def search_users(query: str, shards: List[ShardConnection]) -> List[User]:
    """Fan-out query across all shards, then aggregate"""
    tasks = [
        shard.execute("SELECT * FROM users WHERE name LIKE %s LIMIT 100", f"%{query}%")
        for shard in shards
    ]
    
    results = await asyncio.gather(*tasks)
    
    # Merge and re-sort
    all_users = []
    for result in results:
        all_users.extend(result)
    
    return sorted(all_users, key=lambda u: u.relevance_score)[:100]
```

---

## Feed Generation Algorithms

### Push Model (Fan-out on Write)
```python
async def create_post(post: Post) -> None:
    # Save post
    await db.posts.insert(post)
    
    # Get all followers
    follower_ids = await db.follows.get_followers(post.user_id)
    
    # Push to each follower's feed (in Redis)
    pipeline = redis.pipeline()
    for follower_id in follower_ids:
        pipeline.zadd(
            f"feed:{follower_id}",
            {str(post.id): post.created_at.timestamp()}
        )
        # Keep feed size bounded
        pipeline.zremrangebyrank(f"feed:{follower_id}", 0, -1001)
    
    await pipeline.execute()

# Good for: Users with < 1000 followers
# Bad for: Celebrities (millions of writes per post)
```

### Pull Model (Fan-out on Read)
```python
async def get_feed(user_id: str, page: int = 0) -> List[Post]:
    # Get following list
    following_ids = await db.follows.get_following(user_id)
    
    # Query posts from all followed users
    posts = await db.posts.find({
        "user_id": {"$in": following_ids},
        "created_at": {"$gt": datetime.now() - timedelta(days=7)}
    }).sort("created_at", -1).skip(page * 20).limit(20)
    
    return posts

# Good for: Celebrity followers (read once per user)
# Bad for: Users following many accounts (slow reads)
```

### Hybrid Model (Instagram's Approach)
```python
async def create_post(post: Post) -> None:
    await db.posts.insert(post)
    
    follower_count = await db.users.get_follower_count(post.user_id)
    
    if follower_count < 1000:
        # Small account: push to all followers
        await fan_out_to_feeds(post)
    else:
        # Large account: let followers pull
        await mark_for_pull(post)

async def get_feed(user_id: str) -> List[Post]:
    # Get cached feed (from push)
    cached_posts = await redis.zrevrange(f"feed:{user_id}", 0, 200)
    
    # Get posts from celebrities (pull)
    celebrity_following = await get_celebrity_following(user_id)
    celebrity_posts = await fetch_celebrity_posts(celebrity_following)
    
    # Merge and rank
    all_posts = merge_and_rank(cached_posts, celebrity_posts)
    
    return all_posts[:50]
```

---

## Message Queue Patterns

### At-Least-Once Delivery
```python
# Producer
async def send_with_retry(message: dict, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            await kafka_producer.send(
                "events",
                value=json.dumps(message).encode(),
                key=message["id"].encode()
            )
            return
        except KafkaError as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)

# Consumer with idempotency
async def process_message(message: dict):
    message_id = message["id"]
    
    # Check if already processed
    if await redis.sismember("processed_messages", message_id):
        return  # Skip duplicate
    
    try:
        # Process the message
        await handle_event(message)
        
        # Mark as processed
        await redis.sadd("processed_messages", message_id)
        await redis.expire("processed_messages", 86400 * 7)
    except Exception as e:
        # Don't mark as processed - will be retried
        raise
```

### Exactly-Once Semantics (Kafka)
```python
# Transactional producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    transactional_id='my-transactional-id',
    enable_idempotence=True
)

producer.init_transactions()

try:
    producer.begin_transaction()
    
    for record in records:
        producer.send('topic', value=record)
    
    # Commit offset and messages atomically
    producer.send_offsets_to_transaction(
        {TopicPartition('input-topic', 0): OffsetAndMetadata(100)},
        consumer_group_id
    )
    
    producer.commit_transaction()
except Exception as e:
    producer.abort_transaction()
    raise
```

### Dead Letter Queue
```python
async def process_with_dlq(message: dict, max_retries: int = 3):
    retry_count = message.get("retry_count", 0)
    
    try:
        await process_message(message)
    except RetryableError as e:
        if retry_count < max_retries:
            # Exponential backoff retry
            message["retry_count"] = retry_count + 1
            delay = 2 ** retry_count
            await schedule_retry(message, delay)
        else:
            # Send to DLQ
            await send_to_dlq(message, str(e))
    except NonRetryableError as e:
        # Send directly to DLQ
        await send_to_dlq(message, str(e))

async def send_to_dlq(message: dict, error: str):
    dlq_message = {
        **message,
        "error": error,
        "failed_at": datetime.utcnow().isoformat(),
        "original_topic": message.get("topic")
    }
    await kafka_producer.send("dead-letter-queue", dlq_message)
```

---

## Load Balancing Algorithms

### Round Robin
```python
class RoundRobinBalancer:
    def __init__(self, servers: List[str]):
        self.servers = servers
        self.current = 0
    
    def get_server(self) -> str:
        server = self.servers[self.current]
        self.current = (self.current + 1) % len(self.servers)
        return server
```

### Weighted Round Robin
```python
class WeightedRoundRobinBalancer:
    def __init__(self, servers: Dict[str, int]):  # server: weight
        self.servers = servers
        self.weights = list(servers.values())
        self.current_weight = 0
        self.max_weight = max(self.weights)
        self.gcd_weight = self._gcd_of_list(self.weights)
        self.current_index = -1
    
    def get_server(self) -> str:
        server_list = list(self.servers.keys())
        
        while True:
            self.current_index = (self.current_index + 1) % len(server_list)
            
            if self.current_index == 0:
                self.current_weight -= self.gcd_weight
                if self.current_weight <= 0:
                    self.current_weight = self.max_weight
            
            if self.weights[self.current_index] >= self.current_weight:
                return server_list[self.current_index]
```

### Least Connections
```python
class LeastConnectionsBalancer:
    def __init__(self, servers: List[str]):
        self.servers = servers
        self.connections = {s: 0 for s in servers}
        self.lock = asyncio.Lock()
    
    async def get_server(self) -> str:
        async with self.lock:
            server = min(self.connections, key=self.connections.get)
            self.connections[server] += 1
            return server
    
    async def release_server(self, server: str):
        async with self.lock:
            self.connections[server] = max(0, self.connections[server] - 1)
```

---

## Circuit Breaker Pattern

```python
from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: int = 30,
        expected_exception: type = Exception
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None
        self.success_count = 0
    
    async def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpenError()
        
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise
    
    def _on_success(self):
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= 3:  # Require 3 successes to close
                self.state = CircuitState.CLOSED
                self.failure_count = 0
                self.success_count = 0
        else:
            self.failure_count = 0
    
    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
    
    def _should_attempt_reset(self) -> bool:
        return (
            self.last_failure_time is not None and
            time.time() - self.last_failure_time >= self.recovery_timeout
        )

# Usage
breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=30)

async def call_external_service():
    return await breaker.call(http_client.get, "https://api.example.com/data")
```

---

## Distributed Locking

### Redis-Based Lock (Redlock)
```python
import redis
import uuid
import time

class DistributedLock:
    def __init__(self, redis_client: redis.Redis, key: str, ttl: int = 30):
        self.redis = redis_client
        self.key = f"lock:{key}"
        self.ttl = ttl
        self.token = str(uuid.uuid4())
    
    def acquire(self, timeout: int = 10) -> bool:
        end_time = time.time() + timeout
        
        while time.time() < end_time:
            if self.redis.set(self.key, self.token, nx=True, ex=self.ttl):
                return True
            time.sleep(0.1)
        
        return False
    
    def release(self) -> bool:
        # Lua script for atomic check-and-delete
        script = """
        if redis.call("get", KEYS[1]) == ARGV[1] then
            return redis.call("del", KEYS[1])
        else
            return 0
        end
        """
        return self.redis.eval(script, 1, self.key, self.token) == 1
    
    def extend(self, additional_time: int) -> bool:
        script = """
        if redis.call("get", KEYS[1]) == ARGV[1] then
            return redis.call("expire", KEYS[1], ARGV[2])
        else
            return 0
        end
        """
        return self.redis.eval(script, 1, self.key, self.token, additional_time) == 1
    
    def __enter__(self):
        if not self.acquire():
            raise LockAcquisitionError(f"Could not acquire lock: {self.key}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

# Usage
with DistributedLock(redis_client, "order:12345") as lock:
    # Critical section
    process_order("12345")
```

---

## Event Sourcing & CQRS

### Event Store Implementation
```python
from dataclasses import dataclass
from typing import List
import json

@dataclass
class Event:
    aggregate_id: str
    event_type: str
    data: dict
    version: int
    timestamp: datetime
    
class EventStore:
    def __init__(self, db_connection):
        self.db = db_connection
    
    async def append(self, aggregate_id: str, events: List[Event], expected_version: int):
        async with self.db.transaction():
            # Optimistic concurrency check
            current_version = await self.db.fetchval(
                "SELECT MAX(version) FROM events WHERE aggregate_id = $1",
                aggregate_id
            ) or 0
            
            if current_version != expected_version:
                raise ConcurrencyError(
                    f"Expected version {expected_version}, got {current_version}"
                )
            
            # Append events
            for i, event in enumerate(events):
                await self.db.execute(
                    """
                    INSERT INTO events (aggregate_id, event_type, data, version, timestamp)
                    VALUES ($1, $2, $3, $4, $5)
                    """,
                    event.aggregate_id,
                    event.event_type,
                    json.dumps(event.data),
                    expected_version + i + 1,
                    event.timestamp
                )
    
    async def get_events(
        self,
        aggregate_id: str,
        from_version: int = 0
    ) -> List[Event]:
        rows = await self.db.fetch(
            """
            SELECT * FROM events
            WHERE aggregate_id = $1 AND version > $2
            ORDER BY version
            """,
            aggregate_id,
            from_version
        )
        return [self._row_to_event(row) for row in rows]

# Aggregate example
class Order:
    def __init__(self, order_id: str):
        self.id = order_id
        self.status = "pending"
        self.items = []
        self.version = 0
        self._pending_events = []
    
    def apply(self, event: Event):
        handler = getattr(self, f"_apply_{event.event_type}", None)
        if handler:
            handler(event.data)
        self.version = event.version
    
    def place_order(self, items: List[dict]):
        if self.status != "pending":
            raise InvalidOperationError("Order already placed")
        
        self._emit("OrderPlaced", {"items": items})
    
    def _apply_OrderPlaced(self, data: dict):
        self.items = data["items"]
        self.status = "placed"
    
    def _emit(self, event_type: str, data: dict):
        event = Event(
            aggregate_id=self.id,
            event_type=event_type,
            data=data,
            version=self.version + len(self._pending_events) + 1,
            timestamp=datetime.utcnow()
        )
        self._pending_events.append(event)
        self.apply(event)
```

### CQRS Read Model Projection
```python
class OrderReadModel:
    def __init__(self, db_connection):
        self.db = db_connection
    
    async def handle(self, event: Event):
        handler = getattr(self, f"_handle_{event.event_type}", None)
        if handler:
            await handler(event)
    
    async def _handle_OrderPlaced(self, event: Event):
        await self.db.execute(
            """
            INSERT INTO orders_view (id, status, items, total, created_at)
            VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT (id) DO UPDATE SET
                status = EXCLUDED.status,
                items = EXCLUDED.items,
                total = EXCLUDED.total
            """,
            event.aggregate_id,
            "placed",
            json.dumps(event.data["items"]),
            sum(item["price"] * item["quantity"] for item in event.data["items"]),
            event.timestamp
        )
    
    async def _handle_OrderShipped(self, event: Event):
        await self.db.execute(
            "UPDATE orders_view SET status = 'shipped', shipped_at = $1 WHERE id = $2",
            event.timestamp,
            event.aggregate_id
        )

# Event processor
class EventProcessor:
    def __init__(self, event_store: EventStore, projections: List):
        self.event_store = event_store
        self.projections = projections
        self.last_processed_id = 0
    
    async def process(self):
        while True:
            events = await self.event_store.get_all_events(after_id=self.last_processed_id)
            
            for event in events:
                for projection in self.projections:
                    await projection.handle(event)
                self.last_processed_id = event.id
            
            await asyncio.sleep(0.1)
```

This reference document provides deep implementation details for building planet-scale systems. Use these patterns as the foundation for any distributed application architecture.
