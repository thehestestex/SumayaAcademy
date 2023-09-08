from backend import *
from fastapi import FastAPI , Request , BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
import requests
from pytz import timezone
from datetime import datetime
import json
from fastapi.responses import FileResponse

import json
kalwar = FastAPI(docs_url=None , redoc_url=None , openapi_url=None)
@kalwar.get("/sumayaacademy/keys")
async def verify():
    ke = await returnseckey()
    return ke

@kalwar.get("/sumayaacademy/data" ,  response_class=PlainTextResponse)
async def verif():
    allin = await retall()
    print(allin)
    json_data = json.dumps(allin)
    return json_data
