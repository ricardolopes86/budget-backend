from sqlalchemy.orm import Session
from .models import Gastos, Fixos, Variaveis


# def get_gastos(db: Session, skip: int = 0):
#     return db.query(Gastos).offset(skip).all()


def get_gastos(db: Session, mes: int, ano: int):
    return db.query(Gastos).filter(Gastos.mes == mes, Gastos.ano == ano).first()


def create_gasto(db: Session, gasto: Gastos):
    gasto = Gastos(Fixos=gasto.Fixos, Variaveis=gasto.Variaveis,
                   Salario=gasto.Salario, mes=gasto.mes, ano=gasto.ano)
    db.add(gasto)
    db.commit()
    db.refresh(gasto)
    return gasto


def create_variavel(db: Session, gasto: Variaveis):
    gasto = Variaveis(Compras=gasto.Compras, Restaurantes=gasto.Restaurantes,
                      Mercado=gasto.Mercado, Carro=gasto.Carro, mes=gasto.mes, ano=gasto.ano)
    db.add(gasto)
    db.commit()
    db.refresh(gasto)
    return gasto


def get_fixos(db: Session, mes: int, ano: int):
    return db.query(Fixos).filter(Fixos.mes == mes, Fixos.ano == ano).first()


def get_variaveis(db: Session, mes: int, ano: int):
    return db.query(Variaveis).filter(Variaveis.mes == mes, Variaveis.ano == ano).first()
