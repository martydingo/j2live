from nicegui import ui, app
from ...ansible import renderTemplate

import yaml


class CodeEditor:
    # escapeStr = lambda self, string: string.replace("${", '${"${"}').replace("`", '${"`"}')
    def __init__(self, name: str, language: str, classes=None):
        self.name = name

        editorContainer = ui.element("div")
        editorContainer.classes("w-full h-full flex flex-col")
        shortName = name.replace("Editor", "")

        with editorContainer:
            ui.label(shortName).classes("muted").classes(
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

        if classes != None:
            codeEditor.classes(classes + " font-mono")

    def setOutput(self, value: str):
        app.storage.browser["Output"]["value"] = value

    def testYamlParsing(self, yamlVars):
        try:
            yaml.full_load(yamlVars)
            return True
        except Exception as errorMsg:
            return str(errorMsg)

    async def handleChange(self):
        editorName = self.name

        match editorName:
            case "YAMLEditor":
                jinjaTemplate = app.storage.browser["Jinja2"]["value"]
                yamlVars = app.storage.browser["YAML"]["value"]
                yamlParseResult = self.testYamlParsing(yamlVars)
                if yamlParseResult == True:
                    renderResult = renderTemplate(
                        yamlVars=yamlVars, jinjaTemplate=jinjaTemplate
                    )
                    self.setOutput(renderResult["result"])
                else:
                    self.setOutput(yamlParseResult)

            case "Jinja2Editor":
                jinjaTemplate = app.storage.browser["Jinja2"]["value"]
                yamlVars = app.storage.browser["YAML"]["value"]
                renderResult = renderTemplate(
                    yamlVars=yamlVars, jinjaTemplate=jinjaTemplate
                )

                self.setOutput(str(renderResult["result"]))

            # case "OutputEditor":
            #     escapedCode = self.escapeStr(str(self.editor.value))
            #     flouriteAnalysis = await ui.run_javascript(
            #             f"""
            #             const flourite = window.flourite;
            #             flourite(String.raw`{escapedCode}`);
            #             """)
            #     codeLanguage = flouriteAnalysis['language']
            #     self.editor.language = codeLanguage
