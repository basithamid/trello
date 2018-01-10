import json

def invalidRequestMethod():
    return json.dumps({"status": "failure", "message":{"code":"801", "error":"Invalid Request Method"}})

def badRequest():
    return json.dumps({"status":"failure", "message":{"code":"802", "error":"Invalid Request"}})

def invalidEntries():
    return json.dumps({"status":"failure", "message":{"code":"803", "error":"Invalid Entries"}})

def userExists():
    return json.dumps({"status":"failure", "message":{"code":"804", "error":"User already exists"}})