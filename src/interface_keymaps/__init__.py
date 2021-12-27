from abc import ABC
from abc import abstractmethod
from typing import Callable


class KeyMapABC(ABC):
    press = 'press'
    release = 'release'

    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'
    j = 'j'
    k = 'k'
    l = 'l'
    m = 'm'
    n = 'n'
    o = 'o'
    p = 'p'
    q = 'q'
    r = 'r'
    s = 's'
    t = 't'
    u = 'u'
    v = 'v'
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'

    f1 = 'F1'
    f2 = 'F2'
    f3 = 'F3'
    f4 = 'F4'
    f5 = 'F5'
    f6 = 'F6'
    f7 = 'F7'
    f8 = 'F8'
    f9 = 'F9'
    f10 = 'F10'
    f11 = 'F11'
    f12 = 'F12'

    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    zero = '0'

    minus = '-'
    equal = '='
    slash = '/'
    enter = 'Return'
    return_ = 'Return'
    back_space = 'BackSpace'
    delete = 'Delete'
    escape = 'Escape'

    up = 'Up'
    down = 'Down'
    left = 'Left'
    right = 'Right'

    none = 0
    shift = 1
    control = 4
    command = 8
    alt_option = 16
    function = 64

    @abstractmethod
    def add_new_keyboard_shortcut(self, key_combo: tuple, command: Callable):
        pass

    @abstractmethod
    def get_command_and_feedback(self, key_combo: tuple) -> str:
        pass

    @property
    @abstractmethod
    def keys(self) -> dict:
        pass


class KeyMapsABC(ABC):
    @abstractmethod
    def add_keymap(self, name):
        pass

    @abstractmethod
    def set_active_keymap(self, name):
        pass

    @property
    @abstractmethod
    def active_keymap(self) -> KeyMapABC:
        pass
