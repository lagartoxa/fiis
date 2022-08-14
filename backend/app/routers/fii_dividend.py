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
from backend.db.models.fii_dividend import FIIDividend

from backend.db.repository.fii import FIIRepository
from backend.db.repository.fii_dividend import FIIDividendRepository

from backend.db.schema.api import APISchema
from backend.db.schema.fii_dividend import (
    FIIDividendCreateSchema,
    FIIDividendDeleteSchema,
    FIIDividendSchema,
    FIIDividendsResponseSchema
)


tags = ["FII Dividend", ]
router = APIRouter(tags=tags)


@router.get(
    "/fii_dividend/all", tags=tags,
    response_model=FIIDividendsResponseSchema)
async def get_all_fii_dividends(db_session: Session = Depends(db_session)):
    with FIIDividendRepository(db_session) as repo:
        fii_dividends = []
        for fii_dividend in repo.all():
            fii_dividends.append({
                "pk": fii_dividend.pk,
                "fii_code": fii_dividend.fii.code,
                "base_date": fii_dividend.base_date,
                "payment_date": fii_dividend.payment_date,
                "base_quotation": fii_dividend.base_quotation,
                "dividend_yield": fii_dividend.dividend_yield,
                "value": fii_dividend.value,
            })

    return {
        "success": True,
        "fii_dividends": fii_dividends,
    }


@router.get(
    "/fii_dividend/all_from_fii", tags=tags,
    response_model=FIIDividendsResponseSchema)
async def get_all_dividends_from_fii(
    fii_code: str, db_session: Session = Depends(db_session)):

    with FIIRepository(db_session) as repo:
        fii = repo.one_or_none(code=fii_code)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII '{fii_code}' not found."
            )

    with FIIDividendRepository(db_session) as repo:
        fii_dividends = []
        for fii_dividend in repo.all(fii_code=fii_code):
            fii_dividends.append({
                "pk": fii_dividend.pk,
                "fii_code": fii_dividend.fii.code,
                "base_date": fii_dividend.base_date,
                "payment_date": fii_dividend.payment_date,
                "base_quotation": fii_dividend.base_quotation,
                "dividend_yield": fii_dividend.dividend_yield,
                "value": fii_dividend.value,
            })

    return {
        "success": True,
        "fii_dividends": fii_dividends,
    }


@router.post(
    "/fii_dividend/create", tags=tags, response_model=APISchema)
async def create_fii_dividend(
    request: FIIDividendCreateSchema, db_session: Session = Depends(db_session)):
    fii_code = request.fii_code
    base_date = request.base_date
    payment_date = request.payment_date

    with FIIRepository(db_session) as repo:
        fii_code = request.fii_code
        fii = repo.one_or_none(code=fii_code)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII '{fii_code}' not found."
            )

    with FIIDividendRepository(db_session) as repo:
        if repo.one_or_none(fii_code=fii_code, base_date=base_date):
            raise HTTPException(
                status_code=409,
                detail=
                f"Dividend with base_date '{base_date}' for "
                f"FII with code '{fii_code}' was already registered."
            )

        if repo.one_or_none(
                fii_code=fii_code, payment_date=payment_date):

            raise HTTPException(
                status_code=409,
                detail=
                f"Dividend with payment_date '{payment_date}' for "
                f"FII with code '{fii_code}' was already registered."
            )

        fii_dividend = FIIDividend(
            fii=fii,
            base_date=base_date,
            payment_date=payment_date,
            base_quotation=request.base_quotation,
            dividend_yield=request.dividend_yield,
            value=request.value
        )

        repo.add(fii_dividend)
        repo.commit()

    return {
        "success": True,
        "reason": f"Dividend for FII {fii.code} added successfully.",
    }


@router.delete(
    "/fii_dividend/delete", tags=tags, response_model=APISchema)
async def delete_fii_dividend(
    request: FIIDividendDeleteSchema, db_session: Session = Depends(db_session)):

    pk = request.pk

    with FIIDividendRepository(db_session) as repo:
        fii_dividend = repo.one_or_none(pk=pk)

        if not fii_dividend:
            raise HTTPException(
                status_code=404,
                detail=f"FII dividend with pk = {pk} not found."
            )

        fii_dividend.deleted = True
        repo.commit()

    return {
        "success": True,
        "reason": f"FII dividend deleted successfully.",
    }

