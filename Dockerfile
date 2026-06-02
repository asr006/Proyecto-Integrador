FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install fastapi[standard] sqlmodel pycryptodome

CMD ["fastapi", "run"]
