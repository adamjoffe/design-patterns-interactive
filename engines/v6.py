__engines: "V6" = []

class V6:
    MAX_FUEL = 40
    __tested = False

    def __init__(self):
        self.fuel = 0
        __engines.append(self)

    def add_fuel(self, fuel: int):
        self.fuel += fuel

    def turn_on(self):
        if self.fuel == V6.MAX_FUEL:
            print(f"{self} engine is on")
            self.__tested = True
        else:
            raise Exception("Insufficient fuel")

    def is_tested(self):
        return self.__tested
