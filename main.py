from backend import *
from fastapi import FastAPI, Request, BackgroundTasks, UploadFile, File, Form
from fastapi.responses import PlainTextResponse
import requests
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


import json

kalwar = FastAPI()

@kalwar.get("/sumayaacademy/keys")
async def verify():
    ke = await returnseckey()
    return ke


@kalwar.get("/sumayaacademy/data", response_class=PlainTextResponse)
async def verif():
    allin = await retall()
    json_data = json.dumps(allin)
    return json_data

@kalwar.get("/", response_class=HTMLResponse)
async def rootu():
    html_content = """
     <html>
         <head>
             <title>Sumaya Academy</title>
         </head>
         <body>

             <h1>Developed By Jatin Kalwar</h1>
             <br>
             <h3>For Business Query Contact me on  thejatinkalwar@gmail.com</h3>
         </body>
     </html>
     """
    return HTMLResponse(content=html_content, status_code=200)

@kalwar.get("/sumayaacademy/login/", response_class=PlainTextResponse)
async def loginf(userid, password, deviceid):
    checkuser = await  userexists(userid)
    if checkuser == "exists":
        pass
    else:
        return "nouserfound"
    # checkpass = await userloginpass(password)
    if password == "sumaya@123":
        pass
    else:
        return "invalid password"
    deviceidreturn = await getdeviceid(userid)
    dataa = await returndata(userid)
    gi = await getdeviceidall(deviceid)
    if gi == userid:
        json_data = json.dumps(dataa)
        return json_data

    if deviceidreturn == "None" or deviceidreturn == "null":
        gui = await newdeviceid(userid, deviceid)
        if gui == "true":
            json_data = json.dumps(dataa)
            return json_data
    else:
        return "already logged in"

@kalwar.get("/sumayaacademy/addstudent/", response_class=PlainTextResponse)
async def addstu(stuid, name, sem):
    return await insertstu(stuid, sem, name)

@kalwar.get("/sumayaacademy/update/", response_class=PlainTextResponse)
async def loginf( userid ,mobileno , gender):
    dics = await updateinfo(userid , mobileno , gender)
    json_data = json.dumps(dics)
    return json_data

@kalwar.get("/sumayaacademy/checkstatus/", response_class=PlainTextResponse)
async def checkstatuss(userid):
    return await getuserall(userid)

@kalwar.post("/sumayaacademy/")
async def uploadd(assign_id: str = Form(...) , file:UploadFile = File(...) ):

        file_ext = file.filename.split(".").pop()
        file_name = 21045
        file_path = f"{file_name}.{file_ext}"
        print(assign_id)
        with open (file_path , 'wb') as f:
            conent = await file.read();
            f.write(conent)
        return "ok"
