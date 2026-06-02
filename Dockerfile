FROM python:3.12-slim

WORKDIR /app

COPY . .

# Usamos la línea de la pizarra pero añadimos tus dependencias de base de datos y seguridad
RUN pip install fastapi[standard] sqlmodel pycryptodome

CMD ["fastapi", "run"]