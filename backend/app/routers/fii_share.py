# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 13:35:42
##############################################################################

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend.db.models.database import db_session
from backend.db.models.fii import FII
from backend.db.models.fii_share import FIIShare

from backend.db.repository.fii import FIIRepository
from backend.db.repository.fii_share import FIIShareRepository

from backend.db.schema.api import APISchema
from backend.db.schema.fii_share import (
    FIIShareCreateSchema,
    FIIShareDeleteSchema,
    FIIShareSchema,
    FIISharesResponseSchema
)


tags = ["FII Share", ]
router = APIRouter(tags=tags)


@router.get(
    "/fii_share/all", tags=tags,
    response_model=FIISharesResponseSchema)
async def get_all_fii_shares(db_session: Session = Depends(db_session)):
    with FIIShareRepository(db_session) as repo:
        fii_shares = []
        for fii_share in repo.all():
            fii_shares.append({
                "pk": fii_share.pk,
                "fii_code": fii_share.fii.code,
                "purchase_date": fii_share.purchase_date,
                "value": fii_share.value,
                "quantity": fii_share.quantity,
            })

    return {
        "success": True,
        "fii_shares": fii_shares,
    }


@router.get(
    "/fii_share/all_from_fii", tags=tags,
    response_model=FIISharesResponseSchema)
async def get_all_share_from_fii(
    fii_code: str, db_session: Session = Depends(db_session)):

    with FIIRepository(db_session) as repo:
        fii = repo.one_or_none(code=fii_code)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII '{fii_code}' not found."
            )

    with FIIShareRepository(db_session) as repo:
        fii_shares = []
        for fii_share in repo.all(fii_code=fii_code):
            fii_shares.append({
                "pk": fii_share.pk,
                "fii_code": fii_share.fii.code,
                "purchase_date": fii_share.purchase_date,
                "value": fii_share.value,
                "quantity": fii_share.quantity,
            })

    return {
        "success": True,
        "fii_shares": fii_shares,
    }


@router.post(
    "/fii_share/create", tags=tags, response_model=APISchema)
async def create_fii_share(
    request: FIIShareCreateSchema, db_session: Session = Depends(db_session)):
    fii_code = request.fii_code

    with FIIRepository(db_session) as repo:
        fii_code = request.fii_code
        fii = repo.one_or_none(code=fii_code)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII '{fii_code}' not found."
            )

    with FIIShareRepository(db_session) as repo:
        fii_share = FIIShare(
            fii=fii,
            purchase_date=request.purchase_date,
            value=request.value,
            quantity=request.quantity
        )

        repo.add(fii_share)
        repo.commit()

    return {
        "success": True,
        "reason": f"Share for FII {fii.code} added successfully.",
    }


@router.delete(
    "/fii_share/delete", tags=tags, response_model=APISchema)
async def delete_fii_share(
    request: FIIShareDeleteSchema, db_session: Session = Depends(db_session)):

    pk = request.pk

    with FIIShareRepository(db_session) as repo:
        fii_share = repo.one_or_none(pk=pk)

        if not fii_share:
            raise HTTPException(
                status_code=404,
                detail=f"FII share with pk = {pk} not found."
            )

        fii_share.deleted = True
        repo.commit()

    return {
        "success": True,
        "reason": f"FII share deleted successfully.",
    }

