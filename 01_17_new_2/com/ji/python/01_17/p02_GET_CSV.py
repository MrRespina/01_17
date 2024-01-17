'''
Created on 2024. 1. 17.

@author: sdedu
'''
from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

file = open("C:\\Users\\sdedu\\Desktop\\Dev\\prac\\weathers.csv",'w',encoding='UTF-8')

sql = 'SELECT * FROM weathers'

cur = con.cursor()
cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.

for i in cur:
    file.write(f"{i[0]},{i[1]}-{i[2]},{i[3]},{i[4]},{i[5]}\n")
    print(f"{i[1]}-{i[2]} 생성 완료")

file.close()
con.close()
