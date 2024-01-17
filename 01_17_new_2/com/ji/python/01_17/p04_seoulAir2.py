'''
Created on 2024. 1. 17.

@author: sdedu
'''

# DB에 있는 미세먼지 데이터 > CSV 파일에 저장

from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

file = open("C:\\Users\\sdedu\\Desktop\\Dev\\prac\\seoul_air.csv",'w',encoding='UTF-8')

sql = 'SELECT * FROM seoul_air'

cur = con.cursor()
cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.

for i in cur:
    file.write(f"{i[0]},{i[1]},{i[2]}\n")
    print(f"{i[0]} 를 csv에 입력했습니다.")

file.close()
con.close()
