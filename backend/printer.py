import base64
import io
import json

import requests
from PIL import Image


base_uri = "https://networkprint.ne.jp/LiteServer/app/"

def login():
    userAgent = "Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/112.0.0.0+Safari/537.36"
    payload = {"userAgent" : userAgent}
    headers = {"User-Agent": userAgent}

    res = requests.post(base_uri+"login",params=payload,headers=headers)
    authToken = json.loads(res.content)["authToken"]
    userCode = json.loads(res.content)["userCode"]

    return authToken, userCode

def upload(authToken,bin_data,registerName,max_size=10000000):
    
    if len(bin_data) > max_size:
        output = io.BytesIO()
        img = Image.open(io.BytesIO(bin_data))
        img_p = img.convert('P')
        img_p.save(output,format="png")
        bin_data = output.getvalue()

    files = {
        "file" : ("test3.png", bin_data, "image/png"),
        }
    
    payload = {
        "authToken" : authToken,
        "registerName" : registerName,
    }

    res = requests.post(base_uri+"upload",params=payload,files=files)
    
    return res

def checkfile(authToken):
    userAgent = "Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/112.0.0.0+Safari/537.36"
    payload = {"authToken" : authToken}
    headers = {"User-Agent": userAgent}

    res = requests.post(base_uri+"files",params=payload,headers=headers)

    preview_url = json.loads(res.content)["files"][0]['previewUrls'][0]

    return preview_url, json.loads(res.content)
