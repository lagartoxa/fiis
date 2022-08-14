# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-13 15:40:42
##############################################################################

from backend.db.models.fii import FII
from backend.db.repository.base import BaseRepository


class FIIRepository(BaseRepository):
    def __init__(self, db_session):
        BaseRepository.__init__(self, db_session, FII)

    def create_query(self, **kwargs):
        query = BaseRepository.create_query(self, **kwargs)

        name = kwargs.get("name", None)
        code = kwargs.get("code", None)

        if name:
            query = query.filter(FII.name == name)

        if code:
            query = query.filter(FII.code == code)

        return query

