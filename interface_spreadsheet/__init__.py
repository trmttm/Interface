from abc import ABC
from abc import abstractmethod


class SpreadsheetABC(ABC):
    @abstractmethod
    def export(self, **kwargs) -> tuple:
        pass

    @staticmethod
    @abstractmethod
    def save_dictionary_as_spreadsheet(file_name, dictionary: dict):
        pass
