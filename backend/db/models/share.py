# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-06 23:28:42
##############################################################################

from sqlalchemy import (
    Column,
    Float
)

from .database import BaseTable


class Share(BaseTable):
    __tablename__ = "share"

    value = Column(Float, nullable=False)

