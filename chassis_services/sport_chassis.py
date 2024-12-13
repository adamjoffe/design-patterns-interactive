from chassis_services.chassis import AbstractChassis
from engine_services.electric_service import ElectricService
from engine_services.v8_service import V8Service
from engines.electric import Electric
from engines.v8 import V8


class SportChassis(AbstractChassis):
    engine: V8 | Electric

    def accepts_engine(self, engine_type: type) -> bool:
        return engine_type in (V8, Electric)

    def install_engine(self, engine_service: V8Service | ElectricService) -> None:
        engine = engine_service.procure_and_test_engine()
        if not isinstance(engine, (V8, Electric)):
            raise Exception("Engine must be of type V8 or Electric")
        self.engine = engine_service
