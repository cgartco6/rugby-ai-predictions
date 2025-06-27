# Dockerfile
FROM python:3.10-slim-bullseye

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# Run scheduler
CMD ["python", "-m", "src.telegram_bot.scheduler"]  # Fixed execution
