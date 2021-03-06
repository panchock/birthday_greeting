import time
import pika
from config import RABBITMQ_ADDR

conn = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_ADDR))
channel = conn.channel()

channel.queue_declare(queue='greetings')


def callback(ch, method, properties, body):
    print('creating greeting for {}'.format(body))
    time.sleep(10)
    print('created greeting for {}'.format(body))
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_consume(queue='greetings', on_message_callback=callback)

channel.start_consuming()
