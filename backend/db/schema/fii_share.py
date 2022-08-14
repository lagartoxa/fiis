# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 13:38:42
##############################################################################

from datetime import date

from pydantic import BaseModel
from typing import List

from .api import APISchema


class FIIShareCreateSchema(BaseModel):
    fii_code: str
    purchase_date: date
    value: float
    quantity: int


class FIIShareDeleteSchema(BaseModel):
    pk: int


class FIIShareSchema(BaseModel):
    pk: int
    fii_code: str
    purchase_date: date
    value: float
    quantity: int


class FIISharesResponseSchema(APISchema):
    fii_shares: List[FIIShareSchema]

