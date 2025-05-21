from nicegui import ui, app
from ...ansible import renderTemplate

import yaml


class CodeEditor:
    def __init__(self, name: str, language: str, tailwind=None):
        self.name = name

        editorContainer = ui.element("div")
        editorContainer.tailwind("w-full h-full flex flex-col")
        shortName = name.replace("Editor", "")

        with editorContainer:
            ui.label(shortName).classes("muted").tailwind(
                "indent-4 font-bold text-xs tracking-wider font-display"
            )
            codeEditor = ui.codemirror(
                language=language,
                theme="nord",
                line_wrapping=True if shortName == "Output" else False,
                on_change=self.handleChange,
            ).classes(name)

            if shortName == "Output":
                codeEditor.bind_value_from(app.storage.browser[shortName])
            else:
                codeEditor.bind_value(app.storage.browser[shortName])

        self.editor = codeEditor

        if tailwind != None:
            codeEditor.tailwind(tailwind + " font-mono")

    def handleChange(event):
        editorName = event.name

        match editorName:
            case "YAMLEditor":
                jinjaTemplate = app.storage.browser["Jinja2"]["value"]
                yamlVars = app.storage.browser["YAML"]["value"]    
                renderResult = renderTemplate(yamlVars=yamlVars, jinjaTemplate=jinjaTemplate)
                app.storage.browser["Output"]["value"] = renderResult["result"] if renderResult["error"] == False else ui.notify(message=renderResult['result'], type="negative")
                
                
            case "Jinja2Editor":
                jinjaTemplate = app.storage.browser["Jinja2"]["value"]
                yamlVars = app.storage.browser["YAML"]["value"]
                renderResult = renderTemplate(yamlVars=yamlVars, jinjaTemplate=jinjaTemplate)
                app.storage.browser["Output"]["value"] = renderResult["result"] if renderResult["error"] == False else ui.notify(message=renderResult['result'], type="negative")
                
                
                
