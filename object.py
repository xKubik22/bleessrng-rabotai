from price_calculation import calculate_price
from typing import List


class Object:
    def __init__(self, name: str, works: List):
        self.name = name
        self.works = works
        self.price = self.calculate_price()

    def calculate_price(self) -> int:
        return calculate_price(self.works)

    def get_object_info(self) -> List:
        info = [self.name]
        info.extend(self.works)
        info.append(self.price)
        return info


if __name__ == "__main__":
    pass