import uuid
import pika


def create_logic(body) -> str:
    conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = conn.channel()

    channel.queue_declare('greetings')
    body['id'] = str(uuid.uuid4())
    channel.basic_publish(exchange='', routing_key='greetings', body=body)

    return body['id']


def check_logic(id: str) -> str:
    return "/"
