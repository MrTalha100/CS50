import requests
import sys
import _json
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json",+ sys.argv[1])
f=response.json()
for time in f["time"]:
 print(time["rate"])
print(_json.dumps(f))
while True:
    a=input("enter how munch bitcion you want to buy:")
    
    