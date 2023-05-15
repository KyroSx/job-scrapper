import os
import dotenv

dotenv.load_dotenv()


class Env:
    @staticmethod
    def _get_key(key):
        return os.environ.get(key)

    @staticmethod
    def get_links_path() -> str:
        return Env._get_key('LINK_PATH')

    @staticmethod
    def get_result_path() -> str:
        return Env._get_key('RESULT_PATH')

    @staticmethod
    def get_redis_host():
        return Env._get_key('REDIS_HOST')

    @staticmethod
    def get_redis_port() -> int:
        return int(Env._get_key('REDIS_PORT'))

    @staticmethod
    def get_redis_db() -> int:
        return int(Env._get_key('REDIS_DB'))
