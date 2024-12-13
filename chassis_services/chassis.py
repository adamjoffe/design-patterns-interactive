from abc import ABC, abstractmethod

from engine_services.engine_service import EngineService


class AbstractChassis(ABC):

    @abstractmethod
    def accepts_engine(engine_type: type) -> bool:
        ...

    @abstractmethod
    def install_engine(engine_service: EngineService) -> None:
        ...
