import re
from typing import List


class Regexp:
    def __init__(self, regexp):
        self.regexp = regexp

    def search(self, target: str) -> bool:
        return bool(re.search(self.regexp, target))

    def search_any_in(self, *targets: str):
        for target in targets:
            if self.search(target):
                return True

        return False
