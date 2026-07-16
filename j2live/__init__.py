import os

os.environ.setdefault("HOME", "/tmp")
os.environ.setdefault("ANSIBLE_HOME", "/tmp/.ansible")
os.environ.setdefault("ANSIBLE_LOCAL_TEMP", "/tmp/.ansible/tmp")
os.environ.setdefault("ANSIBLE_REMOTE_TEMP", "/tmp/.ansible/tmp")

import nicegui.run as nicegui_run

nicegui_run.setup = lambda: None

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
