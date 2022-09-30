from datetime import date
from pydantic import BaseModel


class FixosBase(BaseModel):
    Contas: float
    Assinaturas: float
    Seguros: float
    Mesadas: float
    Impostos: float
    Outros: float
    mes: int
    ano: int


class GastosBase(BaseModel):
    Fixos: float
    Variaveis: float
    Salario: float
    mes: int
    ano: int


class VariaveisBase(BaseModel):
    Compras: float
    Restaurantes: float
    Mercado: float
    Carro: float
    mes: int
    ano: int


class ContasBase(BaseModel):
    Nome: str
    Valor: float
    Vencimento: date
    ContaDePagamento: str
    FormaDePagamento: str


class Fixos(FixosBase):
    class Config:
        orm_mode = True


class Gastos(GastosBase):
    class Config:
        orm_mode = True


class Variaveis(VariaveisBase):
    class Config:
        orm_mode = True


class Contas(ContasBase):
    class Config:
        orm_mode = True