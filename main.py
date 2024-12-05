from manufacturer import Manufacturer
from order import Chassis, Engine, Order, get_completed, get_rejected


if __name__ == "__main__":
    manufacturer = Manufacturer()

    manufacturer.manufacture(Order(Chassis.SPORT, Engine.V8))
    manufacturer.manufacture(Order(Chassis.SEDAN, Engine.V6))
    manufacturer.manufacture(Order(Chassis.SEDAN, Engine.ELECTRIC))
    manufacturer.manufacture(Order(Chassis.UTE, Engine.V8))

    manufacturer2 = Manufacturer()
    manufacturer2.manufacture(Order(Chassis.SPORT, Engine.V6))
    manufacturer2.manufacture(Order(Chassis.UTE, Engine.ELECTRIC))

    assert get_completed() == 4
    assert get_rejected() == 2

    print("All cars manufactured successfully")
