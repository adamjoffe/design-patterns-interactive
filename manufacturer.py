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
        # Facade pattern to simplify the process of manufacturing a car based on an order input
        engine_service = self.engine_factory.create_engine_service(order.engine)
        chassis = self.chassis_factory.create_chassis(order.chassis)
        if not chassis.accepts_engine(engine_service.engine_type()):
            print("Chassis does not accept engine type")
            order.reject()
            return
        chassis.install_engine(engine_service)
        self.storage.get_warehouse().store_car(get_next_vin(), chassis)
        order.complete()
