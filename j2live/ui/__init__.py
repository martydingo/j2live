from .theme import NordTheme

from .components.AppHeader import AppHeader
from .components.CodeEditor import CodeEditor
from ..ansible import renderTemplate
from nicegui import ui, app

import os


@ui.page(path="/", title="J2Live", favicon="favicon.ico")
class UI:
    def __init__(self):
        self.setRootPageStyles()
        self.setStorage()

        AppHeader()
        
        editorContainer = ui.element("div")
        editorContainer.tailwind("flex w-full h-full justify-evenly items-start")

        with editorContainer:
            inputContainer = ui.element("div")
            inputContainer.tailwind(
                "flex flex-col justify-center items-center basis-5/12"
            )

            outputContainer = ui.element("div")
            outputContainer.tailwind(
                "flex flex-col justify-center items-center basis-5/12"
            )

            with inputContainer:
                CodeEditor(
                    name="YAMLEditor", language="yaml", tailwind="min-h-[32rem]"
                )
                ui.space().tailwind("h-12")
                CodeEditor(
                    name="Jinja2Editor", language="jinja2", tailwind="min-h-[32rem]"
                )
            with outputContainer:
                CodeEditor(
                    name="OutputEditor", language="", tailwind="min-h-[68rem]"
                )

    def setStorage(self):
        try:
            app.storage.browser["YAML"]
        except KeyError as errorMsg:
            app.storage.browser["YAML"] = {"value": "x: 1"}

        try:
            app.storage.browser["Jinja2"]
        except KeyError:
            app.storage.browser["Jinja2"] = {"value": "{{ x }}"}

        try:
            app.storage.browser["Output"]
        # except RuntimeError:
        #     pass
        except KeyError:
            app.storage.browser["Output"] = {
                "value": renderTemplate(
                    yamlVars=app.storage.browser["YAML"]["value"],
                    jinjaTemplate=app.storage.browser["Jinja2"]["value"],
                )["result"]
            }
            

    def setRootPageStyles(self):
        app.add_static_files("/static", f"{os.getcwd()}/j2live/ui/static")

        ui.dark_mode(True)

        NordTheme()

        ui.query("#c3").classes(
            add="min-w-screen max-w-screen min-h-screen max-h-screen h-screen w-screen"
        )
