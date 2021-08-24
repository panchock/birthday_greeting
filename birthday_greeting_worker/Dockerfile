FROM faucet/python3

RUN pip install pika

COPY . /app

CMD python /app/worker.py
