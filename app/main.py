from fastapi import Depends, FastAPI, HTTPException, status
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


@app.get('/')
def index():
    print(f'chegou no index')
    return {"error": "not found"}


@app.get('/api/v1/gastos/{mes}/{ano}/', response_model=schemas.Gastos)
def read_gastos(mes: int, ano: int, db: Session = Depends(get_db)):
    if mes is None or ano is None:
        raise HTTPException(status_code=404, detail="Mes or Ano not found")

    gastos = api.get_gastos(db, mes=mes, ano=ano)
    return gastos


@app.post('/api/v1/gastos', response_model=schemas.Gastos)
def criar_gasto(gasto: schemas.Gastos, db: Session = Depends(get_db)):
    gastos = api.create_gasto(db=db, gasto=gasto)
    return gastos


@app.get("/api/v1/fixos/{mes}/{ano}/", response_model=schemas.Fixos)
def read_fixos(mes: int, ano: int, db: Session = Depends(get_db)):
    fixos = api.get_fixos(db, mes=mes, ano=ano)
    return fixos


@app.get("/api/v1/variaveis/{mes}/{ano}/", response_model=schemas.Variaveis)
def read_variaveis(mes: int, ano: int, db: Session = Depends(get_db)):
    variaveis = api.get_variaveis(db, mes=mes, ano=ano)
    return variaveis
