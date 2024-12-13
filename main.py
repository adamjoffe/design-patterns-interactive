from bestql.contract import Contract
from engines.electric import Electric
from engines.v6 import V6
from engines.v8 import V8
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
    stored_car = Contract.get_storage()
    assert len(stored_car) == 4
    assert "0000001" in stored_car
    assert "0000002" in stored_car
    assert "0000003" in stored_car
    assert "0000004" in stored_car

    # All engines created correctly and tested
    assert len(Electric.get_engines()) == 1
    assert Electric.get_engines()[0].is_tested()
    assert len(V6.get_engines()) == 1
    assert V6.get_engines()[0].is_tested()
    assert len(V8.get_engines()) == 2
    assert V8.get_engines()[0].is_tested()
    assert V8.get_engines()[1].is_tested()

    print("All cars manufactured successfully")
