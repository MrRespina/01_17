'''
Created on 2024. 1. 17.

@author: sdedu
'''

# 커피 테이블을 활용하여 input으로 숫자 2개 입력
# 가격순(오름차순) 으로 정렬해서
# 숫자 2개 사이에 있는 것들의 평균 가격을 출력

# 

from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

num1 = input('첫 번째 숫자 입력 : ')
num2 = input('두 번째 숫자 입력 : ')

sql = f"SELECT AVG(c_price) FROM (SELECT c_name,c_price,c_beans,ROWNUM as rn FROM (SELECT * FROM COFFEE ORDER BY c_price)) WHERE rn BETWEEN {num1} AND {num2}"

cur = con.cursor()
cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.

p = cur.fetchone()

print(f"{num1} 번째 커피와 {num2} 번째 커피까지의 평균 가격 : {p[0]:.2f}")

con.close()
