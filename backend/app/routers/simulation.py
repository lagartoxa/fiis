# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-19 10:06:42
##############################################################################

from datetime import datetime
from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session

from backend.db.models.database import db_session
from backend.db.schema.simulation import MonthSimulationSchema
from backend.db.repository.fii import FIIRepository
from backend.db.repository.fii_dividend import FIIDividendRepository


tags = ["Simulation", ]
router = APIRouter(tags=tags)


@router.get(
    "/simulation/next_month", tags=tags, response_model=MonthSimulationSchema)
async def simulate_next_month_dividends(db_session: Session = Depends(db_session)):
    now = datetime.now()
    with FIIRepository(db_session) as fii_repo:
        fiis = fii_repo.all()

        data = []
        total = 0
        with FIIDividendRepository(db_session) as dividend_repo:
            for fii in fiis:
                dividend = dividend_repo.get_month_dividend(
                    fii.code,
                    now.month,
                    now.year
                )

                quantity = fii_repo.get_share_quantity(fii.code)

                data.append({
                    "fii_code": fii.code,
                    "dividends_value": dividend,
                    "shares_quantity": quantity,
                    "fii_total": dividend * quantity,
                })
                total += dividend * quantity

        return {
            "fiis": data,
            "total": total
        }

