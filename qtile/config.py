# A bunch of people who weren't me made this, i only changed the layout and colors, rice is easy just like 20 minutes in a pot of boiling water, no idea what everyone is going on about

import os
import socket
import re
import subprocess
import psutil

from typing import List  # noqa: F401
from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"
myTerm = "terminator"
terminal = guess_terminal()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

keys = [
    # Function keys
    #Key([], "F1", )
    # Switch between windows in current stack pane
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in stack pane"),
    #
    # # Move windows up or down in current stack
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(), desc="Move window up in current stack "),
    # # Switch window focus to other pane(s) of stack
    Key([mod, "shift"], "Left", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),
    # # Swap panes of split stack
    Key([mod], "space", lazy.layout.rotate(), desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod, "control", "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "k", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a rofi run window"),
    Key([mod, "shift", "control"], "c", lazy.spawn("pycharm-professional"), desc="Spawns a Pycharm instance"),
    # # Sizing hotkeys
    Key([mod], "o", lazy.layout.normalize(), desc="Reset"),

    # MonadTall shrink and grow hotkeys
    Key([mod], "p", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc="Shrink the current layout"),
    Key([mod], "i", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc="Shrink the current layout"),

    #Key([], 'XF86AudioMute', lazy.spawn('amixer -c 0 -q set Master 2dB+')),
]

# groups = [Group(i) for i in "asdfuiop"]
#
# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),
#
#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])

group_names = [("Web", {'layout': 'monadtall', 'spawn': 'firefox'}),
                           ("Dev",  {'layout': 'monadtall', 'spawn': 'atom .config/qtile/config.py'}),
                           ("Steam", {'layout': 'max'}),
                           ("Music", {'layout': 'monadtall', 'spawn': 'spotify'}),
                           ("Status", {'layout': 'monadtall', 'spawn': 'htop'}),]

groups = [Group(name, **kwargs) for name, kwargs in group_names]


for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i) , lazy.group[name].toscreen())),
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))),


layouts = [
    layout.Max(),
    #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(
        border_focus = "2d6349",
        border_normal = "13463d"
        ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(
        border_focus = "2d6349",
        border_normal = "13463d"
        ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [
            ["#0f1e25", "#0f1e25"], #panel background
            ["#2d6349","#2d6349"],  #current tab background
            ["#ffffff","#ffffff"],  #font color for group names
            ["#14483c","#14483c"],  #border line color for current Tab
            ["#3f7553","#3f7553"],  #border line color for other tabs and widget_defaults
            ["#13463d","#13463d"],  #color for even widget_defaults
            ["c8e690","c8e690"],  #window name
         ]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

#GMem = (int)MemUsed / 1024

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/is_it_pre_timeskip.png",
                    background = colors[6]
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Clock(
                    foreground = colors[2],
                    background = colors[5],
                    format = "%A, %B %d     [%H:%M:%S]"
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.GroupBox(
                    font = "sans",
                    fontsize = 12,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 5,
                    active = colors[2],
                    inactive = colors[2],
                    rounded = True,
                    highlight_color = colors[1],
                    highlight_method = "line",
                    this_current_screen_border = colors[3],
                    this_screen_border = colors[4],
                    other_current_screen_border = colors[0],
                    other_screen_border = colors[0],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Prompt(
                    prompt = prompt,
                    font = "sans",
                    padding = 10,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 50,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.WindowName(
                    foreground = colors[2],
                    background = colors[0],
                    padding = 0
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/bar03.png",
                    background = colors[6]
                ),
                widget.Battery(
                    foreground = colors[2],
                    background = colors[4],
                    update_interval = 60,
                    unknown_char = '^?'
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/bar02.png",
                    background = colors[6]
                ),
                widget.Wlan(
                    foreground = colors[2],
                    background = colors[5],
                    interface = 'wlo1'
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/bar01.png",
                    background = colors[6]
                ),
                widget.CPU(
                    foreground = colors[2],
                    background = colors[4]
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/bar02.png",
                    background = colors[6]
                ),
                widget.Memory(
                    foreground = colors[2],
                    background = colors[5],
                    format = '{MemUsed}M/{MemTotal}M'
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/bar01.png",
                    background = colors[6]
                ),
                widget.Net(
                    foreground = colors[2],
                    background = colors[4]
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/assets/bar02.png",
                    background = colors[6]
                ),
                widget.Systray(
                    background = colors[5],
                    padding = 5
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[0],
                    background = colors[5]
                ),
                #widget.CurrentLayout(),
                #widget.GroupBox(),
                #widget.Prompt(),
                #widget.WindowName(),
                #widget.Chord(
                #    chords_colors={
                #        'launch': ("#000000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Systray(),
                #widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                #widget.QuickExit(),
            ],
            24,
        ),
        wallpaper="~/Downloads/Backgrounds/forestnight.jpg",
        wallpaper_mode="fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
