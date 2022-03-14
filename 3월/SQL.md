# 03.14
## SQL 시작
```
sqlite3 tutorial.sqlite3
.database
.mode csv
.import hellodb.csv examples
.tables
.headers on # 속성 보기
.mode column # 이쁘게 보기
.schema classmates
```
## CRUD
```
SELECT * FROM examples;
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
);
DROP TABLE classmates;
INSERT INTO 테이블이름 (컬럼1,컬럼2,...) VALUES (값1,값2,...);
SELECT rowid, * FROM classmates;
DELETE FROM classmates WHERE rowid=5;
```
## SELECT
```
LIMIT # 쿼리에서 반환되는 행 수를 제한 (OFFSET과 같이 사용하기도 함)
DISTINCT # 조회결과에서 중복된 행을 제거
WHERE # 특별한 조건
```
## DELETE
### AUTOINCREMENT
CREATE 할떄 설정해주면 된다.

## UPDATE
```
UPDATE 테이블이름 SET 컬럼1=값1, 컬럽2=값2 WHERE 조건;