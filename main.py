import re
from config import max_num_of_messages_per_queue
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello, message queue"}