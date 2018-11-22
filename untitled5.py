import requests
import os
import json
import base64
#获取tokent
baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
grant_type = "client_credentials"
#API Key
client_id = "2ek0ojqkKUN2WGU3jjGkvCbd"   #使用自己的id
#Secret Key
client_secret = "MtTnyGYWgC6RR0YRrtGK4so72UwYbfT4"   #使用自己的secret 下同

#拼url
url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(baidu_server,grant_type,client_id,client_secret)
#获取token
res = requests.post(url)
token = json.loads(res.text)["access_token"]
#设置格式
RATE = "16000"
FORMAT = "wav"
CUID="864131036184396864131036366050"
DEV_PID="1536"

#以字节格式读取文件之后进行编码
with open(r'f:\respon.wav', "rb") as f:
    speech = base64.b64encode(f.read()).decode('utf8')
size = os.path.getsize(r'f:\respon.wav')
headers = { 'Content-Type' : 'application/json'} 
url = "https://vop.baidu.com/server_api"
data={

        "format":FORMAT,
        "rate":RATE,
        "dev_pid":DEV_PID,
        "speech":speech,
        "cuid":CUID,
        "len":size,
        "channel":1,
        "token":token,
    }

req = requests.post(url,json.dumps(data),headers)
result = json.loads(req.text)
print(result["result"][0])
