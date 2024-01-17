'''
Created on 2024. 1. 17.

@author: sdedu
'''
# openAPI.seoul.go.kr:8088
# 42008a8c8e7402a3fc9d3b1a7df8fee9
# /4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/

# 구 이름, 미세먼지, 초미세먼지의 정보를 DB에 담기. (여러 기간에 걸쳐 이 데이터를 모은다고 가정.)

from http.client import HTTPConnection
from json import loads
from cx_Oracle import connect

# http://openAPI.seoul.go.kr:8088/(인증키)/xml/RealtimeCityAir/1/5/
url = 'openAPI.seoul.go.kr:8088'
query = '/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/'

hc = HTTPConnection(url)
hc.request('GET',query)

res = hc.getresponse() # 응답
resBody = res.read().decode('utf-8')
dates = loads(resBody)

con = connect('respina/sdj7524@localhost:1521/xe')
cur = con.cursor() 

# dates['RealtimeCityAir']['row'][0]
for i in dates['RealtimeCityAir']['row']:         
     
    year = f"{i['MSRDT'][:4]}"
    month = f"{i['MSRDT'][4:6]}"
    day = f"{i['MSRDT'][6:8]}"
    hour = f"{i['MSRDT'][8:10]}"
    minute = f"{i['MSRDT'][10:12]}"
    locale = f"{year}/{month}/{day}/{hour}/{minute}"
    pm10,pm25 = i['PM10'],i['PM25']  
    
    try:         
        sql = f"INSERT INTO seoul_air VALUES(\'{locale}-{i['MSRRGN_NM']}-{i['MSRSTE_NM']}\',{pm10},{pm25})"
        cur.execute(sql)

        if cur.rowcount == 1: 
            print(f"장소 : {locale}-{i['MSRRGN_NM']}-{i['MSRSTE_NM']}")
            print(f"미세먼지 : {pm10}")
            print(f"초미세먼지 : {pm25}")
            print('*'*30)
            con.commit()  
        
    except Exception as e:
        print(f"{locale}-{i['MSRRGN_NM']}-{i['MSRSTE_NM']} 은 이미 존재하는 데이터입니다!")

con.close()