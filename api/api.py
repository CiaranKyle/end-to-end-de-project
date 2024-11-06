from fastapi import FastAPI, Response, status, HTTPException, Query
from pydantic import BaseModel
import json

app = FastAPI()

"""Healthcheck API"""

@app.get("/healthcheck")
def handle_healthcheck():
    return {"message": "server is running!"}