# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 15:46:42
##############################################################################

from pydantic import BaseModel
from typing import Optional


class APISchema(BaseModel):
    success: bool
    reason: Optional[str] = None

