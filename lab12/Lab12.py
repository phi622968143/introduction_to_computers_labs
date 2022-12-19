#臺南市政府道路挖掘案件資料
#https://data.gov.tw/dataset/6176

import pymysql
import requests
import json

response = requests.get('https://soa.tainan.gov.tw/Api/Service/Get/5f0e2a89-e7f1-441f-9803-7d78cac8d5bb')

name = json.dumps(response.json())#to string
nd=json.loads(name)#to dict
data=nd["data"]#to key

#資料庫連線設定
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='622968', db='wordpress', charset='utf8')
#建立操作游標
cursor = db.cursor()
 
for i in data:

    sql = "INSERT INTO 臺南市政府道路挖掘案件資料(許可證號,案件編號,工程名稱,工程地點) VALUES ('" +i['AC_NO']+ "','" + i['CASE_ID']+"', '"+i['CONST_NAME']+"', '"+i['LOCATION']+"')"

    try:
      cursor.execute(sql)
      #提交修改
      db.commit()
    except:
      #發生錯誤時停止執行SQL
      db.rollback()
      print('error')

#關閉連線
db.close()
