from nicegui import ui, app


class CodeEditor:
    def __init__(self, name: str, language: str, tailwind=None):
        self.name = name
        print(app.storage.browser)
        editorContainer = ui.element("div")
        editorContainer.tailwind("w-full h-full flex flex-col")
        shortName = name.replace("Editor", "")
        print(shortName)
        with editorContainer:
            ui.label(shortName).classes("muted").tailwind(
                "indent-4 font-bold text-xs tracking-wider font-display mb-2"
            )
            codeEditor = ui.codemirror(
                language=language,
                theme="nord",
                on_change=self.handleChange,
            ).classes(name)
            # codeEditor.bind_value(app.storage.browser[shortName])

        self.editor = codeEditor

        if tailwind != None:
            codeEditor.tailwind(tailwind + " font-mono")

    def handleChange(event):
        editorName = event.name
        editor = event.editor

        match editorName:
            case "YAMLEditor":
                jinjaEditor = ui.query(".Jinja2Editor").element.tailwind("h-2")
                print(jinjaEditor.element.__dict__)
            case "Jinja2Editor":
                print("Jinja2")
