from engines.v6 import V6


class V6TestService:
    engine: V6

    def __init__(self, engine: V6):
        self.engine = engine

    def prepare_and_test_engine(self):
        self.engine.add_fuel(10)
        self.engine.turn_on()
