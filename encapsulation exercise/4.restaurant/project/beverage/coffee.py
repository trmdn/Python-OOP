from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, price: float, caffeine: float):
        super().__init__(Coffee.MILLILITERS, Coffee.PRICE)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine