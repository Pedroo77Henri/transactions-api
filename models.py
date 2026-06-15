from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class MeuModelo(BaseModel):
    valor: Decimal
    dataHora: datetime