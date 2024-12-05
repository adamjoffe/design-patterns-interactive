from engine_services.engine_service import EngineService
from engines.v6 import V6


class V6Service(EngineService):

    def procure_and_test_engine(self) -> V6:
        engine = V6()
        engine.add_fuel(V6.MAX_FUEL)
        engine.turn_on()
        return engine
