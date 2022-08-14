# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-07 14:05:42
##############################################################################

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend.db.models.database import db_session
from backend.db.models.fii import FII

from backend.db.repository.fii import FIIRepository
from backend.db.repository.fii_type import FIITypeRepository

from backend.db.schema.api import APISchema
from backend.db.schema.fii import (
    FIICreateSchema,
    FIIDeleteSchema,
    FIIsResponseSchema
)


tags = ["FII", ]
router = APIRouter(tags=tags)


@router.get("/fii/all", tags=tags, response_model=FIIsResponseSchema)
async def get_all_fiis(db_session: Session = Depends(db_session)):
    with FIIRepository(db_session) as repo:
        fiis = []
        for fii in repo.all():
            fiis.append({
                "pk": fii.pk,
                "name": fii.name,
                "code": fii.code,
                "value": fii.value,
                "fii_type": fii.fii_type.name,
            })

    return {
        "success": True,
        "fiis": fiis,
    }


@router.post("/fii/create", tags=tags, response_model=APISchema)
async def create_fii(
    request: FIICreateSchema, db_session: Session = Depends(db_session)):
    name = request.name
    code = request.code

    with FIITypeRepository(db_session) as repo:
        fii_type_name = request.fii_type
        fii_type = repo.one_or_none(name=fii_type_name)

        if not fii_type:
            raise HTTPException(
                status_code=404,
                detail=f"FII type '{fii_type_name}' not found."
            )

    with FIIRepository(db_session) as repo:
        if repo.one_or_none(name=name):
            raise HTTPException(
                status_code=409,
                detail=f"FII with name = '{name}' already exists."
            )

        if repo.one_or_none(code=code):
            raise HTTPException(
                status_code=409,
                detail=f"FII with code = '{code}' already exists."
            )

        fii = FII(
            name=request.name,
            code=request.code,
            value=request.value,
            fii_type=fii_type
        )

        repo.add(fii)
        repo.commit()

    return {
        "success": True,
        "reason": f"FII {fii.name} inserted successfully.",
    }


@router.delete("/fii/delete", tags=tags, response_model=APISchema)
async def delete_fii(
    request: FIIDeleteSchema, db_session: Session = Depends(db_session)):

    pk = request.pk
    name = request.name
    code = request.code

    if not pk and not name and not code:
        raise HTTPException(
            status_code=400,
            detail="You must provide the pk, name and/or code."
        )

    with FIIRepository(db_session) as repo:
        filters = {}
        if pk:
            filters["pk"] = pk
        if name:
            filters["name"] = name
        if code:
            filters["code"] = code

        fii = repo.one_or_none(**filters)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII not found."
            )

        fii.deleted = True
        repo.commit()

    return {
        "success": True,
        "reason": f"FII '{fii.name}' deleted successfully.",
    }

