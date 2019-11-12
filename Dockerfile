FROM python:3.8.0-alpine3.10

WORKDIR /app
COPY requirements.txt main.py ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
