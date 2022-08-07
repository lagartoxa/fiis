# -*- coding: utf-8 -*-

##############################################################################
# @Author: Ildomar Carvalho
# @Email:  ildomarcarvalho@gmail.com
# @Date:   2022-08-06 22:46:42
##############################################################################

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {
        "fon": "eoq",
    }

