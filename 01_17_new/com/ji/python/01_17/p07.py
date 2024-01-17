'''
Created on 2024. 1. 17.

@author: sdedu
'''

from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

val1 = input('인상할 원두 이름 검색 : ')

try:
    val2 = int(input('인상할 가격 입력 : '))
    
    if(val2 < 0):
        vals = -val2
        sql = f"UPDATE COFFEE SET c_price = c_price-{vals} WHERE c_beans='{val1}'"
    else:
        sql = f"UPDATE COFFEE SET c_price = c_price+{val2} WHERE c_beans='{val1}'"
    cur = con.cursor()
    cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.\
    print(f"{val1} 원두를 사용하는 커피들의 가격을\n{val2}원 만큼 변경했습니다.")
    con.commit()
    
except Exception as e:
    print(e)
    print('가격은 정수만 입력해주세요!\nex) 100 or -100')
        
con.close()
