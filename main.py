import re

import uvicorn
from config import max_num_of_messages_per_queue
from fastapi import FastAPI
import logging
from asyncio import Queue

logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(message)')

queue = Queue(maxsize=max_num_of_messages_per_queue)

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello, message queue"}


@app.get('/queue/{queue_n}')
async def push(queue_n : str, msg : str):
    pass




if __name__ == "__main__":
    uvicorn.run(host='localhost', port=7500)