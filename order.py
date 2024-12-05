from enum import Enum

total_complete = 0
total_reject = 0

class Chassis(Enum):
    SPORT = 1
    SEDAN = 2
    UTE = 3

class Engine(Enum):
    V6 = 1
    V8 = 2
    ELECTRIC = 3

class Order:
    def __init__(self, chassis: Chassis, engine: Engine):
        self.chassis = chassis
        self.engine = engine

    def complete(self):
        global total_complete
        total_complete += 1
        print(f"Completed order for {self.chassis.name} chassis with {self.engine.name} engine")

    def reject(self):
        global total_reject
        total_reject += 1
        print(f"Rejected order for {self.chassis.name} chassis with {self.engine.name} engine")

def get_completed() -> int:
    return total_complete

def get_rejected() -> int:
    return total_reject
