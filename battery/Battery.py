from abc import ABC, abstractmethod
class Battery(ABC):
    @abstractmethod
    def need_service()->bool:
        pass