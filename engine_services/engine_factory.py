
from engine_services.electric_service import ElectricService
from engine_services.v6_service import V6Service
from engine_services.v8_service import V8Service
from order import Engine


class EngineFactory:
    # Factory pattern to create respective engine service based on engine type

    def create_engine_service(self, engine: Engine):
        if (engine == Engine.V6):
            return V6Service()
        elif (engine == Engine.V8):
            return V8Service()
        elif (engine == Engine.ELECTRIC):
            return ElectricService()
        else:
            raise NotImplementedError("Engine type not supported")
