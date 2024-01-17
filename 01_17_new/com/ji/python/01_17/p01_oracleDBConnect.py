'''
Created on 2024. 1. 17.

@author: sdedu
'''
from cx_Oracle import connect

# OracleDB와 연동이 되는 Java : instant client에 있는 ojdbc8.jar
# OracleDB와 연동이 되는 Python : cx_oracle.py(instant client를 사용)

# 기본적으로 python에는 oracleDB 연결 기능이 없다.
# cx_oracle.py > ojdbc8.jar를 사용

# pip install cx_oracle
# sqlplus로 접속할 때 사용하는 주소
#    sqlplus [ID]/[PW]@[IP Address]:[PORT]/[SID]
#    sqlplus respina/sdj7524@localhost:1521/xe

try:
    c = connect("respina/sdj7524@localhost:1521/xe")
    print('연결 성공')
except Exception as e:
    print(e)
    
    
c.close()