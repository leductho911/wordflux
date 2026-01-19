import asyncio
import time

class RateLimiter:
    """Class để giới hạn số lượng requests trong một khoảng thời gian"""
    
    def __init__(self, requests_per_minute: int):
        self.rate_limit = requests_per_minute
        self.period = 60.0
        self.tokens = requests_per_minute
        self.updated_at = time.monotonic()
        self.lock = asyncio.Lock()

    async def acquire(self):
        """Acquire a token to proceed with request"""
        async with self.lock:
            now = time.monotonic()
            time_passed = now - self.updated_at
            
            # Refill tokens based on time passed
            self.tokens += time_passed * (self.rate_limit / self.period)
            
            # Cap tokens at rate limit
            if self.tokens > self.rate_limit:
                self.tokens = self.rate_limit
            
            self.updated_at = now

            if self.tokens < 1:
                # Wait needed
                wait_time = (1 - self.tokens) * (self.period / self.rate_limit)
                await asyncio.sleep(wait_time)
                
                # Consume token after waiting
                self.tokens -= 1
                self.updated_at = time.monotonic() 
            else:
                # Consume token immediately
                self.tokens -= 1
