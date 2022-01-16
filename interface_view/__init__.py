from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import Tuple
from typing import Union


class ViewABC(ABC):

    @abstractmethod
    def attach_to_event_upon_closing(self, observer):
        pass

    @abstractmethod
    def add_text_box(self, view_model: list):
        pass

    @abstractmethod
    def add_rectangle(self, view_model: dict):
        pass

    @abstractmethod
    def add_text(self, view_model: dict):
        pass

    @abstractmethod
    def remove_shape(self, view_model: list):
        pass

    @abstractmethod
    def connect_shapes(self, view_model: dict):
        pass

    @abstractmethod
    def move_shapes(self, view_model: dict):
        pass

    @abstractmethod
    def move_lines(self, view_model: dict):
        pass

    @abstractmethod
    def add_widgets(self, view_model: Union[list, tuple]):
        pass

    @abstractmethod
    def highlight_shapes(self, view_model: dict):
        pass

    @abstractmethod
    def draw_rectangle(self, view_model: dict):
        pass

    @abstractmethod
    def set_border_color(self, view_model: dict):
        pass

    @abstractmethod
    def set_text_color(self, view_model: dict):
        pass

    @abstractmethod
    def set_font_size(self, view_model: dict):
        pass

    @abstractmethod
    def set_border_width(self, view_model: dict):
        pass

    @abstractmethod
    def set_fill_color(self, view_model: dict):
        pass

    @abstractmethod
    def add_line(self, view_model: dict):
        pass

    @abstractmethod
    def draw_line(self, view_model: dict):
        pass

    @abstractmethod
    def get_value(self, widget_id):
        pass

    @abstractmethod
    def set_values(self, widget_ids: tuple, values: tuple):
        pass

    @abstractmethod
    def set_value(self, widget_id, value):
        pass

    @abstractmethod
    def get_mouse_coordinates_captured(self, event) -> Tuple[int, int]:
        pass

    @abstractmethod
    def get_mouse_canvas_coordinate(self) -> tuple:
        pass

    @property
    @abstractmethod
    def focused_widget(self) -> str:
        pass

    @abstractmethod
    def focus(self, widget_id, **kwargs):
        pass

    @abstractmethod
    def launch_app(self):
        pass

    @abstractmethod
    def bind_command_to_widget(self, widget_id, command):
        pass

    @abstractmethod
    def bind_entry_update(self, entry_id, command):
        pass

    @abstractmethod
    def switch_status_bar(self, status_bar_id):
        pass

    @abstractmethod
    def update_status_bar(self, view_model: dict):
        pass

    @abstractmethod
    def clear_canvas(self, view_model: dict = None):
        pass

    @abstractmethod
    def switch_frame(self, widget_id):
        pass

    @abstractmethod
    def switch_canvas(self, canvas_id):
        pass

    @abstractmethod
    def switch_tree(self, tree_id):
        pass

    @abstractmethod
    def update_tree(self, view_model):
        pass

    @abstractmethod
    def tree_focused_values(self, tree_id) -> tuple:
        pass

    @abstractmethod
    def tree_selected_values(self, tree_id=None) -> tuple:
        pass

    @abstractmethod
    def get_selected_tree_item_indexes(self, tree_id) -> tuple:
        pass

    @abstractmethod
    def select_multiple_tree_items(self, tree_id=None, indexes=()):
        pass

    @abstractmethod
    def tree_number_of_items(self, tree_id=None) -> int:
        pass

    @abstractmethod
    def select_tree_top_items_after_deleting_items(self, indexes: tuple, tree_id=None):
        pass

    @abstractmethod
    def set_title(self, title: str):
        pass

    @abstractmethod
    def change_window_size(self, width=600, height=900):
        pass

    @abstractmethod
    def set_exception_catcher(self, callback: Callable):
        pass

    @property
    @abstractmethod
    def current_canvas(self):
        pass

    @abstractmethod
    def scroll_canvas(self, x, y):
        pass

    @abstractmethod
    def save_canvas_as_an_image(self, file_name):
        pass

    @abstractmethod
    def get_canvas_width(self) -> float:
        pass

    @abstractmethod
    def get_canvas_height(self) -> float:
        pass

    @abstractmethod
    def bind_change_canvas_size(self, call_back: Callable, canvas_id=None):
        pass

    @abstractmethod
    def clear_canvas_shapes_by_tag(self, tag):
        pass

    @abstractmethod
    def get_widget(self, widget_id):
        pass

    @staticmethod
    @abstractmethod
    def close(widget_id):
        pass

    @abstractmethod
    def quit(self):
        pass

    @abstractmethod
    def get_mid_y_coordinates_of_all_rectangles_on_canvas(self):
        pass

    @abstractmethod
    def move_item_vertically_within_range(self, item, delta_x, delta_y, y_range: tuple):
        pass

    @abstractmethod
    def get_clicked_rectangle(self):
        pass

    @staticmethod
    @abstractmethod
    def ask_color(title='Choose color') -> str:
        pass

    @abstractmethod
    def select_folder(self, initialdir=None):
        pass

    @abstractmethod
    def ask_yes_no(self, title, message) -> bool:
        pass

    @abstractmethod
    def select_save_file(self, initialdir=None):
        pass

    @abstractmethod
    def select_open_file(self, initialdir=None):
        pass

    @abstractmethod
    def update_menu_bar(self, menu_bar_model: dict):
        pass

    @abstractmethod
    def set_keyboard_shortcut_handler_to_root(self, keyboard_shortcut_handler: Callable):
        pass

    @abstractmethod
    def set_keyboard_shortcut_handler(self, widget_id, keyboard_shortcut_handler: Callable):
        pass

    @abstractmethod
    def set_paned_window_sash_position(self, paned_window_id, new_position: int):
        pass

    @abstractmethod
    def get_paned_window_sash_position(self, paned_window_id) -> int:
        pass
