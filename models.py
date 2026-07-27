from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class TransationType(BaseModel):
    valor: Decimal
    dataHora: datetime