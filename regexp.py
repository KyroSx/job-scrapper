import re


class Regexp:
    def __init__(self, regexp):
        self.regexp = regexp

    def search(self, target: str) -> bool:
        return bool(re.search(self.regexp, target))
