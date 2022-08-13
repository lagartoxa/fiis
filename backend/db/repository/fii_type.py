# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 14:18:42
##############################################################################

from backend.db.models.fii_type import FIIType
from backend.db.repository.base import BaseRepository


class FIITypeRepository(BaseRepository):
    def __init__(self, db_session):
        BaseRepository.__init__(self, db_session, FIIType)

    def create_query(self, **kwargs):
        query = BaseRepository.create_query(self, **kwargs)

        name = kwargs.get("name", None)
        if name:
            query = query.filter(FIIType.name == name)

        return query

