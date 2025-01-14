import requests
url="http://192.168.0.162:8084/api/LoginAPI/generatetoken"
params={
"UserName":"Maker1",
"Password":"Pass@1234",
"requestdatetime":"2025-01-14T14:20:00Z"
}
response=requests.get(url,params=params)
if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Reponse not in JSON")
    except requests.exceptions.HTTPError:
        print("HTTP request Error")
else:
    print("Response Code : ",response.status_code)
    print(f"Response Text: ",{response.text})
