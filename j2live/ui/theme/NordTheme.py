from nicegui import ui
from enum import Enum
import os


class Theme:
    def __init__(self):
        ui.add_head_html(
            '<link rel="stylesheet" type="text/css" href="static/styles.css">'
        )


class NordColors(Enum):
    nord0 = "#2e3440"
    nord1 = "#3b4252"
    nord2 = "#434c5e"
    nord3 = "#4c566a"
    nord4 = "#d8dee9"
    nord5 = "#e5e9f0"
    nord6 = "#eceff4"
    nord7 = "#8fbcbb"
    nord8 = "#88c0d0"
    nord9 = "#81a1c1"
    nord10 = "#5e81ac"
    nord11 = "#bf616a"
    nord12 = "#d08770"
    nord13 = "#ebcb8b"
    nord14 = "#a3be8c"
    nord15 = "#b48ead"


class NordTheme(Theme):
    def __init__(self):
        super().__init__()

        ui.colors(
            primary=NordColors.nord7,
            secondary="",
            accent="",
            dark="",
            dark_page=NordColors.nord1,
            positive="",
            negative="",
            info="",
            warning="",
        )

        ui.add_css(
            """
                body.body--dark {
                    color: #eceff4 !important;
                }

                .muted {
                    color: #d8dee9 !important;
                }
            """
        )
