class Electric:
    MAX_CHARGE = 100

    def __init__(self):
        self.battery_charge = 0

    def charge(self, charge: int):
        self.battery_charge += charge

    def turn_on(self):
        if self.battery_charge == Electric.MAX_CHARGE:
            print(f"{self} engine is on")
        else:
            raise Exception("Insufficient charge")
