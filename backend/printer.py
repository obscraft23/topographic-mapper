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

def testdata(path):

    with open(path, "rb") as f:
        data = f.read()
    
    output = io.BytesIO()

    file_data = data
    b64_data = base64.b64encode(file_data).decode('utf-8')
    bin_data = base64.b64decode(b64_data.encode('utf-8'))
    
    img = Image.open(io.BytesIO(bin_data))
    img_p = img.convert('P')
    img_p.save(output,format="png")
    img_p.save(path.replace(".png",".tt.png"))

    print(len(data))
    print()
    print(len(output.getvalue()))

    return data, b64_data

if (__name__ == "__main__"):

    import sys
    args = sys.argv

    bin_data, b64_data = testdata(args[1])

    files = {
        "file" : ("testdata", b64_data, "text/plain"),
        }
    
    res = requests.post("http://127.0.0.1:8000/api/netprint",files=files)

    """
    authToken, userCode = login()
    
    bin_data, b64_data = testdata(args[1])
    registerName = "testtest.png"

    res = upload(authToken,bin_data,registerName)
    url,dd = checkfile(authToken)
    print(authToken)
    print(userCode)
    print(url)
    """

