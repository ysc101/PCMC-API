from PCMC_Token import bearer_token
import requests

url="http://192.168.0.162:8084/api/ECSUploadAPI/ECSPush"

headers={ "Authorization": f"Bearer {bearer_token}"}

payload={
  "formdata": {
    "ecsdate": "2025-01-14T14:45:27.840Z",
    "ecsnumber": 1149,
    "chequenumber": 55296,
    "chequeDate": "2025-01-10T01:15:27.840Z",
    "chequeamount": 4000,
    "debitaccountnumber": "60507106878",
    "remark": "Checking API Entry",
    "ecstransactioncount": 4,
    "ecsamount": 4000
  },
  "paymentdate": [
    {
      "recordidentifier": "",
      "paymentvaluedate": "2024-11-04T01:15:27.840Z",
      "partycode": "IFT",
      "debitaccountno": "60507106878",
      "beneficiaryname": "RUCTION",
      "instrumentamount": 1000,
      "beneficiarybankifsccode": "HDFCo000437",
      "beneficiaryaccountno": "59201715761070",
      "accounttype": "IFT",
      "enrichment1": "2356",
      "enrichment2": "501",
      "enrichment3": "ABC512501",
      "enrichment4": "20562",
      "enrichment5": "Water Tax",
      "remarks1": "Pcmc_16194",
      "remarks2": "-"
    },
    {
      "recordidentifier": "",
      "paymentvaluedate": "2024-11-04T01:15:27.840Z",
      "partycode": "IFT",
      "debitaccountno": "60507106878",
      "beneficiaryname": "PA KRUSHNAJI BHO",
      "instrumentamount": 1000,
      "beneficiarybankifsccode": "BARB0CHINCH",
      "beneficiaryaccountno": "31060100017815",
      "accounttype": "IFT",
      "enrichment1": "2357",
      "enrichment2": "502",
      "enrichment3": "ABC512502",
      "enrichment4": "20562",
      "enrichment5": "Nalla",
      "remarks1": "Pcmc_SALARY_Month_10_2024",
      "remarks2": "-"
    },
    {
      "recordidentifier": "",
      "paymentvaluedate": "2024-11-04T01:15:27.840Z",
      "partycode": "NEFT",
      "debitaccountno": "60507106878",
      "beneficiaryname": "SHIJI NARAYAN SUR",
      "instrumentamount": 1000,
      "beneficiarybankifsccode": "IBKL0000087",
      "beneficiaryaccountno": "087104000169585",
      "accounttype": "NEFT",
      "enrichment1": "2358",
      "enrichment2": "503",
      "enrichment3": "ABC512503",
      "enrichment4": "20562",
      "enrichment5": "Street Lights",
      "remarks1": "Pcmc_SALARY_Month_10_2024",
      "remarks2": "-"
    },
    {
      "recordidentifier": "",
      "paymentvaluedate": "2024-11-04T01:15:27.840Z",
      "partycode": "IFT",
      "debitaccountno": "60507106878",
      "beneficiaryname": "DEAK JAIPRAKASH B",
      "instrumentamount": 1000,
      "beneficiarybankifsccode": "BARB0CHINCH",
      "beneficiaryaccountno": "31060100020503",
      "accounttype": "IFT",
      "enrichment1": "2359",
      "enrichment2": "504",
      "enrichment3": "ABC512504",
      "enrichment4": "20562",
      "enrichment5": "Road Divider",
      "remarks1": "Pcmc_SALARY_Month_10_2024",
      "remarks2": "-"
    }
  ]
}
response=requests.post(url,headers=headers,json=payload)
if response.status_code==200:
    try:
        data=response.json()
        print("Response Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Response not in JSON")
    except requests.exceptions.HTTPError:
        print("HTTP Request not found")
else:
    print("Response Code: ",response.status_code)
    print(response.text)
