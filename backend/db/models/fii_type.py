# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 13:25:42
##############################################################################

from sqlalchemy import (
    Column,
    Unicode,
    UniqueConstraint
)

from .database import BaseTable


class FIIType(BaseTable):
    __tablename__ = "fii_type"

    name = Column(Unicode(50), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            name, "rm_timestamp",
            name="fii_type_rm_timestamp_un"
        ),
    )

