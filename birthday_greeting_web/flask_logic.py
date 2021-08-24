import uuid
import pika
import json
from config import RABBITMQ_ADDR


def create_logic(body) -> str:
    conn = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_ADDR))
    channel = conn.channel()

    channel.queue_declare('greetings')
    body['id'] = str(uuid.uuid4())
    channel.basic_publish(exchange='', routing_key='greetings', body=json.dumps(body))

    return body['id']


def check_logic(id: str) -> str:
    return "/"
