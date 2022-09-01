# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-19 10:14:42
##############################################################################

from pydantic import BaseModel
from typing import List


class MonthSimulationBaseSchema(BaseModel):
    fii_code: str
    dividends_value: float
    shares_quantity: int
    fii_total: float


class MonthSimulationSchema(BaseModel):
    fiis: List[MonthSimulationBaseSchema]
    total: float

