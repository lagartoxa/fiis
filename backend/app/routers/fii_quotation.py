# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-14 13:39:42
##############################################################################

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend.db.models.database import db_session
from backend.db.models.fii import FII
from backend.db.models.fii_quotation import FIIQuotation

from backend.db.repository.fii import FIIRepository
from backend.db.repository.fii_quotation import FIIQuotationRepository

from backend.db.schema.api import APISchema
from backend.db.schema.fii_quotation import (
    FIIQuotationCreateSchema,
    FIIQuotationDeleteSchema,
    FIIQuotationSchema,
    FIIQuotationsResponseSchema
)


tags = ["FII Quotation", ]
router = APIRouter(tags=tags)


@router.get(
    "/fii_quotation/all", tags=tags,
    response_model=FIIQuotationsResponseSchema)
async def get_all_fii_quotations(db_session: Session = Depends(db_session)):
    with FIIQuotationRepository(db_session) as repo:
        fii_quotations = []
        for fii_quotation in repo.all():
            fii_quotations.append({
                "pk": fii_quotation.pk,
                "fii_code": fii_quotation.fii.code,
                "quotation_date": fii_quotation.quotation_date,
                "open_value": fii_quotation.open_value,
                "high_value": fii_quotation.high_value,
                "low_value": fii_quotation.low_value,
                "close_value": fii_quotation.close_value,
                "volume": fii_quotation.volume,
            })

    return {
        "success": True,
        "fii_quotations": fii_quotations,
    }


@router.get(
    "/fii_quotation/all_from_fii", tags=tags,
    response_model=FIIQuotationsResponseSchema)
async def get_all_quotation_from_fii(
    fii_code: str, db_session: Session = Depends(db_session)):

    with FIIRepository(db_session) as repo:
        fii = repo.one_or_none(code=fii_code)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII '{fii_code}' not found."
            )

    with FIIQuotationRepository(db_session) as repo:
        fii_quotations = []
        for fii_quotation in repo.all(fii_code=fii_code):
            fii_quotations.append({
                "pk": fii_quotation.pk,
                "fii_code": fii_quotation.fii.code,
                "quotation_date": fii_quotation.quotation_date,
                "open_value": fii_quotation.open_value,
                "high_value": fii_quotation.high_value,
                "low_value": fii_quotation.low_value,
                "close_value": fii_quotation.close_value,
                "volume": fii_quotation.volume,
            })

    return {
        "success": True,
        "fii_quotations": fii_quotations,
    }


@router.post(
    "/fii_quotation/create", tags=tags, response_model=APISchema)
async def create_fii_quotation(
    request: FIIQuotationCreateSchema, db_session: Session = Depends(db_session)):
    fii_code = request.fii_code
    quotation_date = request.quotation_date

    with FIIRepository(db_session) as repo:
        fii_code = request.fii_code
        fii = repo.one_or_none(code=fii_code)

        if not fii:
            raise HTTPException(
                status_code=404,
                detail=f"FII '{fii_code}' not found."
            )

    with FIIQuotationRepository(db_session) as repo:
        if repo.one_or_none(fii_code=fii_code, quotation_date=quotation_date):
            raise HTTPException(
                status_code=409,
                detail=f"There is already a quotation for the FII '{fii.code}' "
                f"at '{quotation_date}'"
            )
        fii_quotation = FIIQuotation(
            fii=fii,
            quotation_date=quotation_date,
            open_value=request.open_value,
            high_value=request.high_value,
            low_value=request.low_value,
            close_value=request.close_value,
            volume=request.volume,
        )

        repo.add(fii_quotation)
        repo.commit()

    return {
        "success": True,
        "reason": f"Quotation for FII {fii.code} added successfully.",
    }


@router.delete(
    "/fii_quotation/delete", tags=tags, response_model=APISchema)
async def delete_fii_quotation(
    request: FIIQuotationDeleteSchema, db_session: Session = Depends(db_session)):

    pk = request.pk

    with FIIQuotationRepository(db_session) as repo:
        fii_quotation = repo.one_or_none(pk=pk)

        if not fii_quotation:
            raise HTTPException(
                status_code=404,
                detail=f"FII quotation with pk = {pk} not found."
            )

        fii_quotation.deleted = True
        repo.commit()

    return {
        "success": True,
        "reason": f"FII quotation deleted successfully.",
    }

