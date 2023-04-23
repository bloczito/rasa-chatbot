FROM python:3.10.11-alpine3.17

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY main.py .

CMD ["python3", "main.py"]
