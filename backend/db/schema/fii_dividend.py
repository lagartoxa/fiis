# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 01:57:42
##############################################################################

from datetime import date

from pydantic import BaseModel
from typing import List

from .api import APISchema


class FIIDividendCreateSchema(BaseModel):
    fii_code: str
    base_date: date
    payment_date: date
    base_quotation: float
    dividend_yield: float
    value: float


class FIIDividendCreateManySchema(BaseModel):
    dividends: List[FIIDividendCreateSchema]


class FIIDividendDeleteSchema(BaseModel):
    pk: int


class FIIDividendSchema(BaseModel):
    pk: int
    fii_code: str
    base_date: date
    payment_date: date
    base_quotation: float
    dividend_yield: float
    value: float


class FIIDividendsResponseSchema(APISchema):
    fii_dividends: List[FIIDividendSchema]

