# Build Stage
FROM python:3.11-slim AS build
RUN apt-get update && apt-get upgrade
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Run Stage
FROM python:3.11-slim AS run
WORKDIR /app
RUN pip install flask
COPY --from=build /app .
EXPOSE 8080
CMD ["python", "app.py"]
