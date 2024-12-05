class Electric:
    def __init__(self):
        self.battery_charge = 0

    def charge(self, charge: int):
        self.battery_charge += charge

    def turn_on(self):
        if self.battery_charge > 0:
            print(f"{self} engine is on")
        else:
            raise Exception("No charge")
