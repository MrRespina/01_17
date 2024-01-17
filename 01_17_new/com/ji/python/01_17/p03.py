from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

sql = 'SELECT * FROM COFFEE'

cur = con.cursor()
cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.

for i in cur:
    print(i)
    print('*'*40)


con.close()
