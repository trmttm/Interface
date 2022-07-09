from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import Iterable
from typing import Union


class BoundaryInABC(ABC):

    @abstractmethod
    def set_project_folder_path(self, path):
        pass

    @abstractmethod
    def create_project_folder(self, path):
        pass

    @property
    @abstractmethod
    def project_folder(self):
        pass

    @property
    @abstractmethod
    def clean_state_prior_to_save(self) -> bool:
        pass

    @abstractmethod
    def clear_project_history(self):
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def tear_down(self):
        pass

    @abstractmethod
    def tear_down_setup(self):
        pass

    @property
    @abstractmethod
    def account_width(self):
        pass

    @property
    @abstractmethod
    def account_height(self):
        pass

    @property
    @abstractmethod
    def account_font_size(self):
        pass

    @property
    @abstractmethod
    def operator_width(self):
        pass

    @property
    @abstractmethod
    def operator_height(self):
        pass

    @property
    @abstractmethod
    def operator_font_size(self):
        pass

    @property
    @abstractmethod
    def constant_width(self):
        pass

    @property
    @abstractmethod
    def constant_font_size(self):
        pass

    @property
    @abstractmethod
    def constant_height(self):
        pass

    @property
    @abstractmethod
    def bb_width(self):
        pass

    @property
    @abstractmethod
    def bb_font_size(self):
        pass

    @property
    @abstractmethod
    def bb_height(self):
        pass

    @abstractmethod
    def set_account_width(self, value: int):
        pass

    @abstractmethod
    def set_account_height(self, value: int):
        pass

    @abstractmethod
    def set_account_font_size(self, value: int):
        pass

    @abstractmethod
    def set_operator_width(self, value: int):
        pass

    @abstractmethod
    def set_operator_height(self, value: int):
        pass

    @abstractmethod
    def set_operator_font_size(self, value: int):
        pass

    @abstractmethod
    def set_constant_width(self, value: int):
        pass

    @abstractmethod
    def set_constant_height(self, value: int):
        pass

    @abstractmethod
    def set_constant_font_size(self, value: int):
        pass

    @abstractmethod
    def set_bb_width(self, value: int):
        pass

    @abstractmethod
    def set_bb_height(self, value: int):
        pass

    @abstractmethod
    def set_bb_font_size(self, value: int):
        pass

    @property
    @abstractmethod
    def recent_project_paths(self) -> tuple:
        pass

    @abstractmethod
    def upon_exception(self, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def entry_by_mouse(self) -> bool:
        pass

    @abstractmethod
    def do_nothing(self, *_, **__):
        pass

    @abstractmethod
    def set_entry_point(self, entry_by: str = None, request: dict = None):
        pass

    @abstractmethod
    def set_previous_command(self, f: Callable, args: tuple, kwargs: dict):
        pass

    @abstractmethod
    def execute_previous_command(self):
        pass

    @abstractmethod
    def exit_point(self, exit_by: str = None, request: dict = None):
        pass

    @property
    @abstractmethod
    def entities(self):
        pass

    @abstractmethod
    def clear_selection(self):
        pass

    @abstractmethod
    def add_shape_at_x_y_to_selection(self, request: dict):
        pass

    @property
    @abstractmethod
    def selection_except_blanks(self) -> tuple:
        pass

    @abstractmethod
    def get_shape_at_coordinate(self, x, y):
        pass

    @abstractmethod
    def select_shape_at_x_y(self, request: dict):
        pass

    @abstractmethod
    def add_shapes_in_range_to_selection(self, request: dict):
        pass

    @abstractmethod
    def select_shapes_in_range(self, request: dict):
        pass

    @abstractmethod
    def unselect_shape_in_range(self, request: dict):
        pass

    @abstractmethod
    def unselect_shape_at_x_y(self, request: dict):
        pass

    @abstractmethod
    def move_selections(self, delta_x=None, delta_y=None, request: dict = None):
        pass

    @abstractmethod
    def move_selections_to(self, x: int, y: int):
        pass

    @abstractmethod
    def erase_selected_shapes(self, **_):
        pass

    @abstractmethod
    def add_new_shape(self, text: str = 'Text', tag: str = None):
        pass

    @abstractmethod
    def copy_shapes(self, shape_ids):
        pass

    @abstractmethod
    def copy_selection(self):
        pass

    @abstractmethod
    def add_live_values_of_selected_accounts(self, period=0):
        pass

    @abstractmethod
    def draw_rectangle(self, coordinate_from=None, coordinate_to=None, line_width=None, line_color=None,
                       request: dict = None):
        pass

    @abstractmethod
    def clear_rectangles(self, **_):
        pass

    @abstractmethod
    def connect_shapes_by_coordinates(self, coordinate_from=None, coordinate_to=None, request: dict = None):
        pass

    @abstractmethod
    def connect_shapes_by_shape_ids(self, shape_id_from, shape_id_to):
        pass

    @abstractmethod
    def disconnect_shapes_by_shape_ids(self, shape_id_from, shape_id_to):
        pass

    @abstractmethod
    def draw_line_shape_connector(self, coordinate_from: tuple = None, coordinate_to: tuple = None, width=None,
                                  color=None, request: dict = None):
        pass

    @abstractmethod
    def erase_all_lines(self, request: dict = None):
        pass

    @abstractmethod
    def save_state_to_memory(self):
        pass

    @property
    @abstractmethod
    def current_state(self):
        pass

    @abstractmethod
    def states_are_different(self, state_one, state_two) -> bool:
        pass

    @abstractmethod
    def save_state_to_file(self, file_name: str):
        pass

    @abstractmethod
    def save_current_sheet_as_module(self, file_name: str):
        pass

    @abstractmethod
    def load_file(self, file_name: str):
        pass

    @abstractmethod
    def merge_file(self, file_name: str):
        pass

    @abstractmethod
    def merge_file_to_selected_sheet(self, file_name: str):
        pass

    @abstractmethod
    def save_all_to_file(self, file_name: str):
        pass

    @abstractmethod
    def load_all_from_file(self, file_name: str):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass

    @abstractmethod
    def show_connectable_shapes(self, id_from=None, request: dict = None):
        pass

    @abstractmethod
    def load_pickle_files_list(self, negative_list: tuple = None):
        pass

    @abstractmethod
    def get_pickle_file_names(self, negative_list):
        pass

    @property
    @abstractmethod
    def pickle_commands_file_names(self) -> list:
        pass

    @abstractmethod
    def feedback_user(self, text: str, feedback_type='normal'):
        pass

    @abstractmethod
    def add_selection_to_vertical_accounts(self):
        pass

    @abstractmethod
    def remove_selection_from_vertical_accounts(self):
        pass

    @abstractmethod
    def add_vertical_reference_to_selection(self, vertical_reference_id):
        pass

    @abstractmethod
    def remove_vertical_reference_to_selection(self, vertical_reference_id):
        pass

    @abstractmethod
    def add_unit_of_measure(self, shape_id, unit_of_measure: str):
        pass

    @abstractmethod
    def add_unit_of_measure_to_selection(self, unit_of_measure: str):
        pass

    @abstractmethod
    def display_pickle(self, pickle_name: str):
        pass

    @abstractmethod
    def activate_state_cleaner(self):
        pass

    @abstractmethod
    def deactivate_state_cleaner(self):
        pass

    @abstractmethod
    def activate_live_calculation(self):
        pass

    @abstractmethod
    def deactivate_live_calculation(self):
        pass

    @property
    @abstractmethod
    def is_live_calculation_mode(self) -> bool:
        pass

    @abstractmethod
    def select_shape_by_account_order(self, account_order):
        pass

    @abstractmethod
    def select_shape_by_account_orders(self, account_orders: tuple):
        pass

    @abstractmethod
    def select_shape_by_shape_id(self, shape_id):
        pass

    @abstractmethod
    def add_shapes_to_selection(self, shape_ids: tuple):
        pass

    @abstractmethod
    def erase_all_shapes(self):
        pass

    @abstractmethod
    def change_account_order(self, index_: int, deistination: int):
        pass

    @abstractmethod
    def move_selection_up(self, by: int = 1):
        pass

    @abstractmethod
    def move_selection_down(self, by: int = 1):
        pass

    @abstractmethod
    def add_blank_row(self, index_: int):
        pass

    @abstractmethod
    def add_blank_above_selection(self):
        pass

    @abstractmethod
    def add_relay(self):
        pass

    @abstractmethod
    def align_left(self):
        pass

    @abstractmethod
    def align_right(self):
        pass

    @abstractmethod
    def align_top(self):
        pass

    @abstractmethod
    def align_bottom(self):
        pass

    @abstractmethod
    def align_middle_horizontal(self):
        pass

    @abstractmethod
    def align_middle_vertical(self):
        pass

    @abstractmethod
    def evenly_distribute_horizontally(self):
        pass

    @abstractmethod
    def evenly_distribute_vertically(self):
        pass

    @abstractmethod
    def connect_relay_of_shape_at_x_y(self, request: dict):
        pass

    @abstractmethod
    def analyze_circular_reference(self):
        pass

    @abstractmethod
    def erase_connections_in_range(self, request: dict):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def remove_templates(self, pickle_name):
        pass

    @abstractmethod
    def remove_template(self, pickle_name):
        pass

    @abstractmethod
    def clean_up_all_templates(self, negative_list: tuple):
        pass

    @abstractmethod
    def fit_selected_shapes_width(self):
        pass

    @abstractmethod
    def fit_all_shapes_width(self):
        pass

    @abstractmethod
    def fit_shapes_width(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def match_selected_shapes_width(self):
        pass

    @abstractmethod
    def match_shapes_width(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def decrease_width_of_selected_shapes(self):
        pass

    @abstractmethod
    def increase_width_of_selected_shapes(self):
        pass

    @abstractmethod
    def _present_shape_properties(self):
        pass

    @abstractmethod
    def set_property_to_selection(self, key: str, value):
        pass

    @abstractmethod
    def move_selections_one_direction(self, request: dict):
        pass

    @abstractmethod
    def move_selections_one_direction_and_evenly_distribute(self, request: dict):
        pass

    @abstractmethod
    def present_state(self):
        pass

    @property
    @abstractmethod
    def selected_sheet(self):
        pass

    @abstractmethod
    def add_new_worksheet(self, sheet_name: str = None):
        pass

    @abstractmethod
    def select_worksheet(self, sheet_name: str, update=False):
        pass

    @abstractmethod
    def delete_selected_worksheet(self):
        pass

    @property
    @abstractmethod
    def selection(self):
        pass

    @property
    @abstractmethod
    def account_order(self):
        pass

    @abstractmethod
    def change_selected_sheet_name(self, sheet_name: str):
        pass

    @abstractmethod
    def is_blank(self, value) -> bool:
        pass

    @property
    @abstractmethod
    def selected_account_names(self) -> tuple:
        pass

    @property
    @abstractmethod
    def first_selected_text(self) -> str:
        pass

    @abstractmethod
    def change_sheet_order(self, indexes: tuple, shift: int) -> tuple:
        pass

    @abstractmethod
    def add_worksheet_parent_child_relationships(self, above_sheet_names: Iterable, child_sheet_names: Iterable):
        pass

    @abstractmethod
    def remove_worksheet_parent_child_relationships(self, child_sheet_names: Iterable):
        pass

    @abstractmethod
    def copy_accounts(self):
        pass

    @abstractmethod
    def paste_accounts(self):
        pass

    @abstractmethod
    def unselect_all(self):
        pass

    @abstractmethod
    def select_all_in_the_sheet(self):
        pass

    @abstractmethod
    def select_account_by_name(self, account_name, sheet_name: str = None, nth: int = 0):
        pass

    @property
    @abstractmethod
    def copied_account_names(self) -> tuple:
        pass

    @property
    @abstractmethod
    def input_accounts(self) -> tuple:
        pass

    @property
    def input_names(self) -> tuple:
        pass

    @property
    @abstractmethod
    def output_worksheet_information(self):
        pass

    @abstractmethod
    def plug_in_gateway_spreadsheet(self, cls_spreadsheet_gateway):
        pass

    @abstractmethod
    def export_excel(self, file_name: str = None, path: str = None):
        pass

    @abstractmethod
    def set_worksheet_to_selected_shapes_properties(self, value):
        pass

    @abstractmethod
    def change_path_pickles(self, directory: str):
        pass

    @abstractmethod
    def change_path_command_pickles(self, directory: str):
        pass

    @abstractmethod
    def set_default_increment(self, x, y):
        pass

    @abstractmethod
    def set_bb_shift(self, shift):
        pass

    @abstractmethod
    def set_number_of_periods(self, number_of_periods: int):
        pass

    @abstractmethod
    def set_save_file_name(self, file_name):
        pass

    @abstractmethod
    def save_file_name(self):
        pass

    @abstractmethod
    def set_save_path(self, folder_path):
        pass

    @abstractmethod
    def set_relay_x_to_right(self):
        pass

    @abstractmethod
    def set_relay_x_to_right_end(self):
        pass

    @property
    @abstractmethod
    def relay_to_be_placed_at_right_end(self) -> bool:
        pass

    @property
    @abstractmethod
    def breakdown_accounts(self) -> tuple:
        pass

    @abstractmethod
    def add_selection_to_breakdown_accounts(self):
        pass

    @abstractmethod
    def remove_selection_from_breakdown_accounts(self):
        pass

    @abstractmethod
    def turn_on_insert_sheet_names_in_input_sheet(self):
        pass

    @abstractmethod
    def turn_off_insert_sheet_names_in_input_sheet(self):
        pass

    @abstractmethod
    def add_sensitivity_target_accounts(self, account_id):
        pass

    @abstractmethod
    def remove_sensitivity_target_accounts(self, account_ids: tuple):
        pass

    @abstractmethod
    def shift_multiple_sensitivity_target_account(self, indexes, shift: int):
        pass

    @abstractmethod
    def add_sensitivity_variable_accounts(self, account_ids: tuple):
        pass

    @abstractmethod
    def remove_sensitivity_variable_accounts(self, account_ids: tuple):
        pass

    @abstractmethod
    def set_sensitivity_deltas(self, account_ids: tuple, delta: float):
        pass

    @property
    @abstractmethod
    def save_path(self):
        pass

    @property
    @abstractmethod
    def pickle_path(self):
        pass

    @abstractmethod
    def worksheet_exists(self, sheet_name: str) -> bool:
        pass

    @abstractmethod
    def refresh_properties(self):
        pass

    @abstractmethod
    def erase_shapes_in_rectangle(self, request: dict):
        pass

    @abstractmethod
    def update_input_entry_upon_launch(self):
        pass

    @abstractmethod
    def set_values_to_input_being_modified(self, values: tuple):
        pass

    @abstractmethod
    def set_decimals_to_input_being_modified(self, decimals: int):
        pass

    @abstractmethod
    def show_next_input(self):
        pass

    @abstractmethod
    def show_previous_input(self):
        pass

    @abstractmethod
    def show_specified_input(self, input_id):
        pass

    @abstractmethod
    def update_input_entry(self):
        pass

    @property
    @abstractmethod
    def input_being_modified(self):
        pass

    @abstractmethod
    def set_input_y_range(self, y_range: tuple):
        pass

    @abstractmethod
    def get_input_y_range(self, input_account) -> tuple:
        pass

    @abstractmethod
    def get_input_decimals(self, input_account) -> int:
        pass

    @property
    @abstractmethod
    def prevent_user_input_by_tree(self) -> bool:
        pass

    @property
    @abstractmethod
    def move_shape_increment(self) -> tuple:
        pass

    @property
    @abstractmethod
    def number_of_periods(self) -> int:
        pass

    @abstractmethod
    def set_default_input_values_if_values_not_set(self):
        pass

    @abstractmethod
    def clear_input_being_modified(self):
        pass

    @abstractmethod
    def change_shape_id(self, old_shape_id, new_shape_id):
        pass

    @abstractmethod
    def scale_canvas(self, x_times, y_times):
        pass

    @abstractmethod
    def present_insert_worksheet_in_input_sheet_mode(self):
        pass

    @abstractmethod
    def present_sensitivity_input_accounts(self):
        pass

    @abstractmethod
    def present_sensitivity_accounts(self):
        pass

    @abstractmethod
    def present_sensitivity_target_accounts(self):
        pass

    @abstractmethod
    def present_sensitivity_variable_accounts(self):
        pass

    @abstractmethod
    def present_refresh_canvas(self):
        pass

    @abstractmethod
    def highlight_automatic(self, **_):
        pass

    @property
    @abstractmethod
    def selection_contains_constant(self) -> bool:
        pass

    @property
    @abstractmethod
    def number_of_selected_shapes(self) -> int:
        pass

    @abstractmethod
    def add_connection_id(self, shape_id, socket_name: str):
        pass

    @abstractmethod
    def add_the_same_connection_ids_to_selection(self, socket_name: str):
        pass

    @abstractmethod
    def remove_connection_id_from_selection(self, connection_id):
        pass

    @abstractmethod
    def remove_connection_id(self, shape_id, connection_id):
        pass

    @abstractmethod
    def remove_plug_id_from_selection(self, plug_id):
        pass

    @abstractmethod
    def remove_socket_id_from_selection(self, socket_id):
        pass

    @abstractmethod
    def set_selection_as_heading(self):
        pass

    @abstractmethod
    def set_selection_as_sub_total(self):
        pass

    @abstractmethod
    def toggle_format(self):
        pass

    @abstractmethod
    def toggle_number_format(self):
        pass

    @abstractmethod
    def set_number_format_whole_number_to_selection(self):
        pass

    @abstractmethod
    def set_number_format_one_digit_to_selection(self):
        pass

    @abstractmethod
    def set_number_format_two_digit_to_selection(self):
        pass

    @abstractmethod
    def set_number_format_percent_to_selection(self):
        pass

    @abstractmethod
    def remove_format_from_selections(self):
        pass

    @abstractmethod
    def remove_number_format_from_selections(self):
        pass

    @abstractmethod
    def set_format_heading(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def set_format_sub_total(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def set_whole_number(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def set_one_digit(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def set_two_digit(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def set_percent(self, shape_ids: Iterable):
        pass

    @property
    @abstractmethod
    def macro_commands(self) -> tuple:
        pass

    @abstractmethod
    def remove_format(self, shape_ids: Iterable):
        pass

    @abstractmethod
    def present_update_worksheets(self):
        pass

    @abstractmethod
    def add_inter_sheets_relays(self):
        pass

    @abstractmethod
    def add_the_same_plug_to_selection(self, plug_id: str):
        pass

    @abstractmethod
    def add_the_same_socket_to_selection(self, socket_id: str):
        pass

    @abstractmethod
    def export_vba_user_defined_function(self, file_name: str):
        pass

    @abstractmethod
    def register_all_keyboard_shortcuts(self, key_combos_dictionary: dict):
        pass

    @abstractmethod
    def load_keyboard_shortcut(self, name: str, key_combos: dict):
        pass

    @abstractmethod
    def change_active_keymap(self, keymap_name):
        pass

    @abstractmethod
    def set_command_name(self, index_: int, command_name: str, selection: tuple = ()):
        pass

    @abstractmethod
    def set_macro_args(self, index_: int, args_str: str, selection: tuple = ()):
        pass

    @abstractmethod
    def set_macro_kwargs(self, index_: int, kwargs_str: str, selection: tuple = ()):
        pass

    @abstractmethod
    def merge_macro(self, file_name: str):
        pass

    @abstractmethod
    def start_macro_recording(self):
        pass

    @abstractmethod
    def stop_macro_recording(self):
        pass

    @abstractmethod
    def add_command(self, key, args: tuple, kwargs: dict):
        pass

    @abstractmethod
    def add_command_always(self, key, args: tuple, kwargs: dict):
        pass

    @property
    @abstractmethod
    def commands(self) -> tuple:
        pass

    @abstractmethod
    def set_commands(self, data: tuple):
        pass

    @abstractmethod
    def copy_commands(self, indexes: tuple):
        pass

    @abstractmethod
    def paste_command(self, index_: int):
        pass

    @abstractmethod
    def delete_commands(self, indexes: tuple):
        pass

    @abstractmethod
    def clear_commands(self):
        pass

    @abstractmethod
    def toggle_macro_mode(self, value):
        pass

    @abstractmethod
    def delete_macros(self, file_names: tuple, next_position=None):
        pass

    @abstractmethod
    def delete_macro(self, file_name: str, next_position=None):
        pass

    @abstractmethod
    def save_macro(self, file_name: str):
        pass

    @abstractmethod
    def present_macros(self, file_name_to_select: str = None):
        pass

    @abstractmethod
    def shift_multiple_commands(self, indexes: tuple, shift: int) -> tuple:
        pass

    @abstractmethod
    def present_commands(self, select: tuple = ()):
        pass

    @abstractmethod
    def highlight_commands_containing_text_box_input(self, search_text: str, select: tuple = ()):
        pass

    @abstractmethod
    def add_bar_of_selected_accounts(self):
        pass

    @abstractmethod
    def add_a_y_axis_of_selected_accounts(self, coordinate: tuple = (), min_max: tuple = None):
        pass

    @abstractmethod
    def set_fill_to_selection(self, color):
        pass

    @abstractmethod
    def remove_fill_of_selection(self):
        pass

    @abstractmethod
    def add_slider_of_selected_input_accounts(self):
        pass

    @abstractmethod
    def save_slider_images(self, number_of_images, travel_range, direction):
        pass

    @abstractmethod
    def save_canvas_as_image(self, file_name):
        pass

    @abstractmethod
    def run_macro_fast(self, observer_passed: Callable = None) -> tuple:
        pass

    @abstractmethod
    def run_macro(self, observer_passed: Callable = None) -> tuple:
        pass

    @abstractmethod
    def turn_off_presenters(self):
        pass

    @abstractmethod
    def turn_on_presenters(self):
        pass

    @property
    @abstractmethod
    def cleared_commands(self) -> bool:
        pass

    @property
    @abstractmethod
    def is_macro_recording_mode(self) -> bool:
        pass

    @property
    @abstractmethod
    def turned_off_macro_recording(self) -> bool:
        pass

    @property
    @abstractmethod
    def turned_on_macro_recording(self) -> bool:
        pass

    @abstractmethod
    def save_data_table(self, file_name):
        pass

    @abstractmethod
    def calculate(self):
        pass

    @property
    @abstractmethod
    def sheet_name_to_pass_to_presenter(self):
        pass

    @abstractmethod
    def update_canvas(self):
        pass

    @abstractmethod
    def update_canvas_of_current_sheet(self):
        pass

    @abstractmethod
    def create_data_table(self):
        pass

    @abstractmethod
    def cache_audit_results(self):
        pass

    @abstractmethod
    def clear_cache_audit_results(self):
        pass

    @abstractmethod
    def cache_slider(self):
        pass

    @abstractmethod
    def clear_cache_slider(self):
        pass

    @abstractmethod
    def keyboard_shortcut_handler(self, modifiers: int, key: str):
        pass

    @abstractmethod
    def keyboard_shortcut_handler_silent(self, modifiers: int, key: str):
        pass

    @abstractmethod
    def save_any_data_as_pickle(self, file_name_abs_path, data):
        pass

    @abstractmethod
    def get_pickle_from_file_system(self, abs_path):
        pass

    @property
    @abstractmethod
    def get_all_group_and_names(self) -> tuple:
        pass

    @property
    @abstractmethod
    def get_list_of_templates(self) -> tuple:
        pass

    @property
    @abstractmethod
    def gateway_out_methods(self) -> tuple:
        pass

    @abstractmethod
    def export_input_setter_csv(self, file_name: str = None):
        pass

    @abstractmethod
    def load_inputs_from_csv(self, file_name: str = None):
        pass

    @abstractmethod
    def set_text_color_input(self, color: str):
        pass

    @abstractmethod
    def set_text_color_domestic_input(self, color: str):
        pass

    @abstractmethod
    def set_heading_color(self, color: str):
        pass

    @property
    @abstractmethod
    def text_color_input(self) -> Union[str, None]:
        pass

    @property
    @abstractmethod
    def text_color_domestic_input(self) -> Union[str, None]:
        pass

    @property
    @abstractmethod
    def heading_color(self) -> Union[str, None]:
        pass
