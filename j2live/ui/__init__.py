from .theme import NordTheme

from .components.AppHeader import AppHeader
from .components.CodeEditor import CodeEditor
from ..ansible import renderTemplate
from nicegui import ui, app

import os


@ui.page(path="/", title="J2Live", favicon="/static/favicon.ico")
class UI:
    def __init__(self):
        self.setRootPageStyles()
        self.setStorage()

        AppHeader()

        editorContainer = ui.element("div")
        editorContainer.classes("flex w-full h-full justify-evenly items-start")

        with editorContainer:
            inputContainer = ui.element("div")
            inputContainer.classes(
                "flex flex-col justify-center items-center basis-5/12"
            )

            outputContainer = ui.element("div")
            outputContainer.classes(
                "flex flex-col justify-center items-center basis-5/12"
            )

            with inputContainer:
                CodeEditor(name="YAMLEditor", language="yaml", classes="min-h-[32rem]")
                ui.space().classes("h-12")
                CodeEditor(
                    name="Jinja2Editor", language="jinja2", classes="min-h-[32rem]"
                )
            with outputContainer:
                CodeEditor(name="OutputEditor", language="", classes="min-h-[68rem]")

    def setStorage(self):
        try:
            app.storage.browser["YAML"]
        except KeyError as errorMsg:
            app.storage.browser["YAML"] = {
                "value": "functions:\n  - init\n  - main\n  - new\n  - clr"
            }

        try:
            app.storage.browser["Jinja2"]
        except KeyError:
            app.storage.browser["Jinja2"] = {
                "value": "class SomeClass(SomeBaseClassHere):\n  {% for name in functions %}\n  def __{{ name }}__(self, **kwargs):\n      super().__init__(**kwargs)\n  \n  {% endfor %}"
            }

        try:
            app.storage.browser["Output"]
        # except RuntimeError:
        #     pass
        except KeyError:
            app.storage.browser["Output"] = {
                "value": renderTemplate(
                    yamlVars=str(app.storage.browser["YAML"]["value"]),
                    jinjaTemplate=(app.storage.browser["Jinja2"]["value"]),
                )["result"]
            }

    def setRootPageStyles(self):
        app.add_static_files("/static", f"{os.getcwd()}/j2live/ui/static")

        ui.add_head_html("""
            <link rel="icon" type="image/png" href="/static/favicon-96x96.png" sizes="96x96" />
            <link rel="icon" type="image/svg+xml" href="/static/favicon.svg" />
            <link rel="shortcut icon" href="/static/favicon.ico" />
            <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png" />
            <meta name="apple-mobile-web-app-title" content="J2Live" />
            <link rel="manifest" href="/static/site.webmanifest" />
        """)
        # ui.add_body_html('<script src="https://unpkg.com/flourite@1.3.0"></script>')

        ui.dark_mode(True)

        NordTheme()

        ui.query("#c3").classes(
            add="min-w-screen max-w-screen min-h-screen max-h-screen h-screen w-screen"
        )
