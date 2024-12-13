from engine_services.engine_service import EngineService
from engines.electric import Electric


class ElectricService(EngineService):

    def engine_type(self) -> type:
        return Electric

    def procure_and_test_engine(self) -> Electric:
        engine = Electric()
        engine.charge(Electric.MAX_CHARGE)
        engine.turn_on()
        return engine
