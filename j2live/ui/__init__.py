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

        editorContainer.tailwind("flex w-full h-full justify-evenly items-center")
        # ui.space().tailwind("basis-1/3")

        with editorContainer:
            inputContainer = ui.element("div")
            inputContainer.tailwind(
                "flex flex-col justify-center items-center basis-1/3"
            )

            outputContainer = ui.element("div")
            outputContainer.tailwind(
                "flex flex-col justify-center items-center basis-1/3"
            )

            with inputContainer:
                jinja2Editor = CodeEditor(
                    name="Jinja2Editor", language="jinja2", tailwind="min-h-[30rem]"
                )
                ui.space().tailwind("h-12")
                yamlEditor = CodeEditor(
                    name="YAMLEditor", language="yaml", tailwind="min-h-[30rem]"
                )
            with outputContainer:
                outputEditor = CodeEditor(
                    name="OutputEditor", language="", tailwind="min-h-[64rem]"
                )

    def setStorage(self):
        try:
            app.storage.browser["YAML"]
            app.storage.browser["YAML"] = {"value": {"x: 1"}}
        # except RuntimeError:
        #     pass
        except KeyError:
            app.storage.browser["YAML"] = {"value": {"x: 1"}}

        try:
            app.storage.browser["Jinja2"]
            app.storage.browser["Jinja2"] = {"value": {"{{ x }}"}}
        # except RuntimeError:
        #     pass
        except KeyError:
            app.storage.browser["Jinja2"] = {"value": {"{{ x }}"}}

        try:
            app.storage.browser["Output"]
        # except RuntimeError:
        #     pass
        except KeyError:
            app.storage.browser["Output"] = {
                "value": renderTemplate(
                    yamlVars=app.storage.browser["YAML"],
                    jinjaTemplate=app.storage.browser["Jinja2"],
                )["result"]
            }

    def setRootPageStyles(self):
        app.add_static_files("/static", f"{os.getcwd()}/j2live/ui/static")

        ui.dark_mode(True)

        NordTheme()

        ui.query("#c3").classes(
            add="min-w-screen max-w-screen min-h-screen max-h-screen h-screen w-screen"
        )
