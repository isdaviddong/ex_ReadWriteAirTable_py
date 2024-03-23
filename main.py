import requests
import json

ID="👉ID"
Table="👉Table"
PAT="👉PAT"

# 你的個人存取令牌和基礎數據庫 ID
api_url =  f"https://api.airtable.com/v0/{ID}/{Table}"

headers = {
    "Authorization": f"Bearer {PAT}",
    "Content-Type": "application/json"
}

# 新增資料
def add_data(field1, value1, field2, value2):
    data = {
        "fields": {
            field1: value1,
            field2: value2
        }
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("資料新增成功")
    else:
        print("資料新增失敗:", response.text)


# 搜尋資料
def search_record(field, value):
    params = {
        "filterByFormula": "{請假人} = '值1'"
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        records = response.json().get("records")
        if records:
            # 顯示有幾筆資料
            print(f"共有{len(records)}筆資料")
            # 顯示每一筆資料
            for record in records:
                print(record)
        else:
            print("找不到資料")
    else:    
        print("資料查詢失敗:", response.text)
        print("response.status_code:", response.status_code)
        
        return None
    
# 主程式
# 跑一個迴圈
for i in range(1, 2):
    field1 = "請假人"
    value1 = "值" + str(i)
    field2 = "代理人"
    value2 = "值" + str(i+1)
    add_data(field1, value1, field2, value2)    

# 搜尋資料
search_record("請假人", "值1")    