FROM python:3.10.12-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

ENV FLASK_APP="blacklists/src/main.py"

CMD ["flask", "run", "-h", "0.0.0.0", "--port=3000"]