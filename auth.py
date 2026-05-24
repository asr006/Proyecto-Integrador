import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

PEPPER = os.getenv("PEPPER")


def generar_hash(password: str):

    password_con_pepper = password + PEPPER

    salt = bcrypt.gensalt()

    hash_generado = bcrypt.hashpw(
        password_con_pepper.encode(),
        salt
    )

    return hash_generado.decode()


def verificar_password(password: str, hashed_password: str):

    password_con_pepper = password + PEPPER

    return bcrypt.checkpw(
        password_con_pepper.encode(),
        hashed_password.encode()
    )