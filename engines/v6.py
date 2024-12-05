class V6:
    def __init__(self):
        self.fuel = 0

    def add_fuel(self, fuel: int):
        self.fuel += fuel

    def turn_on(self):
        if self.fuel > 0:
            print(f"{self} engine is on")
        else:
            raise Exception("No fuel")
