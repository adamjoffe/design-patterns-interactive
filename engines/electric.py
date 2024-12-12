__engines: "Electric" = []

class Electric:
    MAX_CHARGE = 100
    __tested = False

    def __init__(self):
        self.battery_charge = 0
        __engines.append(self)

    def charge(self, charge: int):
        self.battery_charge += charge

    def turn_on(self):
        if self.battery_charge == Electric.MAX_CHARGE:
            print(f"{self} engine is on")
            self.__tested = True
        else:
            raise Exception("Insufficient charge")

    def is_tested(self):
        return self.__tested
