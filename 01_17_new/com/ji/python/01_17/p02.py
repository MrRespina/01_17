from cx_Oracle import connect

# 1. DB 연결
con = connect('respina/sdj7524@localhost:1521/xe')

# 3. 데이터 입력
n = input('커피 이름 : ')
p = int(input('커피 가격 : '))
b = input('원두 이름 : ')

# 4. sql문 작성
#    Java : ?,?
#    MyBatis : ${멤버변수명}
#    Python : 완성된 sql문 사용.

sql  = "INSERT INTO COFFEE VALUES(coffee_seq.nextval,'%s',%d,'%s')" %(n,p,b)
print(sql)

# 5. DB 관련 작업 (sql문을 서버로 전송, 실행, 결과 받기) : 총괄 객체
#    Java : PreparedStatement (pstmt)
#    Python : cursor()
cur = con.cursor() 

# 6. 수행
cur.execute(sql)

# 7. 결과 처리

if cur.rowcount == 1: # 방금 작업때문에 영향을 받은 행 수가 하나라면
    print('성공')
    con.commit() # DB에 실제로 반영시킴.

con.close()