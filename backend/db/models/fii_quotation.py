# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 11:47:42
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


class FIIQuotation(BaseTable):
    __tablename__ = "fii_quotation"

    fii_pk = Column(
        BigInteger,
        ForeignKey(
            FII.pk, name="fii_quotation_fii_pk_fk"),
        nullable=False,
        index=True
    )

    quotation_date = Column(DateTime, nullable=False, index=True)
    open_value = Column(Float, nullable=False)
    high_value = Column(Float, nullable=False)
    low_value = Column(Float, nullable=False)
    close_value = Column(Float, nullable=False)
    volume = Column(Integer)

    fii = relationship(FII)

    __table_args__ = (
        UniqueConstraint(
            quotation_date, fii_pk, "rm_timestamp",
            name="fii_quotation_quotation_date_fii_pk_un"
        ),
    )

