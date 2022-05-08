import price_calculation
from typing import List


class Object:
    def __init__(self, name: str, works: List[str]):
        self.name = name
        self.works = works
        self.price = self.calculate_price()

    def calculate_price(self) -> int:
        self.works = self.works
        return 100

    def get_object_info(self) -> List:
        info = [self.name]
        info.extend(self.works)
        info.append(self.price)
        return info


if __name__ == "__main__":
    a = Object('Упрдор', ['ДИ ПЭМИН', 'ДИ НСД', 'КП'])
    print(a.get_object_info())