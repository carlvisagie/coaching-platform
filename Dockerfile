FROM python:3.10-slim

WORKDIR /app

# Copy backend files
COPY backend /app/backend

# Copy frontend static files
COPY frontend/static /app/backend/static

WORKDIR /app/backend

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
