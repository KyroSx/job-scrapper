import redis


class CacheHandler:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.redis_conn = redis.Redis(host=host, port=port, db=db)

    def get(self, key: str) -> str:
        return self.redis_conn.get(key)

    def set(self, key: str, value: str):
        self.redis_conn.set(key, value)
