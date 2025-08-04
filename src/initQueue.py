import json
from uuid import uuid4

from fastapi import logger
from src.api.rabbitmq.models import RabbitMQ

queueManager = RabbitMQ()

def callback(ch, method, properties, body):
    id = str(uuid4())
    logger.info(f'call.log:{id}: {body} is received')
    body_json = json.loads(body)
    try:
        logger.info(f"get new process message {id}")
    except Exception as error:
        logger.error(error)

def start_consume_call(): 
    queueManager.consume('test', callback)

if __name__ == "__main__":
    start_consume_call()
