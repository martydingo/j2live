from nicegui import ui

import os


class AppHeader:
    def __init__(self):
        AppHeaderContainer = ui.row()
        AppHeaderContainer.tailwind("w-full h-fit flex justify-between")
        with AppHeaderContainer:
            siteLogoContainer = ui.element('span')
            siteLogoContainer.tailwind("flex flex-col")
            with siteLogoContainer:
                ui.image(f"/static/logo_nord.png").tailwind("h-16 w-64")
                ui.label("Now purely in Python!").tailwind("place-self-end text-xs -mt-4 mr-5")