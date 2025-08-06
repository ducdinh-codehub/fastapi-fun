from .models import RabbitMQ

rabbitMQManager = RabbitMQ()

async def publishMessage(queue_name: str, message: str):
    response = rabbitMQManager.publish(queue_name, message)
    return response

async def consumeMessage(queue_name: str, callback):
    response = rabbitMQManager.consume(queue_name, callback)
    return response
    