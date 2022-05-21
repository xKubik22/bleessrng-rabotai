from typing import List


class Object:
    def __init__(self, name: str, works: List):
        self._name = name
        self._works = works

    def get_works(self):
        return self._works

    def get_name(self):
        return self._name


if __name__ == "__main__":
    pass