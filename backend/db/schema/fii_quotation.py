# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 13:39:42
##############################################################################

from datetime import date

from pydantic import BaseModel
from typing import (
    List,
    Optional
)

from .api import APISchema


class FIIQuotationCreateSchema(BaseModel):
    fii_code: str
    quotation_date: date
    open_value: float
    high_value: float
    low_value: float
    close_value: float
    volume: Optional[int]


class FIIQuotationDeleteSchema(BaseModel):
    pk: int


class FIIQuotationSchema(BaseModel):
    pk: int
    fii_code: str
    quotation_date: date
    open_value: float
    high_value: float
    low_value: float
    close_value: float
    volume: Optional[int]


class FIIQuotationsResponseSchema(APISchema):
    fii_quotations: List[FIIQuotationSchema]

