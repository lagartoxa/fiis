# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 13:30:42
##############################################################################

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from .database import BaseTable
from .fii import FII


class FIIDividend(BaseTable):
    __tablename__ = "fii_dividend"

    fii_pk = Column(
        BigInteger,
        ForeignKey(
            FII.pk, name="fii_dividend_fii_pk_fk"),
        nullable=False,
        index=True
    )

    base_date = Column(DateTime, nullable=False, index=True)
    payment_date = Column(DateTime, nullable=False, index=True)
    base_quotation = Column(Float, nullable=False)
    dividend_yield = Column(Float, nullable=False)
    value = Column(Float, nullable=False)

    fii = relationship(FII)

    __table_args__ = (
        UniqueConstraint(
            base_date, fii_pk, "rm_timestamp",
            name="fii_dividend_base_date_fii_pk_un"
        ),
        UniqueConstraint(
            payment_date, fii_pk, "rm_timestamp",
            name="fii_dividend_payment_date_fii_pk_un"
        ),
    )

