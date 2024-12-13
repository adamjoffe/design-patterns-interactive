class V6:
    MAX_FUEL = 40
    __engines: "V6" = []

    def __init__(self):
        self.fuel = 0
        self.tested = False
        self.__engines.append(self)

    def add_fuel(self, fuel: int):
        self.fuel += fuel

    def turn_on(self):
        if self.fuel == V6.MAX_FUEL:
            print(f"{self} engine is on")
            self.tested = True
        else:
            raise Exception("Insufficient fuel")

    def is_tested(self):
        return self.tested

    @classmethod
    def get_engines(cls):
        return cls.__engines
