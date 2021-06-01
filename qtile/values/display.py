from libqtile import bar, layout, widget
from libqtile.config import Screen
from .colors import colors




layouts = [
    layout.Max(),
    layout.MonadWide(
        border_focus=colors["purple"],
        margin=5,
    ),
    layout.Columns(
        border_focus=colors["purple"],
        margin=5,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack Nerd Font',
    fontsize=20,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Systray(), 
                widget.GroupBox(
                 active=colors["future"],
                 background=colors["black"],
                 block_highlight_text_color=colors["watermelon"],
                 borderwidth=5,
                 center_aligned=True,
                 disable_drag=True,
                 fontsize=26,
                 fontshadow=colors["future"],
                 padding_x=4,
                 highlight_method="line",
                 spacing=30,
                 font="Hack Nerd Font",
                ),
                widget.Sep(
                    linewidth=200,
                    background=colors["black"],
                    foreground=colors["black"],
                ),
                widget.Memory(
                    foreground=colors["future"],
                    background=colors["black"],
                    format="Ram:{MemUsed}M/{MemTotal}M",
                    padding=20,
                    fontsize=20,
                ),
                widget.Net(
                    format="NET({interface}):{up}   {down}",
                    padding=20,
                    background=colors["black"],
                    foreground=colors["future"],
                    fontsize=20,
                ),
                widget.Clock(
                    foreground=colors["future"],
                    background=colors["black"],
                    padding=22,
                    #font="Digital-7",
                    format="[ %Y-%m-%d ]-[  %H:%M:%S ]",
                    fontsize=20,

                ), 
            ],
            30,
            opacity=1,
            margin=0,
        ),
    ),
]
