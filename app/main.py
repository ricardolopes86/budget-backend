from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import api, models, schemas
from .database import SessionLocal, engine 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/gastos/{mes}/{ano}/', response_model=schemas.Gastos)
def read_gastos(mes: int, ano: int, db: Session = Depends(get_db)):
    
    if mes is None or ano is None:
        raise HTTPException(status_code=404, detail="Mes or Ano not found")

    gastos = api.get_gastos(db, mes=mes, ano=ano)
    return gastos


@app.get("/fixos/{mes}/{ano}/", response_model=schemas.Fixos)
def read_fixos(mes: int, ano: int, db: Session = Depends(get_db)):
    fixos = api.get_fixos(db, mes=mes, ano=ano)
    return fixos


@app.get("/variaveis/{mes}/{ano}/", response_model=schemas.Variaveis)
def read_variaveis(mes: int, ano: int, db: Session = Depends(get_db)):
    variaveis = api.get_variaveis(db, mes=mes, ano=ano)
    return variaveis