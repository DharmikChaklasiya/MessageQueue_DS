import datetime
from http.client import HTTPException
from msilib.schema import Class
import re
import uvicorn
from config import max_num_of_messages_per_queue
from fastapi import FastAPI
import logging
from asyncio import Queue
from pydantic import BaseModel

class Job(BaseModel):
    name: str
    t_stamp: datetime.datetime
    description: str


LOCAL_HOST = "127.0.0.1"

logging.basicConfig(level=logging.INFO,filename='logging.log', encoding='utf8')

queue = Queue(maxsize=max_num_of_messages_per_queue)
queues = {"jobs": queue}

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello, message queue"}

# TODO Implement
@app.post('/queue/{queue_n}/{role}')
async def push(queue_n : str, message : str, role : str):
    if role == "secretary":
        raise HTTPException(400,detail="insufficient privileges")
        
    queue = queues[queue_n]
    await queue.put(message)
    return {"message":"success"}


# TODO Implement
@app.get('/queue/{queue_n}/{role}')
async def pull(queue_n : str, message : str, role : str):
    if role != "admin" or role != "manager":
        raise HTTPException(400,detail="insufficient privileges")

    queue = queues[queue_n]
    content = await queue.get(message)
    return {"message":content}

# TODO Implement
@app.get('/queues')
async def list_out(role: str):
    if role != "admin" or role != "manager":
        raise HTTPException(400,detail="insufficient privileges")
    return {"message": list(queues.keys())}

# TODO Implement
@app.delete('/queue/{queue_n}/{role}')
async def delete(queue_n : str ,role : str):
    if role != "admin":
        return {"Insuficient privileges"}
    try:
        del queues[queue_n]
        return {"message":"success"}
    except Exception as exeption:
        raise HTTPException(400,detail=exeption)
        



if __name__ == "__main__":
    uvicorn.run(app, host=LOCAL_HOST, port=7500)