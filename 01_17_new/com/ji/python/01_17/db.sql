CREATE TABLE COFFEE(

	c_id number(4) primary key,
	c_name varchar2(20 char) not null,
	c_price number(7) not null,
	c_beans varchar2(30 char) not null

);

CREATE sequence coffee_seq

SELECT * FROM COFFEE ORDER BY c_price

SELECT AVG(c_price) FROM (SELECT c_name,c_price,c_beans,ROWNUM as rn FROM (SELECT * FROM COFFEE ORDER BY c_price)) WHERE rn BETWEEN 1 AND 2

SELECT ROWNUM as rn,c_price FROM (SELECT c_name,c_price,c_beans FROM COFFEE ORDER BY c_price)

SELECT AVG(c_price) FROM COFFEE WHERE c_id BETWEEN 0 AND 2

UPDATE COFFEE SET c_price = c_price+200 WHERE c_beans='블루마운틴'

DELETE FROM COFFEE WHERE c_id=5

CREATE TABLE weathers(
	w_id number(4) primary key,
	w_day number(3) not null,
	w_hour number(2) not null, 
	w_temp number(3) not null,
	w_max_temp number(3) not null,
	w_min_temp number(3) not null
)
