from .ui import UI
from nicegui import ui
from fastapi import FastAPI

app = FastAPI()

class J2Live():
    def __init__(self):
        UI()

    ui.run_with(
        app=app,
        storage_secret="test123"
    )