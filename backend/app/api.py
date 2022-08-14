# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-06 22:46:42
##############################################################################

from fastapi import FastAPI

from backend.app.routers import (
    fii,
    fii_type
)


app = FastAPI()
app.include_router(fii.router)
app.include_router(fii_type.router)


@app.get('/')
async def root():
    return {
        "fon": "eoq",
    }

