# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 13:39:42
##############################################################################


from sqlalchemy import false

from backend.db.models import (
    FII,
    FIIShare
)
from backend.db.repository.base import BaseRepository


class FIIShareRepository(BaseRepository):
    def __init__(self, db_session):
        BaseRepository.__init__(self, db_session, FIIShare)

    def create_query(self, **kwargs):
        query = BaseRepository.create_query(self, **kwargs)

        fii_code = kwargs.get("fii_code", None)
        purchase_date = kwargs.get("payment_date", None)

        if fii_code:
            query = query.join(
                FII, 
                self.model.fii_pk == FII.pk)\
            .filter(FII.deleted == false())\
            .filter(FII.code == fii_code)

        if purchase_date:
            query = query.filter(
                self.model.purchase_date == purchase_date)

        return query

