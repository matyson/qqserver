FROM docker.io/python:3.11-slim

WORKDIR /app
COPY config.yaml .
RUN pip install bluesky-httpserver pandas
ENV QSERVER_HTTP_SERVER_CONFIG=/app/config.yaml

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "60610", "bluesky_httpserver.server:app"]