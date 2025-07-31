from typing import Any
from fastapi import HTTPException, status
import pika

import config

class RabbitMQ:
    rabbitmq_user: str
    rabbitmq_password: str
    rabbitmq_host: str
    rabbitmq_port: int
    connection: Any
    channel: Any
    credentials: Any
    parameters: Any

    def __init__(self):
        self.rabbitmq_user = config.Settings().rabbitmq_user
        self.rabbitmq_password = config.Settings().rabbitmq_password
        self.rabbitmq_host = config.Settings().rabbitmq_host
        self.rabbitmq_port = config.Settings().rabbitmq_port
        self.credentials = pika.PlainCredentials(self.rabbitmq_user, self.rabbitmq_password)
        self.parameters = pika.ConnectionParameters(host=self.rabbitmq_host, port=self.rabbitmq_port, credentials=self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def initialeQueue(self, queue_name: str) -> Any:
        self.channel.queue_declare(queue=queue_name, durable=True)

    def publish(self, queue_name: str, message: str):
        if not self.channel:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Cannot establish connection to RabbitMQ",
                headers={"WWW-Authenticate": "Bearer"},
            )
        self.initialeQueue(queue_name)
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message,  properties=pika.BasicProperties(
                                       delivery_mode=2,  # make message persistent
                                   ))
        return f"Sent message to queue {queue_name}: {message}"
    
    def consume(self, queue_name, callback):
        if not self.channel:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Cannot establish connection to RabbitMQ",
                headers={"WWW-Authenticate": "Bearer"},
            )
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
        return f"Consume message from queue {queue_name}"
