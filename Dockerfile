FROM python:3.10-slim

WORKDIR /app

COPY backend /app/backend

WORKDIR /app/backend

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "/app/backend/main.py"]

