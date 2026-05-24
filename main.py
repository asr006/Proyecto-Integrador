from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from models import Usuario
from auth import generar_hash, verificar_password

app = FastAPI()

URL_BASE_DATOS = "sqlite:///users.db"
motor = create_engine(URL_BASE_DATOS)


@app.on_event("startup")
def iniciar_base_datos():
    SQLModel.metadata.create_all(motor)


@app.post("/register")
def registrar(username: str, password: str):
    with Session(motor) as sesion:

        usuario_existente = sesion.exec(
            select(Usuario).where(Usuario.username == username)
        ).first()

        if usuario_existente:
            raise HTTPException(
                status_code=400,
                detail="El usuario ya existe"
            )

        nuevo_usuario = Usuario(
            username=username,
            hashed_password=generar_hash(password)
        )

        sesion.add(nuevo_usuario)
        sesion.commit()

        return {
            "message": "Usuario registrado correctamente"
        }


@app.post("/login")
def login(username: str, password: str):

    with Session(motor) as sesion:

        usuario = sesion.exec(
            select(Usuario).where(Usuario.username == username)
        ).first()

        if not usuario:
            raise HTTPException(
                status_code=401,
                detail="Credenciales incorrectas"
            )

        if not verificar_password(password, usuario.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Credenciales incorrectas"
            )

        return {
            "message": "Inicio de sesión exitoso"
        }