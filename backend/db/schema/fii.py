# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-13 15:42:42
##############################################################################

from pydantic import BaseModel
from typing import (
    List,
    Optional,
    Union
)

from .api import APISchema


class FIICreateSchema(BaseModel):
    name: str
    code: str
    value: float
    fii_type: str


class FIIDeleteSchema(BaseModel):
    pk: Optional[int]
    name: Optional[str]
    code: Optional[str]


class FIISchema(BaseModel):
    pk: int
    name: str
    code: str
    value: float
    fii_type: str


class FIIsResponseSchema(APISchema):
    fiis: List[FIISchema]

