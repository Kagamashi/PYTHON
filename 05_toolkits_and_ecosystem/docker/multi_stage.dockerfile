# Stage 1: Build dependencies
FROM python:3.11 AS builder
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
