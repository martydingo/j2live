from nicegui import ui

import os


class AppHeader:
    def __init__(self):
        AppHeaderContainer = ui.row()
        AppHeaderContainer.tailwind("w-fit h-fit")
        with AppHeaderContainer:
            ui.image(f"/static/logo_nord.png").tailwind("h-16 w-64")
