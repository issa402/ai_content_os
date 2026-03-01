# Stage 1: Build the Go applications
FROM golang:1.19-alpine AS builder

WORKDIR /app

# Copy all go files
COPY . .

# Build the Go services
RUN go build -o /app/api-gateway/api-gateway ./api-gateway
RUN go build -o /app/orchestration-service/orchestration-service ./orchestration-service
RUN go build -o /app/ingestion-service/ingestion-service ./ingestion-service
RUN go build -o /app/video-assembly-service/video-assembly-service ./video-assembly-service
RUN go build -o /app/posting-service/posting-service ./posting-service
RUN go build -o /app/analytics-service/analytics-service ./analytics-service

# Stage 2: Setup Python environment
FROM python:3.9-slim

WORKDIR /app

# Copy requirements file and install dependencies
COPY ai-services/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python services source code
COPY ai-services/ .

# Stage 3: Final image
FROM alpine:latest

WORKDIR /root/

# Copy the built Go binaries from the builder stage
COPY --from=builder /app/api-gateway/api-gateway .
COPY --from=builder /app/orchestration-service/orchestration-service .
COPY --from=builder /app/ingestion-service/ingestion-service .
COPY --from=builder /app/video-assembly-service/video-assembly-service .
COPY --from=builder /app/posting-service/posting-service .
COPY --from=builder /app/analytics-service/analytics-service .

# Copy the Python services and dependencies from the python stage
COPY --from=1 /app /app

# Expose ports for the services
EXPOSE 8080 8081 8082 8083 8084 8085 5001 5002 5003

# TODO: Add a command to start all the services
CMD ["./api-gateway"]
