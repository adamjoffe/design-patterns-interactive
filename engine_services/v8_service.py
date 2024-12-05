from engine_services.engine_service import EngineService
from engines.v8 import V8


class V8Service(EngineService):

    def procure_and_test_engine(self) -> V8:
        engine = V8()
        engine.add_fuel(V8.MAX_FUEL)
        engine.turn_on()
        return engine
