# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-13 15:40:42
##############################################################################

from sqlalchemy import false

from backend.db.models.fii_dividend import (
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

