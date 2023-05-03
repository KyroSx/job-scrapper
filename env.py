import os
import dotenv


class Env:
    @staticmethod
    def init():
        dotenv.load_dotenv()

    @staticmethod
    def get_links_path() -> str:
        return os.environ.get('LINK_PATH')