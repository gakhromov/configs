# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401


mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
network_interface = 'wlan0'


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "Tab", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod, "control"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    
    # Launch stuff
    Key([mod], "space", lazy.spawn('dmenu_run -fn "sans"'),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn('chromium'), desc="Launch browser"),

    # Circle through groups
    Key([mod], "Right", lazy.screen.next_group(), desc="Move to next group"),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Move to previous group"),

    # Toggle window mode
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle window floating"),
    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="Toggle window fullscreen"),
    
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 1")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 1")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10-")),
]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("TERM", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("DISC", {'layout': 'monadtall'}),
               ("MUSIC", {'layout': 'monadtall'}),
               ("OTHER", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 0,
                "margin": 5,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    layout.Floating(**layout_theme)
]

colors = [["#292d3e", "#292d3e"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#8d62a9", "#8d62a9"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#ffffff", "#ffffff"]] # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

callbacks = {
    'update': {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
    'memory': {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
    'wifi':   {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e iwctl')},
}


widgets_list = [
          # Separator
          widget.Sep(
                   linewidth = 0,
                   padding = 6,
                   foreground = colors[2],
                   background = colors[0]
                   ),

          # Groups
          widget.GroupBox(
                   font = "Ubuntu Bold",
                   fontsize = 9,
                   margin_y = 3,
                   margin_x = 0,
                   padding_y = 5,
                   padding_x = 3,
                   borderwidth = 3,
                   active = colors[2],
                   inactive = colors[2],
                   rounded = False,
                   highlight_color = colors[1],
                   highlight_method = "line",
                   this_current_screen_border = colors[3],
                   this_screen_border = colors [4],
                   other_current_screen_border = colors[0],
                   other_screen_border = colors[0],
                   foreground = colors[2],
                   background = colors[0]
                   ),

          # Prompt
          widget.Prompt(
                   prompt = prompt,
                   font = "Ubuntu Mono",
                   padding = 10,
                   foreground = colors[3],
                   background = colors[1]
                   ),

          # Separator
          widget.Sep(
                   linewidth = 0,
                   padding = 40,
                   foreground = colors[2],
                   background = colors[0]
                   ),

          # Window name
          widget.WindowName(
                   foreground = colors[6],
                   background = colors[0],
                   padding = 0
                   ),
          
          # Systray
          widget.Systray(
                   background = colors[0],
                   padding = 5
                   ),

          # Pacman updates
          widget.TextBox(
                   text='',
                   background = colors[0],
                   foreground = colors[5],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.Pacman(
                   update_interval = 1800,
                   foreground = colors[2],
                   mouse_callbacks = callbacks['update'],
                   background = colors[5]
                   ),
          widget.TextBox(
                   text = "Updates",
                   padding = 5,
                   mouse_callbacks = callbacks['update'],
                   foreground = colors[2],
                   background = colors[5]
                   ),

          # Memory + htop on click
          widget.TextBox(
                   text = '',
                   background = colors[5],
                   foreground = colors[4],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.Memory(
                   foreground = colors[2],
                   background = colors[4],
                   mouse_callbacks = callbacks['memory'],
                   padding = 5
                   ),

          # Wifi
          widget.TextBox(
                   text='',
                   background = colors[4],
                   foreground = colors[5],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.TextBox(
                   text = '\uF1EB',
                   background = colors[5],
                   foreground = colors[2],
                   padding = 0,
                   fontsize = 12,
                   mouse_callbacks = callbacks['wifi'],
                   ),
          widget.Wlan(
                   interface = network_interface,
                   foreground = colors[2],
                   background = colors[5],
                   padding = 5,
                   mouse_callbacks = callbacks['wifi'],
                   ),

          # Volume
          widget.TextBox(
                   text = '',
                   background = colors[5],
                   foreground = colors[4],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.TextBox(
                   text = '\uF028',
                   background = colors[4],
                   foreground = colors[2],
                   padding = 0,
                   fontsize = 12
                   ),
          widget.TextBox(
                  text = ' Volume:',
                   foreground = colors[2],
                   background = colors[4],
                   padding = 0
                   ),
          widget.PulseVolume(
                   foreground = colors[2],
                   background = colors[4],
                   padding = 5
                   ),

          # Layouts
          widget.TextBox(
                   text = '',
                   background = colors[4],
                   foreground = colors[5],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.CurrentLayoutIcon(
                   custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                   foreground = colors[0],
                   background = colors[5],
                   padding = 0,
                   scale = 0.7
                   ),
          widget.CurrentLayout(
                   foreground = colors[2],
                   background = colors[5],
                   padding = 5
                   ),
          
          # Battery
          widget.TextBox(
                   text = '',
                   background = colors[5],
                   foreground = colors[4],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.TextBox(
                   text = '\uF240',
                   background = colors[4],
                   foreground = colors[2],
                   padding = 0,
                   fontsize = 12
                   ),
          widget.Battery(
                   foreground = colors[2],
                   background = colors[4],
                   format='{percent:2.0%} {hour:d}:{min:02d}',
                   padding = 5
                   ),

          # Clock
          widget.TextBox(
                   text = '',
                   background = colors[4],
                   foreground = colors[5],
                   padding = 0,
                   fontsize = 37
                   ),
          widget.TextBox(
                   text = '\uF017 ',
                   background = colors[5],
                   foreground = colors[2],
                   padding = 0,
                   fontsize = 12
                   ),
          widget.Clock(
                   foreground = colors[2],
                   background = colors[5],
                   format = "%A, %B %d  [ %H:%M ]"
                   ),

          # Separator
          widget.Sep(
                   linewidth = 0,
                   padding = 5,
                   foreground = colors[0],
                   background = colors[5]
                   ),
]


screens = [
    Screen(top=bar.Bar(widgets=widgets_list, opacity=1.0, size=20)),
]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
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

'''
@hook.subscribe.startup_once
def start_once():
    lazy.spawn('setxkbmap -layout us')
    # home = os.path.expanduser('~')
    # subprocess.call([home + '/.config/qtile/autostart.sh'])
'''

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
