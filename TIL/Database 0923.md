# Database 0923 

- 이전까지 Django의 ORM으로 DBMS의 데이터를 파이썬 파일 및 구문으로 사용할 수 있었다.
- `sqlite`를 사용 

```
# 버클리 오라클
https://www.oracle.com/kr/database/technologies/related/berkeleydb.html
# 데이터베이스 직접 만들어버리는 강의 
https://www2.eecs.berkeley.edu/Courses/CS186/

```

## 기본용어

```
스키마(schema): 데이터베이스의 구조와 제약 조건(자료의 구조, 표현 방법, 관계)에
관련한 전반적인 명세를 기술한 것.

테이블(table): 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합.
SQL 데이터베이스에서는 테이블을 관계 라고도 한다.

열(Column): 각 열에는 고유한 데이터 형식이 지정됨 
행(row): 테이블의 데이터는 행에 저장된다.즉, user 테이블에 4명의 고객정보가 저장되어 있으며,행은 4개가 존재한다.

PK(기본키): 각 행(레코드)의 고유값으로 Primary Key로 불린다. 반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.
```

### SQL?

```
SQL(Structured Query Language)는 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수
목적의 프로그래밍 언어이다. 관계형 데이터베이스 관리 시스템에서 자료의 검색과 관리 데이터베이스 스키마 생성과 수정, 데이터베이스 객체 접근 조정 관리를 위해 고안되었다.
```

- DDL(데이터 정의 언어)*
- DML(데이터 조작 언어)*
- DCL(데이터 제어 언어)

DDL이랑 DML만 공부할 것 

## sqlite3

```bash
설치 후 database가 있는 디렉토리에서 sqlite3 실행
#<bash.rc로 고친 명령어> <db파일명>
sqlite3 db.sqlite3
# 파일이 없는 상태에서 그냥 sqlite3 해도 실행이 되긴 함 
# 파일이 없을 때 sqlite3 <파일이름>.sqlite3 하면 DB 자동생성해줌 ㅎ  
## 자동생성했을 때 .databases 명령하면 디렉토리에 sqlite3 파일생성 된 것을 확인 가능 

#db 위치
.database

# 테이블 모두 보기
.tables 

# 한글 유니코드 출력하기
bash window창 우클릭 > options > texts > Locale:ko_KR / Character set: UTF-8
```

- 출력

```bash

# <table>에 속한 모든 것 출력 
SELECT * FROM <table>;
# title 출력
SELECT title FROM <table>;
# SELECT <column> FROM <table> LIMIT <num> OFFSET <num>;
# OFFSET num을 띄우고 LIMIT num 만큼 출력 

# 특정 column값이 value인 값들을 가져옴 
$ SELECT * FROM <table> WHERE column=value;
# AND 구문도 사용 가능 
$ SELECT * FROM <table> WHERE column1=value1 AND column2>=40;

# COUNT 및 여러 구문
$ SELECT <구문>(column) FROM <table> WHERE column=value;
$ SELECT COUNT(first_name) FROM users;
$ SELECT AVG(age) FROM users;
$ SELECT MAX(age) FROM users;
$ SELECT MIN(age) FROM users;
$ SELECT AVG(age) FROM users WHERE age>=30;

# LIKE 구문
$ SELECT * FROM table WHERE colun LIKE '';

'2%' : 2로 시작하는 값
'%2' : 2로 끝나는 값
'%2%': 2가 들어가는 값
'_2%' : 두번째가 2로 시작하는 값
'1___': 1로 시작하고 4자리인 값
'2_%_% / 2__%': 2로 시작하고 적어도 3자리인 값 

# ORDER 구문
# 오름차순(default)
$ SELECT columns FROM table ORDER BY column1, column2 ASC;
# 내림차순
$ SELECT columns FROM table ORDER BY column1, column2 DESC;
# 응용
$ SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;


# SET 처럼 중복값없이 출력 :
$ SELECT DISTINCT <column> FROM <table>;
```

- csv 파일 load하기 

```bash
load할 db 실행
$ .mode csv # 꼭 하자! 
$ .import <import할 csv파일>.csv <로드할 테이블>

# import 시 header exclusion 해줘야함 
```

- UI 조작

```bash
# 헤더 표시
$ .headers on

# column 별 표시 
$ .mode column
```

- table 생성 및 삭제

```bash
# 생성 기본형
$ CREATE TABLE table(
	column1 datatype PRIMARY KEY,
	column2 datatype
	.....
);

# classmates 테이블에 2개 column 생성 
$ CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT #마지막 줄 쉼표 없다! 
);

////////////////////////////////////////////////

# 삭제 
$ DROP TABLE <table명>
```

- 테이블 조회 방법 2개
  - `.tables`
  - `schema <table명>` : 스키마 조회 가능 

- DATA 추가(행추가 INSERT) 및 삭제 

```bash
# INSERT 기본형
$ INSERT INTO table (column1, column2, ...)
$ VALUES(value1, value2, ...);

# cf) 현재 테이블에 있는 모든 column Value가 필요한 건 아님. 한 두개 빠져도 그곳만 비우고 나머지 들어감

# 모든 열에 데이터를 넣을 때는 column을 명시할 필요가 없다. 
$ INSERT INTO table VALUES (value1, value2, ...)

////////////////////////////////////////////////
# DELETE 삭제 
$ DELETE FROM table WHERE rowid=?;
# column의 레코드 중 value가 일치하면 삭제
$ DELETE FROM table WHERE column=value;

# 동일 id가 겹치지 않게 하려면, AUTOINCREMENT를 사용해야한다. (Primary KEY column에서)
```

- id는 어디에???

```bash
# SQLite는 따로 Primary Key 속성의 column을 작성하지 않으면 값이 자동으로 증가하는 PK옵션을 가진 rowid column을 정의함. 
$ SELECT rowid, * FROM classmates;

```

- AUTOINCREMENT

```
$ CREATE TABLE table(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);

# INSERT 시 자동으로 id 값 1씩 추가해서 뒤에 추가해준다. 
```

- UPDATE

```
# condition에 해당하는 모든 레코드들의 값을 column=value로 바꾼다. 
$ UPDATE table SET column1=value1, column2=value2, ... WHERE condition;
```

