from dataclasses import dataclass

import redis

from lib.env import Env


@dataclass
class CacheConnection:
    host: str = Env.get_redis_host()
    port: int = Env.get_redis_port()
    db: int = Env.get_redis_db()


class CacheHandler:
    def __init__(self, connection: CacheConnection = CacheConnection()):
        self.redis_conn = redis.Redis(host=connection.host,
                                      port=connection.port,
                                      db=connection.db)

    def get(self, key: str) -> str:
        return self.redis_conn.get(key)

    def set(self, key: str, value: str):
        self.redis_conn.set(key, value)
