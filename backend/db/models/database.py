# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-06 23:28:42
##############################################################################

from sqlalchemy import (
    BigInteger,
    Column,
    create_engine
)
from sqlalchemy.ext.hybrid import Comparator
from sqlalchemy.sql.elements import True_

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker

import time


SQLALCHEMY_DATABASE_URL = "postgresql://project:project@localhost/fiis"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_session():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


class DeletedComparator(Comparator):
    def __eq__(self, other):
        right = True if isinstance(other, True_) else False

        if right:
            return self.__clause_element__() != 0
        return self.__clause_element__() == 0


class BaseTable(Base):
    __abstract__ = True

    pk = Column(BigInteger, primary_key=True, index=True)
    rm_timestamp = Column(BigInteger, nullable=False, server_default='0')

    @hybrid_property
    def deleted(self):
        return self.rm_timestamp != 0

    @deleted.setter
    def deleted(self, value):
        self.rm_timestamp = int(time.time() * 1000) if value else 0

    @deleted.expression
    def deleted(cls):
        return cls.rm_timestamp != 0

    @deleted.comparator
    def deleted(cls):
        return DeletedComparator(cls.rm_timestamp)

