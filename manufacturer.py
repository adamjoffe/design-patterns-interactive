from chassis_services.chassis_factory import ChassisFactory
from engine_services.engine_factory import EngineFactory
from order import Order
from storage import Storage
from vin_service import get_next_vin


class Manufacturer:
    storage: Storage
    engine_factory: EngineFactory
    chassis_factory: ChassisFactory

    def __init__(self):
        self.storage = Storage()
        self.engine_factory = EngineFactory()
        self.chassis_factory = ChassisFactory()

    def manufacture(self, order: Order) -> None:
        engine_service = self.engine_factory.create_engine_service(order.engine)
        chassis = self.chassis_factory.create_chassis(order.chassis)
        result = chassis.install_engine(engine_service)
        if not result:
            print("Invalid engine type for chassis")
            order.reject()
        else:
            self.storage.get_warehouse().store_car(get_next_vin(), chassis)
            order.complete()
