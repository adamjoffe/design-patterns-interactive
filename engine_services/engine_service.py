from abc import ABC, abstractmethod


class EngineService(ABC):

    @abstractmethod
    def procure_and_test_engine(self):
        ...
