# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 11:56:42
##############################################################################

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from .database import BaseTable
from .fii import FII


class FIIShare(BaseTable):
    __tablename__ = "fii_share"

    fii_pk = Column(
        BigInteger,
        ForeignKey(
            FII.pk, name="fii_share_fii_pk_fk"),
        nullable=False,
        index=True
    )

    purchase_date = Column(DateTime, nullable=False, index=True)
    value = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    fii = relationship(FII)

