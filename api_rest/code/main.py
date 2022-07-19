from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import pyrebase

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


