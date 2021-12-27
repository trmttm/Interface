from abc import ABC
from abc import abstractmethod


class GateWayABC(ABC):
    def __init__(self, entities, main_directory=None):
        pass

    @property
    @abstractmethod
    def negative_list(self) -> tuple:
        pass

    @property
    @abstractmethod
    def path_pickles(self):
        pass

    @abstractmethod
    def embed_resources_to_project_folder(self, directory_to):
        pass

    @abstractmethod
    def get_resource(self, file_name, package):
        pass

    @abstractmethod
    def get_resource_pickle_load_by_package(self, file_name, package):
        pass

    @abstractmethod
    def get_resource_pickle_load_by_abs_path(self, abs_path):
        pass

    @abstractmethod
    def set_project_folder(self, directory):
        pass

    @abstractmethod
    def change_path_pickles(self, directory: str):
        pass

    @abstractmethod
    def change_path_command_pickles(self, directory: str):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass

    @abstractmethod
    def save_state(self, name: str) -> bool:
        pass

    @abstractmethod
    def save_file(self, file_name: str):
        pass

    @abstractmethod
    def save_commands_to_file(self, file_name: str):
        pass

    @property
    @abstractmethod
    def save_result(self) -> str:
        pass

    @property
    @abstractmethod
    def save_file_result(self) -> str:
        pass

    @abstractmethod
    def load_file(self, file_name: str):
        pass

    @abstractmethod
    def load_macro_file(self, file_name: str):
        pass

    @abstractmethod
    def merge_macro_file(self, file_name: str):
        pass

    @abstractmethod
    def merge_file(self, file_name: str):
        pass

    @abstractmethod
    def load_state(self, memento):
        pass

    @property
    @abstractmethod
    def entities(self):
        pass

    @property
    @abstractmethod
    def pickle_file_names(self) -> list:
        pass

    @property
    @abstractmethod
    def pickle_macro_file_names(self) -> list:
        pass

    @abstractmethod
    def restore_state(self, entities, pickle_name):
        pass

    @abstractmethod
    def save_all_sates_to_file(self, file_name):
        pass

    @abstractmethod
    def restore_all_states_from_file(self, file_name):
        pass

    @abstractmethod
    def reset(self, entities):
        pass

    @abstractmethod
    def remove_template(self, file_name):
        pass

    @abstractmethod
    def remove_macro(self, file_name):
        pass

    @abstractmethod
    def state_changed(self) -> bool:
        pass

    @property
    @abstractmethod
    def current_state(self):
        pass

    @abstractmethod
    def states_are_different(self, state_one, state_two) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def open_file(file_path: str):
        pass

    @abstractmethod
    def save_object_as_pickle(self, file_name_abs_path, data):
        pass

    @abstractmethod
    def create_project_folder(self, path):
        pass

    @staticmethod
    @abstractmethod
    def create_load_config_folder(folder_name, folder_key_word):
        pass
