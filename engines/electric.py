class Electric:
    MAX_CHARGE = 100
    __engines: "Electric" = []

    def __init__(self):
        self.battery_charge = 0
        self.tested = False
        self.__engines.append(self)

    def charge(self, charge: int):
        self.battery_charge += charge

    def turn_on(self):
        if self.battery_charge == Electric.MAX_CHARGE:
            print(f"{self} engine is on")
            self.tested = True
        else:
            raise Exception("Insufficient charge")

    def is_tested(self):
        return self.tested

    @classmethod
    def get_engines(cls):
        return cls.__engines
