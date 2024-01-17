from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

name = input('원두의 이름 입력 : ')

sql = f"SELECT COUNT(*),AVG(c_price) FROM COFFEE WHERE c_beans=\'{name}\'"
print(sql)

cur = con.cursor()
cur.execute(sql)

for c,a in cur:
    print(c,a)

con.close()
