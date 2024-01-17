'''
Created on 2024. 1. 17.

@author: sdedu
'''

from cx_Oracle import connect

con = connect('respina/sdj7524@localhost:1521/xe')

sql = 'SELECT * FROM COFFEE ORDER BY c_id'

cur = con.cursor()

while True:
    
    cur.execute(sql)
    
    print('***** 전체 커피 정보 확인 *****\n')
    print('*'*40)
    
    for i in cur:
        
        print(f"등록번호 : {i[0]}, 이름 : {i[1]}, 가격 : {i[2]}, 원두명 : {i[3]}")
        print('*'*40)
        
    try:
        
        num = int(input('삭제할 데이터의 번호를 입력해주세요 (exit:999) : '))
        print('')
        
        try:
            
            sql2 = f'DELETE FROM COFFEE WHERE c_id={num}'
            
            if(num != 999):
                
                cur.execute(sql2)
                con.commit()
                
                if cur.rowcount == 0:
                    
                    print(f'{num} 번의 데이터가 존재하지 않습니다!\n')
                    
                else:
                    
                    print(f"{num} 번의 데이터를 삭제 완료했습니다.\n")
                    
            else:
                
                print('***** 프로그램 종료 *****')
                break
            
        except Exception as e:
            
            print(e)
            
    except Exception as e:
        
        print(e)
        print('입력은 숫자만 입력해주세요!\n')

con.close()
