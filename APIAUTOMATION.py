import requests
url="http://192.168.0.162:8082/api/LoginApi/GetUserDetails"
params= {"UserName":"AUDITWORK4" ,"PassWord":"Pass@123"}
response=requests.get(url,params=params)
if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Reponse not in JSON")
else:
    print("Response Code ",response.status_code)
    print(f"Response Text: ",{response.text})
    

