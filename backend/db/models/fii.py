# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-06 23:28:42
##############################################################################

from sqlalchemy import (
    BigInteger,
    Column,
    Float,
    ForeignKey,
    Unicode,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from .database import BaseTable
from .fii_type import FIIType


class FII(BaseTable):
    __tablename__ = "fii"

    fii_type_pk = Column(
        BigInteger,
        ForeignKey(
            FIIType.pk, name="fii_fii_type_pk_fk"),
        nullable=False,
        index=True
    )

    name = Column(Unicode(100), nullable=False)
    code = Column(Unicode(10), nullable=False)
    value = Column(Float, nullable=False)

    fii_type = relationship(FIIType)

    __table_args__ = (
        UniqueConstraint(
            name, "rm_timestamp",
            name="fii_name_un"
        ),
        UniqueConstraint(
            code, "rm_timestamp",
            name="fii_code_un"
        ),
    )

