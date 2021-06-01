#config for keys of keyboard
#config by bryan

from libqtile.config import Key,Drag,Click
from libqtile.command import lazy
from libqtile.utils import guess_terminal

#define values keys
mod="mod4" #super
mod1="mod1" #alt
mod2="shift" #shift
mod3="control" #Ctrl
mod4="Return" #Enter
mod5="Tab"  #Tab
terminal = guess_terminal()

keys=[
    Key(key[0],key[1],*key[2:]) for key in [
    # Switch between windows
    ([mod],"Left",lazy.layout.left()),
    ([mod],"Right",lazy.layout.right()),
    ([mod],"Down",lazy.layout.down()),
    ([mod],"Up",lazy.layout.up()),
    ([mod],"space",lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    ([mod,mod2],"Left",lazy.layout.shuffle_left()),
    ([mod,mod2],"Right",lazy.layout.shuffle_right()),
    ([mod,mod2],"Down",lazy.layout.shuffle_down()),
    ([mod,mod2],"Up",lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ([mod,mod3],"Left",lazy.layout.grow_left()),
    ([mod,mod3],"Right",lazy.layout.grow_right()),
    ([mod,mod3],"Down",lazy.layout.grow_down()),
    ([mod,mod3],"Up",lazy.layout.grow_up()),
    ([mod],"n",lazy.layout.normalize()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    ([mod,mod2],mod4,lazy.layout.toggle_split()),
    ([mod],mod4,lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    ([mod],mod5,lazy.next_layout()),
    ([mod],"w",lazy.window.kill()),

    ([mod,mod3],"r",lazy.restart()),
    ([mod,mod3],"q",lazy.shutdown()),
    ([mod], "r",lazy.spawn("rofi -show run")),
    ([mod], "f",lazy.spawn("thunar")),
    # Volume
    ([mod1],"Down",lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([mod1],"Up",lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([mod1],"m",lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),     
    ([mod1,mod2],"z",lazy.window.toggle_floating()),
    ([mod1,mod2],"x",lazy.window.toggle_fullscreen()),    
    ]
]

# Drag floating layouts.

mouse = [
    Drag([mod],"Button1",lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],"Button3",lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([],"Button2",lazy.window.bring_to_front())
]

#config for keys of keyboard
#config by bryan

from libqtile.config import Key,Drag,Click
from libqtile.command import lazy
from libqtile.utils import guess_terminal

#define values keys
mod="mod4" #super
mod1="mod1" #alt
mod2="shift" #shift
mod3="control" #Ctrl
mod4="Return" #Enter
mod5="Tab"  #Tab
terminal = guess_terminal()

keys=[
    Key(key[0],key[1],*key[2:]) for key in [
    # Switch between windows
    ([mod],"Left",lazy.layout.left()),
    ([mod],"Right",lazy.layout.right()),
    ([mod],"Down",lazy.layout.down()),
    ([mod],"Up",lazy.layout.up()),
    ([mod],"space",lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    ([mod,mod2],"Left",lazy.layout.shuffle_left()),
    ([mod,mod2],"Right",lazy.layout.shuffle_right()),
    ([mod,mod2],"Down",lazy.layout.shuffle_down()),
    ([mod,mod2],"Up",lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ([mod,mod3],"Left",lazy.layout.grow_left()),
    ([mod,mod3],"Right",lazy.layout.grow_right()),
    ([mod,mod3],"Down",lazy.layout.grow_down()),
    ([mod,mod3],"Up",lazy.layout.grow_up()),
    ([mod],"n",lazy.layout.normalize()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    ([mod,mod2],mod4,lazy.layout.toggle_split()),
    ([mod],mod4,lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    ([mod],mod5,lazy.next_layout()),
    ([mod],"w",lazy.window.kill()),

    ([mod,mod3],"r",lazy.restart()),
    ([mod,mod3],"q",lazy.shutdown()),
    ([mod], "r",lazy.spawn("rofi -show run")),
    ([mod], "f",lazy.spawn("thunar")),
    # Volume
    ([mod1],"Down",lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([mod1],"Up",lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([mod1],"m",lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),     
    ([mod1,mod2],"z",lazy.window.toggle_floating()),
    ([mod1,mod2],"x",lazy.window.toggle_fullscreen()),    
    ]
]

# Drag floating layouts.

mouse = [
    Drag([mod],"Button1",lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],"Button3",lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod],"Button2",lazy.window.bring_to_front())
]

