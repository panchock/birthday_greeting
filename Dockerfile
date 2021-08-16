FROM faucet/python3

RUN pip install flask wtforms

COPY . /app

CMD python /app/main.py
