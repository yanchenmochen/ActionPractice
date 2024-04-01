# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Filename :main.py
@Description :
@Datetime :2022/11/17 14:25:22
@Author :meizhewei
@email :meizhewei@zhejianglab.com
@desc : main主入口程序，控制所有的router，并且配置程序端口
"""
import os
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from controller import hello

file = Path(__file__)
sys.path.append(str(file.parent.parent))

description = """
    FastBuild is a docker image automatic and rapid construction software.
"""

app = FastAPI(
    title="FastBuild",
    description=description,
    version="0.0.1",
)

origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,  # 设置允许的origins来源
                   allow_credentials=True,
                   allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
                   allow_headers=["*"])  # 允许跨域的headers，可以用来鉴别来源等作用。



@app.get("/api/fast-build/")
async def root():
    return {"message": "Welcome To FastBuild"}



if __name__ == '__main__':
    print("FastBuild 启动ing")
    uvicorn.run(app='main:app', host="0.0.0.0",
                port=int(8888), reload=True, debug=True)
