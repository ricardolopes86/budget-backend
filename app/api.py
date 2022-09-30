from sqlalchemy.orm import Session
from .models import Gastos, Fixos, Variaveis


# def get_gastos(db: Session, skip: int = 0):
#     return db.query(Gastos).offset(skip).all()


def get_gastos(db: Session, mes: int, ano: int):
    return db.query(Gastos).filter(Gastos.mes == mes, Gastos.ano == ano).first()


def get_fixos(db: Session, mes: int, ano: int):
    return db.query(Fixos).filter(Fixos.mes == mes, Fixos.ano == ano).first()


def get_variaveis(db: Session, mes: int, ano: int):
    return db.query(Variaveis).filter(Variaveis.mes == mes, Variaveis.ano == ano).first()