# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-13 15:40:42
##############################################################################

import calendar
from sqlalchemy import false

from backend.db.models import (
    FII,
    FIIDividend
)
from backend.db.repository.base import BaseRepository


class FIIDividendRepository(BaseRepository):
    def __init__(self, db_session):
        BaseRepository.__init__(self, db_session, FIIDividend)

    def create_query(self, **kwargs):
        query = BaseRepository.create_query(self, **kwargs)

        fii_code = kwargs.get("fii_code", None)
        base_date = kwargs.get("base_date", None)
        payment_date = kwargs.get("payment_date", None)

        if fii_code:
            query = query.join(
                FII, 
                self.model.fii_pk == FII.pk)\
            .filter(FII.deleted == false())\
            .filter(FII.code == fii_code)

        if base_date:
            query = query.filter(
                self.model.base_date == base_date)

        if payment_date:
            query = query.filter(
                self.model.payment_date == payment_date)

        return query

    def get_month_dividend(self, fii_code: str, month: int, year: int):
        last_day_of_month = calendar.monthrange(year, month)[1]
        month = str(month) if month > 9 else f"0{str(month)}"

        dividends = self.create_query(fii_code=fii_code)\
            .filter(
                FIIDividend.payment_date > f"{month}/01/{year}")\
            .filter(
                FIIDividend.payment_date < f"{month}/{last_day_of_month}/{year}"
            ).all()

        total = 0
        for dividend in dividends:
            total += dividend.value

        return total

