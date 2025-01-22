import requests

from MyToken import bearer_token

url="http://192.168.0.162:8084/api/PayeeDetailsAPI/updatedpayeedata"
headers={"Authorization":f"Brearer {bearer_token}"}
payload={
  "ecsdate": "2025-01-16T07:08:36.271Z",
  "ecsnumber":996633,
  "beneficiaryname": "MYPARTYNAME",
  "beneficiarybankifsccode": "MAHB0000024",
  "beneficiaryaccountno": "112239632145678",
  "uniquepartykey": "POL123456"
}
response=requests.post(url,headers=headers,json=payload)
if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Response not in JSON")
    except requests.exceptions.HTTPError:
        print("Request not send")
    else:
        print("Response Code ",response.status_code)
        print(f"Response Text: {response.text}")
