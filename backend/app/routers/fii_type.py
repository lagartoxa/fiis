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
from backend.db.models.fii_type import FIIType

from backend.db.repository.fii_type import FIITypeRepository

from backend.db.schema.api import APISchema
from backend.db.schema.fii_type import (
    FIITypesResponseSchema,
    FIITypeSchema
)


tags = ["fii", ]
router = APIRouter(tags=tags)


@router.get("/fii_type/all", tags=tags, response_model=FIITypesResponseSchema)
async def get_all_fii_types(db_session: Session = Depends(db_session)):
    with FIITypeRepository(db_session) as repo:
        fii_types = []
        for fii_type in repo.all():
            fii_types.append({
                "name": fii_type.name
            })

    return {
        "success": True,
        "fii_types": fii_types,
    }


@router.post("/fii_type/create", tags=tags, response_model=APISchema)
async def create_fii_type(
    request: FIITypeSchema, db_session: Session = Depends(db_session)):

    with FIITypeRepository(db_session) as repo:
        fii_type = FIIType(name=request.name)
        repo.add(fii_type)
        repo.commit()

    return {
        "success": True,
        "reason": f"FII type {fii_type.name} inserted successfully",
    }


@router.delete("/fii_type/delete", tags=tags, response_model=APISchema)
async def delete_fii_type(
    request: FIITypeSchema, db_session: Session = Depends(db_session)):

    name = request.name

    with FIITypeRepository(db_session) as repo:
        fii_type = repo.one_or_none(name=name)

        if not fii_type:
            raise HTTPException(status_code=404, detail=f"Fii type '{name}' not found.")

        fii_type.deleted = True
        repo.commit()

    return {
        "success": True,
        "reason": f"Fii type '{name}' deleted successfully",
    }

