import time
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='greetings')


def callback(cg, method, properties, body):
    print('creating greeting for {}'.format(body))
    time.sleep(10)
    print('created greeting for {}'.format(body))


channel.basic_consume(queue='greetings', auto_ack=True, on_message_callback=callback)

channel.start_consuming()
