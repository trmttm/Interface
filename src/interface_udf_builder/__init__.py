from abc import ABC
from abc import abstractmethod


class UDFBuilderABC(ABC):
    @abstractmethod
    def export(self, **kwargs):
        pass
