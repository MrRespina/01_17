from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

sql = 'SELECT c_name,c_price,c_beans FROM COFFEE ORDER BY c_price'

cur = con.cursor()
cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.

# data = cur.fetchall() # fetchall > 결과가 전부 불러와짐.

for n,p,b in cur:
    print(n,p,b)
    print('*'*40)


con.close()
