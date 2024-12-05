class V8:
    MAX_FUEL = 60

    def __init__(self):
        self.fuel = 0

    def add_fuel(self, fuel: int):
        self.fuel += fuel

    def turn_on(self):
        if self.fuel == V8.MAX_FUEL:
            print(f"{self} engine is on")
        else:
            raise Exception("Insufficient fuel")
