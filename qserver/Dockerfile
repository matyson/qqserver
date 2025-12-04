FROM docker.io/python:3.11-slim
WORKDIR /app
COPY config.yaml .
RUN pip install bluesky-queueserver matplotlib
ENV QSERVER_CONFIG=/app/config.yaml
CMD ["start-re-manager", "--zmq-publish-console", "ON"]