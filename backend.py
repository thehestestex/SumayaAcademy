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
