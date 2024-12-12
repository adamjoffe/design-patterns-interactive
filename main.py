from bestql import contract
from engines import electric, v6, v8
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

    # Tests to ensure everything is manufactured as expected
    
    # All orders marked correctly
    assert get_completed() == 4
    assert get_rejected() == 2
    
    # All cars stored with correct VIN
    stored_car = contract.__storage
    assert len(stored_car) == 4
    assert "0000001" in stored_car
    assert "0000002" in stored_car
    assert "0000003" in stored_car
    assert "0000004" in stored_car

    # All engines are created and tested
    assert len(electric.__engines) == 1
    assert electric.__engines[0].is_tested()
    assert len(v6.__engines) == 1
    assert v6.__engines[0].is_tested()
    assert len(v8.__engines) == 2
    assert v8.__engines[0].is_tested()
    assert v8.__engines[1].is_tested()

    print("All cars manufactured successfully")
