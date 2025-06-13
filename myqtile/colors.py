from enum import unique, Enum


@unique
class Colors(Enum):
    BLACK = "#09060d"
    DARKBLUE = "#1e2a50"
    BLUE = "#484e70"
    LIGHTBLUE = "#32789c"
    WHITE = "#feefd2"
    YELLOW = "#ffac36"
    ORANGE = "#ca4d15"
    BURNTORANGE = "#af2b27"
    RED = "#fe6b71"
    DARKRED = "#000"

    @property
    def index():
        return list(Colors).index(self)
