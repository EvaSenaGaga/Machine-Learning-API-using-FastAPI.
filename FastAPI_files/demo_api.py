from fastapi import FastAPI
import sys
sys.path.insert(0, '../src')
import unittest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
