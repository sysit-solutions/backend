from fastapi import FastAPI
from freenit.config import getConfig

from .api import api
from .config import configs

config = getConfig()
app = FastAPI()
app.mount("/api/v1", api)
