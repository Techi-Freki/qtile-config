from enum import unique, Enum


@unique
class Colors(Enum):
    BLACK = "#001219"
    DARKBLUE = "#005f73"
    BLUE = "#0a9396"
    LIGHTBLUE = "#94d2bd"
    WHITE = "#e9d8a6"
    YELLOW = "#ee9b00"
    ORANGE = "#ca6702"
    BURNTORANGE = "#bb3e03"
    RED = "#ae2012"
    DARKRED = "#9b2226"

    @property
    def index(self):
        return list(Colors).index(self)
