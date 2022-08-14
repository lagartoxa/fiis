# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 15:46:42
##############################################################################

from pydantic import BaseModel
from typing import (
    List,
    Optional,
    Union
)

from .api import APISchema


class FIITypeCreateSchema(BaseModel):
    name: str


class FIITypeDeleteSchema(BaseModel):
    pk: Optional[int]
    name: Optional[str]


class FIITypeSchema(BaseModel):
    pk: int
    name: str


class FIITypesResponseSchema(APISchema):
    fii_types: List[FIITypeSchema]

