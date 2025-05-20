from nicegui import ui

import os

class AppHeader():
    def __init__(self):
        ui.image(f"{os.getcwd()}/j2live/ui/static/logo.png").tailwind("h-24 w-56")
            
