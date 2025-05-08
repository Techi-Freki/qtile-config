from enum import Enum


class Icons(Enum):
    HOME = "󱂵"
    TERM = ""
    WEB = "󰾔"
    CODE = "󱃖"
    GITHUB = ""
    VIDEO = "󰃽"
    DISCORD = "󰙯"
    STEAM = ""
    SKULL = ""
    QTILE = ""
    CLOCK = "󰥔"
    X = "󰬟"
    XON = "󰰰"

    @property
    def index(self):
        return list(Icons).index(self)
