from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List
import pyrebase
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()
firebaseConfig = {
  "apiKey": "AIzaSyB_RkuuPEyDrwiiMfXtCnTB7YGrVEI5i6I",
  "authDomain": "apirest-af221.firebaseapp.com",
  "databaseURL": "https://apirest-af221-default-rtdb.firebaseio.com",
  "projectId": "apirest-af221",
  "storageBucket": "apirest-af221.appspot.com",
  "messagingSenderId": "296718360403",
  "appId": "1:296718360403:web:522d8aff0cd4e12e0c0ba6"
}

firebase=pyrebase.initialize_app(firebaseConfig)

securityBasic=HTTPBasic()
securityBearer=HTTPBearer()

class Usuarios_nuevos(BaseModel): 
    email: str
    password: str


origins = [
    "https://8080-yesenia19-apirest2-bisfphn4p0y.ws-us54.gitpod.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello world"}

@app.get("/user/validate",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa el token de un usuario", # aparece en la documentacion de la api
    description="Regresa el token de un usuario",
    tags=["auth"]
    )
async def get_token(credentials: HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth=firebase.auth()
        user= auth.sign_in_with_email_and_password(email, password)
        response = {
            "token" : user['idToken']
        }
        return response
    except Exception as error:
        print(f"ERROR:{error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.get("/user/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa información de un usuario", # aparece en la documentacion de la api
    description="Regresa información de un usuario",
    tags=["auth"]
    )

async def get_user(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth=firebase.auth()
        user= auth.get_account_info(credentials.credentials)
        uid = user["users"][0]["localId"]

        db =firebase.database()
        user_data =db.child("usuarios").child(uid).get().val()
        response = {
            "Datos de usuario" : user_data
        }
        return response
    except Exception as error:
        print(f"ERROR:{error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.post("/user/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Crea un usuario", # aparece en la documentacion de la api
    description="Crea un usuario",
    tags=["Users"]
    )
async def POST_user(usuario: Usuarios_nuevos):
    try:
        auth=firebase.auth()
        db =firebase.database()
        user= auth.create_user_with_email_and_password(usuario.email, usuario.password)
        uid = user["localId"]
        db.child("usuarios").child(uid).set({"user_name": usuario.email, "level": "user" })
        response = {"mensaje":"Usario agregado"}
        return  response
    except Exception as error:
        print(f"ERROR:{error}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
