from abc import ABC
from abc import abstractmethod
from typing import Callable


class MouseControllerABC(ABC):
    @abstractmethod
    def set_mode_to_moving_shapes(self):
        pass

    @abstractmethod
    def set_mode_to_adding_shapes(self):
        pass

    @abstractmethod
    def is_moving_shape_mode(self) -> bool:
        pass

    @abstractmethod
    def is_adding_shapes_mode(self) -> bool:
        pass

    @abstractmethod
    def clicked_coordinate(self) -> tuple:
        pass

    @abstractmethod
    def configure(self, key, command, condition: Callable[[dict], bool], command_specific_arguments_dict: dict):
        pass

    @abstractmethod
    def handle(self, x, y, button, modifier, gesture, **kwargs):
        pass

    @abstractmethod
    def _save_mouse_position(self, request: dict):
        pass

    @staticmethod
    @abstractmethod
    def is_left_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_right_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_middle_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_left_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_right_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_middle_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_left_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_right_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_middle_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_left_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_right_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_middle_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_left_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_right_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_middle_click(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_left_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_right_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_middle_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_left_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_right_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_middle_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_left_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_right_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_middle_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_left_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_right_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_middle_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_left_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_right_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_middle_drag(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_left_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_right_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_middle_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_left_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_right_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_middle_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_left_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_right_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_middle_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_left_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_right_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_middle_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_left_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_right_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_middle_release(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_mouse_in(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_mouse_out(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_mouse_wheel(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_shift_mouse_wheel(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_alt_option_mouse_wheel(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_control_mouse_wheel(request: dict) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def is_command_mouse_wheel(request: dict) -> bool:
        pass
