from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date

from .database import Base


class Gastos(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    Fixos = Column(Float)
    Variaveis = Column(Float)
    Salario = Column(Float)
    mes = Column(Integer)
    ano = Column(Integer)


class Fixos(Base):
    __tablename__ = "fixos"

    id = Column(Integer, primary_key=True, index=True)
    Contas = Column(Float)
    Assinaturas = Column(Float)
    Seguros = Column(Float)
    Mesadas = Column(Float)
    Impostos = Column(Float)
    Outros = Column(Float)
    mes = Column(Integer)
    ano = Column(Integer)


class Variaveis(Base):
    __tablename__ = "variaveis"

    id = Column(Integer, primary_key=True, index=True)
    Compras = Column(Float)
    Restaurantes = Column(Float)
    Mercado = Column(Float)
    Carro = Column(Float)
    mes = Column(Integer)
    ano = Column(Integer)


class Contas(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    Nome = Column(String)
    Valor = Column(Float)
    Vencimento = Column(Date)
    ContaDePagamento = Column(String)
    FormaDePagamento = Column(String)