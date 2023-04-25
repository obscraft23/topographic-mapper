import requests
import json

base_uri = "https://networkprint.ne.jp/LiteServer/app/"

def login():
    userAgent = "Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/112.0.0.0+Safari/537.36"
    payload = {"userAgent" : userAgent}
    headers = {"User-Agent": userAgent}

    res = requests.post(base_uri+"login",params=payload,headers=headers)
    print(res.content)
    authToken = json.loads(res.content)["authToken"]
    userCode = json.loads(res.content)["userCode"]

    return authToken, userCode

def upload(authToken,bin_data,registerName):
    
    files = {
        "file" : ("test3.png", bin_data, "image/png"),
        }
    
    payload = {
        "authToken" : authToken,
        "registerName" : registerName,
    }

    print(files)
    res = requests.post(base_uri+"upload",params=payload,files=files)
    
    return res

def checkfile(authToken):
    userAgent = "Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/112.0.0.0+Safari/537.36"
    payload = {"authToken" : authToken}
    headers = {"User-Agent": userAgent}

    res = requests.post(base_uri+"files",params=payload,headers=headers)

def testbase64():
    import base64

    with open("/home/yyoshimura/test3.png", "rb") as f:
        data = f.read()

    file_data = data
    b64_data = base64.b64encode(file_data).decode('utf-8')
    bin_data = base64.b64decode(b64_data.encode('utf-8'))

    print(bin_data == data)

    return data