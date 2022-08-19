import hashlib  # importa la libreria hashlib permite generar un hash
import os # trabajar con rutas permitiendo que las ajuste de acuerdo al sistema operativo que se utilice 
from fastapi import Depends, FastAPI, HTTPException, status, Security

import sqlite3
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

import databases
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import insert, select, update, delete


DATABASE_URL="sqlite:///clientes.db"
metadata = MetaData() #DB schema

clientes =Table(
    'clientes', metadata,
    Column('id_cliente', Integer, primary_key=True),
    Column('nombre', String, nullable=False),
    Column('email', String, nullable=False),
)
database=databases.Database(DATABASE_URL)
engine=create_engine(DATABASE_URL)
metadata.create_all(engine)

class Usuarios_nuevos(BaseModel): 
    email: str
    password: str

class ClienteIN(BaseModel): 
    nombre: str
    email: str

class Cliente(BaseModel): 
    id_cliente:int
    nombre: str
    email: str

class actualizar(BaseModel): 
    id_cliente:int
    nombre: str
    email: str

class Message(BaseModel): 
    message: str


app= FastAPI()

@app.get("/", response_model=Message)
def root():
    return {"message": "Hello world"}


@app.get(
    "/clientes/",
    response_model=List[Cliente],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de clientes", # aparece en la documentacion de la api
    description="Regresa una lista de clientes",
    tags=["clientes"]
)
async def get_clientes():
        query = select(clientes)
        return await database.fetch_all(query)

@app.get(
    "/clientes/{id}",
    response_model=Cliente,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa un cliente", # aparece en la documentacion de la api
    description="Regresa un cliente",
    tags=["clientes"]
)
async def get_cliente(id:int):
        query = select(clientes).where(clientes.c.id_cliente==id)
        return await database.fetch_one(query)

@app.post(
    "/clientes/",
    response_model=Message,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Crea un cliente", # aparece en la documentacion de la api
    description="Crea un cliente",
    tags=["clientes"]
)
async def create_cliente(cliente:ClienteIN):
        query = insert(clientes).values(nombre=cliente.nombre, email=cliente.email)
        await database.execute(query)
        return {"message":"Cliente nuevo agregado"}

@app.put(
    "/clientes/{id}",
    response_model=Message,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza un cliente", # aparece en la documentacion de la api
    description="Actualiza un cliente",
    tags=["clientes"]
)
async def update_cliente(id:int,cliente:ClienteIN):
        query = update(clientes).where(clientes.c.id_cliente==id).values(nombre=cliente.nombre, email=cliente.email)
        await database.execute(query)
        return {"message":"Cliente actualizado correctamente"}

@app.delete(
    "/clientes/{id}",
    response_model=Message,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Borra un cliente", # aparece en la documentacion de la api
    description="Borra un cliente",
    tags=["clientes"]
)
async def delete_cliente(id:int):
        query = delete(clientes).where(clientes.c.id_cliente==id)
        await database.execute(query)
        return {"message":"Cliente eliminado"}