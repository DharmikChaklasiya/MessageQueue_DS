import re

import uvicorn
from config import max_num_of_messages_per_queue
from fastapi import FastAPI
import logging
from asyncio import Queue

LOCAL_HOST = "127.0.0.1"

logging.basicConfig(filename='logging.log')

queue = Queue(maxsize=max_num_of_messages_per_queue)
queues = {}

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello, message queue"}


@app.get('/queue/{queue_n}')
async def push(queue_n : str):
    return {"message":f"queue nr.{queue_n}"}




if __name__ == "__main__":
    uvicorn.run(app, host=LOCAL_HOST, port=7500)