import os.path
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/myqtile/scripts/autostart.sh")
    subprocess.call(script)
