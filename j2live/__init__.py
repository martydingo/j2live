from .ui import UI
from nicegui import ui
from fastapi import FastAPI

import os

storageSecret = os.getenv("J2LIVE_STORAGE_SECRET")

app = FastAPI()


class J2Live:
    def __init__(self):
        UI()

    ui.run_with(
        app=app, storage_secret=storageSecret if storageSecret != None else "test123"
    )
