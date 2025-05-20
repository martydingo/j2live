from .components.AppHeader import AppHeader

from nicegui import ui

import os


@ui.page("/")
class UI():
    def __init__(self):
        self.setRootPageStyles()
        appContainer = ui.row()
        appContainer.tailwind("flex items-start w-full h-full")
        with appContainer:
            AppHeader()


    def setRootPageStyles(self):
        ui.dark_mode(True)
        ui.query('#c3').classes(add="min-w-screen max-w-screen min-h-screen max-h-screen")