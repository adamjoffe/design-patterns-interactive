from chassis_services.chassis import AbstractChassis
from engine_services.electric_service import ElectricService
from engine_services.v8_service import V8Service
from engines.electric import Electric
from engines.v8 import V8


class SportChassis(AbstractChassis):
    engine: V8 | Electric

    def install_engine(self, engine_service: V8Service | ElectricService) -> bool:
        engine = engine_service.procure_and_test_engine()
        if not isinstance(engine, (V8, Electric)):
            print("Engine must be of type V8 or Electric")
            return False
        self.engine = engine
        return True
