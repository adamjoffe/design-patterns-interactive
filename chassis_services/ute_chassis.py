from chassis_services.chassis import AbstractChassis
from engine_services.v6_service import V6Service
from engine_services.v8_service import V8Service
from engines.v6 import V6
from engines.v8 import V8


class UteChassis(AbstractChassis):
    engine: V6 | V8

    def install_engine(self, engine_service: V6Service | V8Service) -> bool:
        engine = engine_service.procure_and_test_engine()
        if not isinstance(engine, (V6, V8)):
            print("Engine must be of type V6 or V8")
            return False
        self.engine = engine
        return True
