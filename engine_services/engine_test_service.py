from abc import ABC, abstractmethod


class EngineTestService(ABC):

    @abstractmethod
    def prepare_and_test_engine(self):
        ...
