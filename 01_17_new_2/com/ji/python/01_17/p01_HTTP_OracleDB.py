from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1150062000
hc = HTTPConnection('www.kma.go.kr') # 서버 주소
hc.request('GET', '/wid/queryDFSRSS.jsp?zone=1150062000') # 요청 파라미터

res = hc.getresponse()
resBody = res.read().decode() 

con = connect('respina/sdj7524@localhost:1521/xe')
cur = con.cursor() 


# 시간대 / 기온 / 최고 기온 / 최저 기온

for i in fromstring(resBody).getiterator('data'):
     
    sql = f"INSERT INTO weathers VALUES(weathers_seq.nextval,{i.find('day').text},{i.find('hour').text},{i.find('temp').text}"
    sql += f",{i.find('tmx').text},{i.find('tmn').text})"
    cur.execute(sql)

    if cur.rowcount == 1: 
        print(f"시간 : {i.find('day').text},{i.find('hour').text}")
        print(f"기온 : { i.find('temp').text}")
        print(f"최고기온 : { i.find('tmx').text}")
        print(f"최저기온 : { i.find('tmn').text}")
        print('*'*20)
        con.commit()  

con.close()