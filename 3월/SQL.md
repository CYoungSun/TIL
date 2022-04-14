# SQL
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
```
DELETE from classmates where id = 2;
```
### AUTOINCREMENT
CREATE 할떄 설정해주면 된다.

## UPDATE
```
UPDATE 테이블이름 SET 컬럼1=값1, 컬럽2=값2 WHERE 조건;
```

<hr>
[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```



---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql
   select * from users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(age=1,balance=1)
   ```

   ```sql
   -- sql
   insert into users_user values (102,'asd', 'asd', 40,'asd','123213',2);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(id=102)
   ```

   ```sql
   -- sql
   select * from users_user where id=102;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   user = User.objects.get(id=102)
   user.last_name='김'
   user.save()
   ```

      ```sql
   -- sql
      update users_user set first_name='철수' where id=102;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   user.delete()
   ```

   ```sql
   -- sql
   delete from users_user where id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   len(User.objects.all())
   ```

   ```sql
   -- sql
   select count(*) from users_user;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   ```

      ```sql
   -- sql
   select first_name from users_user where age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   len(User.objects.filter(age__gte=30))
   ```

      ```sql
   -- sql
   select count(*) as count  from users_user where age>=30;

      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   len(User.objects.filter(age__lte=20))
   ```

   ```sql
   -- sql
   select count(*) as count  from users_user where age<=20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   len(User.objects.filter(age=30, last_name='김'))
   ```

      ```sql
   -- sql
   select count(*) as count  from users_user where age=30 and last_name='김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   q = Q()
   q.add(Q(age=30), q.OR)
   q.add(Q(last_name='김'), q.OR)
   len(User.objects.filter(q))
   # orm
   ```

   ```sql
   -- sql
   select *   from users_user where age=30 or last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   len(User.objects.filter(phone__startswith='02'))
   ```

      ```sql
   -- sql
   select count(*) from users_user where phone like '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(country='강원도',last_name='황').values('first_name')
   ```

      ```sql
   -- sql
      select * from users_user where country='강원도' and last_name='황';
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

      ```python
   # orm
   User.objects.all().order_by('-age')[:10]
   ```

      ```sql
   -- sql
   select * from users_user order by age desc limit 10;
      ```

2. 잔액이 적은 사람순으로 10명

      ```python
   # orm
   User.objects.all().order_by('balance')[:10]
   ```

      ```sql
   -- sql
   select * from users_user order by balance limit 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   User.objects.all().order_by('balance','-age')[:10]
   ```

   ```sql
   -- sql
   select * from users_user order by balance, age desc limit 10;
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.all().order_by('-last_name','-first_name')[4]
   ```

      ```sql
   -- sql
   select * from users_user order by last_name desc, first_name desc limit 1 offset 4;
      ```



---



### 4. 표현식

#### 4.1 Aggregate

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

      ```python
   # orm
   User.objects.all().aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   select avg(age) as age from users_user;
      ```

2. 김씨의 평균 나이

      ```python
   # orm
   User.objects.all().filter(last_name='김').aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   select avg(age) as age from users_user where last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.all().filter(country='강원도').aggregate(Avg('age'))
   ```

   ```sql
   -- sql
   select avg(age) as age from users_user where country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   User.objects.all().aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   select max(balance) as max from users_user;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   User.objects.all().aggregate(Sum('balance'))
   ```

      ```sql
   -- sql
   select sum(balance) as max from users_user;
      ```



#### 4.2 Annotate

1. 지역별 인원 수

   ```PYTHON
   # orm
   User.objects.values('country').annotate(count=Count('country'))
   ```

   ```SQL
   -- sql
   select country, count(country) as count from users_user group by country;
   ```