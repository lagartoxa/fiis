# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-13 15:40:42
##############################################################################

from backend.db.models.fii import FII
from backend.db.repository.base import BaseRepository
from backend.db.repository.fii_share import FIIShareRepository


class FIIRepository(BaseRepository):
    def __init__(self, db_session):
        BaseRepository.__init__(self, db_session, FII)

    def create_query(self, **kwargs):
        query = BaseRepository.create_query(self, **kwargs)

        name = kwargs.get("name", None)
        code = kwargs.get("code", None)
        code_international = kwargs.get("code_international", None)

        if name:
            query = query.filter(self.model.name == name)

        if code:
            query = query.filter(self.model.code == code)

        if code_international:
            query = query.filter(self.model.code_international == code_international)

        return query

    def get_share_quantity(self, fii_code: str):
        with FIIShareRepository(self.db_session) as share_repo:
            shares = share_repo.all(fii_code=fii_code)

            count = 0
            for share in shares:
                count += share.quantity

        return count

