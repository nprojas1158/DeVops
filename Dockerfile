FROM python:3.10.12-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

ENV FLASK_APP="blacklists/src/main.py"

CMD ["flask", "run", "-h", "0.0.0.0", "--port=3000", "-e","NEW_RELIC_LICENSE_KEY=INGEST_LICENSE"]

RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="docker"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=bf46757fafec63fe000cdade0fbf355bFFFFNRAL
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT [ "newrelic-admin", "run-program" ]