from engines.electric import Electric


class ElectricTestService:
    engine: Electric

    def __init__(self, engine: Electric):
        self.engine = engine

    def prepare_and_test_engine(self):
        self.engine.charge(100)
        self.engine.turn_on()
