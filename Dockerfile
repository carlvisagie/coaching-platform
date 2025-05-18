FROM python:3.10-slim

WORKDIR /app

COPY backend /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "main:gunicorn_app", "--bind", "0.0.0.0:8080"]


