from backend import *
from fastapi import FastAPI , Request , BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
import requests
from pytz import timezone
from datetime import datetime
import json
from fastapi.responses import HTMLResponse
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
    json_data = json.dumps(allin)
    return json_data

@kalwar.get("/" ,   response_class=HTMLResponse)
async def rootu():
    html_content = """
     <html>
         <head>
             <title>Sumaya Academy</title>
         </head>
         <body>
         
             <h1>Developed By Jatin Kalwar</h1>
             <br>
             <h3>For Business Query Contact us on  thejatinkalwar@gmail.com</h3>
         </body>
     </html>
     """
    return HTMLResponse(content=html_content, status_code=200)

@kalwar.get("/sumayaacademy/login/" ,  response_class=PlainTextResponse)
async def loginf(userid , password , deviceid):
    checkuser = await  userexists(userid)
    if checkuser=="exists":
        pass
    else:
        return "nouserfound"
    # checkpass = await userloginpass(password)
    if password=="sumaya@123":
        pass
    else:
        return "invalid password"
    deviceidreturn = await getdeviceid(userid)
    gi = await getdeviceidall(deviceid)
    if gi=="true":
        return gi
    if deviceidreturn=="None" or deviceidreturn=="null":
        return await newdeviceid(userid , deviceid)
    else:
        return "already logged in"
