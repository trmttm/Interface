from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import Tuple
from typing import Union


class ViewABC(ABC):

    @abstractmethod
    def change_style(self):
        pass

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
    def set_text_value(self, view_model: dict):
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
    def set_line_width(self, view_model: dict):
        pass

    @abstractmethod
    def set_line_arrow(self, view_model: dict):
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
    def set_combobox_values(self, widget_id, values: tuple):
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
    def widget_exists(self, widget_id) -> bool:
        pass

    @abstractmethod
    def remove_widget(self, widget_id):
        pass

    @abstractmethod
    def clear_frame(self, frame_id):
        pass

    @abstractmethod
    def get_mouse_canvas_coordinate(self) -> tuple:
        pass

    @abstractmethod
    def set_text(self, widget_id, text: str):
        pass

    @abstractmethod
    def update(self):
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
    def bind_widget_entry(self, widget_id, command):
        pass

    @abstractmethod
    def bind_left_click(self, command: Callable, widget_id):
        pass

    @abstractmethod
    def bind_right_click(self, command: Callable, widget_id):
        pass

    @abstractmethod
    def bind_middle_click(self, command: Callable, widget_id):
        pass

    @abstractmethod
    def bind_left_click_release(self, command: Callable, widget_id):
        pass

    @abstractmethod
    def bind_right_click_release(self, command: Callable, widget_id):
        pass

    @abstractmethod
    def bind_middle_click_release(self, command: Callable, widget_id):
        pass

    @abstractmethod
    def bind_command_to_widget(self, widget_id, command):
        pass

    @abstractmethod
    def unbind_command_from_widget(self, widget_id):
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

    @property
    @abstractmethod
    def current_tree(self):
        pass

    @abstractmethod
    def set_tree_headings(self, tree_id: str, headings: Tuple[str, ...]):
        pass

    @abstractmethod
    def get_all_tree_values(self, tree_id=None):
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
    def bind_tree_left_click(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_tree_right_click(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_tree_middle_click(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_tree_left_click_release(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_tree_right_click_release(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_tree_middle_click_release(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_tree_enter(self, command: Callable, tree_id=None):
        pass

    @abstractmethod
    def bind_mouse_enter(self, command: Callable, widget_id=None):
        pass

    @abstractmethod
    def bind_mouse_leave(self, command: Callable, widget_id=None):
        pass

    @abstractmethod
    def deselect_tree_items(self, tree_id=None):
        pass

    @abstractmethod
    def change_label_text_color(self, label_id, color):
        pass

    @abstractmethod
    def change_label_font_size(self, label_id, size: int, font_name: str = 'Helvetica bold', overstrike=False):
        pass

    @abstractmethod
    def highlight_entry(self, widget_id: str):
        pass

    @abstractmethod
    def remove_highlight_entry(self, widget_id: str):
        pass

    @abstractmethod
    def select_folder(self, initialdir=None):
        pass

    @abstractmethod
    def ask_yes_no(self, title, message) -> bool:
        pass

    @abstractmethod
    def select_note_book_tab(self, widget_id, tab_id):
        pass

    @abstractmethod
    def select_save_file(self, initialdir=None, initialfile=''):
        pass

    @abstractmethod
    def select_open_file(self, initialdir=None):
        pass

    @abstractmethod
    def update_menu_bar(self, menu_bar_model: dict, toplevel_id=None):
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

    @abstractmethod
    def set_foreground_color(self, widget_id, color: str):
        pass

    @abstractmethod
    def bind_upon_drag_and_drop_enter(self, widget_id, callback: Callable):
        pass

    @abstractmethod
    def bind_upon_drag_and_drop_leave(self, widget_id, callback: Callable):
        pass

    @abstractmethod
    def bind_upon_drag_and_drop_drop(self, widget_id, callback: Callable):
        pass
