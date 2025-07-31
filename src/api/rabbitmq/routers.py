from fastapi import APIRouter
import api.rabbitmq.services as services
routers = APIRouter()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

@routers.get("/publish-message/")
async def publish_message(message: str):
    queue_name = "test"
    await services.publishMessage(queue_name=queue_name, message=message)
    return {"message": "Publish Message"}

@routers.get("/consume-message/")
async def consume_message():
    queue_name = "test"
    response = await services.consumeMessage(queue_name=queue_name, callback=callback)
    return response
