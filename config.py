import os

from libqtile import bar, layout, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget

from myqtile.colors import Colors
from myqtile.icons import Icons
from myqtile.hooks import autostart
# from myqtile.functions import name_screenshot
from myqtile.open_weather import geolocation, city_id
from myqtile.bars.decorations import MyDecorations

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "j", lazy.next_screen(), desc="Move to next monitor"),
    Key([mod, "control"], "l", lazy.spawn("rofi -show window -show-icons"), desc="Select from a list of opened windows"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Launch an application with Rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch the Brave browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch the Thunar file manager"),
    # Key(["print"], lazy.application(f"gscreenshot -f {os.cwd() + '/Pictures/' + name_screenshot()}"), desc="Launch the Thunar file manager"),
    # Key([mod, "control"], "print", lazy.application(f"gnome-screenshot -a -f {os.cwd() + '/Pictures/' + name_screenshot()}"), desc="Launch the Thunar file manager"),
    # Key([mod, "alt"], "print", lazy.application(f"gnome-screenshot -w -f {os.cwd() + '/Pictures/' + name_screenshot()}"), desc="Launch the Thunar file manager"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

group_icons = [
    Icons.HOME,
    Icons.TERM,
    Icons.WEB,
    Icons.CODE,
    Icons.GITHUB,
    Icons.VIDEO,
    Icons.DISCORD,
    Icons.STEAM,
    Icons.SKULL,
]

groups = [Group(str(group.index + 1), label=group.value) for group in group_icons]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # mod + control + group number = move focused window to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name),
                desc=f"Move focused window to group {i.name}",
            )
        ]
    )

layout_settings = {
    "margin": 7,
    "border_normal": Colors.DARKBLUE.value,
    "border_focus": Colors.RED.value,
    "border_width": 3,
}

layouts = [
    layout.MonadTall(**layout_settings),
    layout.MonadWide(**layout_settings),
    layout.Spiral(**layout_settings, ratio=0.5, increment_ration=0.0),
    layout.Max(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

powerline = MyDecorations.get_decorations()

_screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(Icons.QTILE.value, padding=20, fontsize=24, background=Colors.BLACK.value, foreground=Colors.WHITE.value, **powerline),
                widget.GroupBox(
                    other_current_screen_border=Colors.ORANGE.value,
                    this_screen_border=Colors.LIGHTBLUE.value,
                    other_screen_border=Colors.LIGHTBLUE.value,
                    fontsize=25,
                    highlight_method="line",
                    background=Colors.DARKBLUE.value,
                    highlight_color=Colors.BLACK.value,
                    this_current_screen_border=Colors.ORANGE.value,
                    active=Colors.WHITE.value,
                    inactive=Colors.BLUE.value,
                    **powerline),
                widget.Spacer(background=Colors.BLUE.value),
                widget.WindowName(fontsize=18, fmt="<b>{}</b>", background=Colors.BLUE.value, foreground=Colors.WHITE.value),
                widget.Spacer(background=Colors.BLUE.value, **powerline),
                widget.CurrentLayoutIcon(scale=0.4, padding=10, background=Colors.LIGHTBLUE.value, **powerline),
                widget.Systray(padding=10, background=Colors.YELLOW.value, foreground=Colors.WHITE.value),
                widget.OpenWeather(metric=False, coordinates=geolocation, cityid=city_id, format="{temp}°{units_temperature} {icon}", background=Colors.YELLOW.value, foreground=Colors.BLACK.value, padding=10),
                widget.Redshift(background=Colors.YELLOW.value, foreground=Colors.BLACK.value, **powerline),
                widget.Clock(format="%a, %B %d, %Y %H:%M", padding=5, background=Colors.ORANGE.value, foreground=Colors.BLACK.value),
                widget.TextBox(Icons.CLOCK.value, fontsize=20, padding=5, background=Colors.ORANGE.value, foreground=Colors.BLACK.value, **powerline),
                widget.QuickExit(default_text=Icons.X.value, countdown_format=Icons.XON.value, fontsize=20, padding=20, background=Colors.BURNTORANGE.value, foreground=Colors.BLACK.value),
            ],
            32,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    other_current_screen_border=Colors.ORANGE.value,
                    this_screen_border=Colors.LIGHTBLUE.value,
                    other_screen_border=Colors.LIGHTBLUE.value,
                    fontsize=25,
                    highlight_method="line",
                    background=Colors.DARKBLUE.value,
                    highlight_color=Colors.BLACK.value,
                    this_current_screen_border=Colors.ORANGE.value,
                    active=Colors.WHITE.value,
                    inactive=Colors.BLUE.value,
                    **powerline),
                widget.Spacer(background=Colors.BLUE.value),
                widget.WindowName(fontsize=18, fmt="<b>{}</b>", background=Colors.BLUE.value, foreground=Colors.WHITE.value),
                widget.Spacer(background=Colors.BLUE.value, **powerline),
                widget.CurrentLayoutIcon(scale=0.4, padding=10, background=Colors.LIGHTBLUE.value),
            ],
            32,
        ),
    ),
]

screens = [
        _screens[1],
        _screens[0]
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart()
