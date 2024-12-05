from abc import ABC, abstractmethod


class EngineService(ABC):
    # Adaptor pattern to abstract underlying differences in engine type process under a unified API

    @abstractmethod
    def procure_and_test_engine(self):
        ...
