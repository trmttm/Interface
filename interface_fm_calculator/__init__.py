from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict


class CalculatorABC(ABC):
    @abstractmethod
    def create_data_table(self, *args, **kwargs) -> Dict[Any, Dict[int, float]]:
        pass
