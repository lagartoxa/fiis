# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import false


class BaseRepository():
    def __init__(self, db_session, model):
        self.db_session = db_session
        self.model = model

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        try:
            self.db_session.commit()
        except IntegrityError as exc:
            self.rollback()
            raise Exception(exc)

    def add(self, obj):
        self.db_session.add(obj)

    def rollback(self):
        self.db_session.rollback()

    def create_query(self, **kwargs):
        pk = kwargs.get("pk", None)
        with_deleted = kwargs.get("with_deleted", False)
        order_by = kwargs.get("order_by", None)

        query = self.db_session.query(self.model)
        if pk:
            query = query.filter(self.model.pk == pk)
        if not with_deleted:
            query = query.filter(self.model.deleted == false())
        if order_by:
            query = query.order_by(order_by)

        return query

    def all(self):
        return self.create_query().all()

    def one_or_none(self, **kwargs):
        return self.create_query(**kwargs).one_or_none()

