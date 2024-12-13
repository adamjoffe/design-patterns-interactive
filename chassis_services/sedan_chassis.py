from chassis_services.chassis import AbstractChassis
from engine_services.electric_service import ElectricService
from engine_services.v6_service import V6Service
from engines.electric import Electric
from engines.v6 import V6


class SedanChassis(AbstractChassis):
    engine: V6 | Electric

    def accepts_engine(self, engine_type: type) -> bool:
        return engine_type in (V6, Electric)

    def install_engine(self, engine_service: V6Service | ElectricService) -> None:
        engine = engine_service.procure_and_test_engine()
        if not isinstance(engine, (V6, Electric)):
            raise Exception("Engine must be of type V6 or Electric")
        self.engine = engine
