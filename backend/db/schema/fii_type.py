# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 15:46:42
##############################################################################

from pydantic import BaseModel
from typing import (
    List,
    Union
)

from .api import APISchema


class FIITypeSchema(BaseModel):
    name: str


class FIITypesResponseSchema(APISchema):
    fii_types: List[FIITypeSchema]

