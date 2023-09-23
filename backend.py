from pymongo.mongo_client import MongoClient
import json
conp = MongoClient("mongodb+srv://thejatin:jatinkalwar@attacknum.nmuaiq8.mongodb.net/?retryWrites=true&w=majority")
async def returnseckey():
    try:
        pas = conp.attack.sumayaacademy.find_one({"pos": "1001"}, {'seckey': 1, '_id': 0})
        print(pas)
        return pas['seckey']
    except Exception as e:
        return "false"

async def helper(data) -> dict:
    return {
    "id": str(data["_id"]),
    "duration": data["duration"],
    "sr": data["sr"],
        "vurl": data["vurl"],
        "iurl": data["iurl"],
        "title": data["title"],
        "desc": data["desc"],
        "date": data["date"],
    }



async def retall():
    try:
        listt = []
        for x in conp.attack.sumayaacademy.find():
            y = await helper(x)
            listt.append(y.copy())
        listt.reverse()
        return listt
    except Exception as e:
        print(e)
        return "false"


async def getdeviceid(userid):
    pas = conp.SumayaAcademyapk.sastudentinfo.find_one({"userID": str(userid)}, {'deviceid': 1, '_id': 0})
    try:
        return (pas['deviceid'])
    except Exception as e:
        print("Invalid key")


async def userexists(userid):
    try:
        for x in conp.SumayaAcademyapk.sastudentinfo.find():
            if userid==x['userID']:
                return "exists"
        else:
            return "nouserfound"
    except Exception as e:
        pass

async def newdeviceid(userid , deviceid):
    device = conp.SumayaAcademyapk.sastudentinfo.update_one({"userID": userid}, {'$set': {"deviceid": deviceid}})
    cpas = conp.SumayaAcademyapk.sastudentinfo.find_one({"userID": str(userid)}, {'deviceid': 1, '_id': 0})
    if cpas['deviceid']==deviceid:
        return "true"
    else:
        return "failed"

async def getdeviceidall(deviceid):
    for x in conp.SumayaAcademyapk.sastudentinfo.find():
        if deviceid==x['deviceid']:
            return "true"
# async def userloginpass(password):
#     passfetch = conp.SumayaAcademyapk.sastudentinfo.find_one({"userID": str(userid)}, {'password': 1, '_id': 0})
#     try:
#         return passfetch['password']
#     except Exception as e:
#         pass
