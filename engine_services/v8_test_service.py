from engines.v8 import V8


class V8TestService:
    engine: V8

    def __init__(self, engine: V8):
        self.engine = engine

    def prepare_and_test_engine(self):
        self.engine.add_fuel(10)
        self.engine.turn_on()
