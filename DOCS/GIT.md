# GIT

## GIT (!= github)

- Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

- VCS (Version Control System)

- Git branching GUI Study: https://learngitbranching.js.org/
- https://git-scm.com/docs?source=post_page-----c25b421ecdbd----------------------

### git workflow

```
1. working tree에서 작업(코드작성)
2. staging area로 add
3. local repository로 commit
4. remote repository가 있다면 push
```

![views](https://wayhome25.github.io/assets/post-img/git/git.png)

![views](https://wayhome25.github.io/assets/post-img/git/git2.png)

## Dictionary : 용어 모음

- `저장소 (Repositary)`: 작업자가 변경한 모든 내용을 추적하는 공간
- `작업 트리 (Working Tree)` : 저장소를 어느 한 시점을 바라보는 작업자의 현재 시점이다.
- `master`: 생성/복사한 원격 저장소 HEAD의 지역 브랜치
- `origin`: git이 복사해 온 저장소를 가리키기 위해 사용하는 default 이름

## Git setting

- `git log`용 graph alias 세팅

```
$ git config --global alias.lg "log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold red)%h%C(reset) : %C(bold green)(%ar)%C(reset) - %C(cyan)<%an>%C(reset)%C(bold yellow)%d%C(reset)%n%n%w(90,1,2)%C(white)%B%C(reset)%n'"
```

- `git lg` 입력 시 커밋이력을 그래프 형태로 이쁘게 보여준다.

## Basic Control : 명령어 모음

### 1.설정

#### -`init`

```bash
# git initiation, Git start
$ git init <path>
```

#### -`config`

```bash
# USER 설정을 하지 않으면 commit후 remote push해도 user가 ?로 나타나고 commit count도 변하지 않는다...

# 전역 사용자명/이메일 구성하기
$ git config --global user.name “<name>”
$ git config --global user.email “<email>”

# 저장소별 사용자명/이메일 구성
$ git config user.name “<name>”
$ git config user.email “<email>”
```

#### -`status`

```bash
# git 저장소 상태 목록 (working tree, staging area, 변경사항)
$ git status
```

### 2. 로그 확인

#### - `log`

```bash
# 모든 커밋 이력보기
$ git log

# n개의 커밋 이력 확인
$ git log -n

# 변경사항 보여주는 패치와 함께 커밋 이력 표시
$ git log -p

# 기간/시간 내의 커밋 로그만 확인
$ git log --since "< time >"

# 기간/시간 이전의 커밋 로그 확인
$ git log --before "< time >"
				   # "1 month"
				   # "5 hours"
				   # "5 days"

# 두 지점 사이의 커밋 로그 확인: 커밋명, 브랜치명 태그명 등 사용가능
$ git log <start> ... <end>

# 각 항목의 로그 한줄씩 출력
$ git log --pretty=oneline

# 로그에서 복사와 붙여 넣은 정보 보기
git log -C -C -p -1 <특정 지점>
```

#### - `diff`

```bash
# 현재 작업 트리와 인덱스의 차이점 확인
$ git diff

# 인덱스와 저장소의 차이점 확인
$ git diff --cached

# 작업트리와 저장소의 차이점 확인
$ git diff HEAD

# 두 지점 사이의 차이점 확인
$ git diff <start> end
```

#### - `blame`

```bash
# 파일 커밋정보 줄 단위로 확인
$ git blame <file>

# 파일의 줄 단위의 복사, 붙여 넣기, 이동 정보 보기
$ git blame -M <파일>

# 파일의 줄 단위의 이동과 원본 파일 정보 보기
$ git blame -C -C <파일>
```

### 3. 커밋 & 브랜치 조작

#### - `add`

```bash
# 새로운 파일 추가 / 존재하는 파일 스테이징
$ git add <file>

# 파일의 일부만 스테이징
$ git add -p [<file>[<file>[<file> ... ]]]

# Git 대화모드를 사용하여 파일 추가
$ git add -i

# 수정 및 추적되는 파일의 변경사항 스테이징
$ git add -u [<path>[<path>]]
```

#### - `commit`

```bash
# 스테이징된 파일 커밋
$ git commit -m "<message>"

# 수정 및 추적되는 모든 파일의 변경 사항 커밋
$ git commit -m "<message>" -a

# 마지막 커밋 수정
$ git commit -m "<message>" --amend

# 이전 커밋을 수정하고 커밋 메세지를 재사용하기
$ git commit -C HEAD --amend
```

#### - `checkout`

```bash
# 작업트리의 변경사항 되돌리기(이전 커밋으로 돌아가기)
$ git checkout HEAD <file> [<file>]

# 다른 브랜치로 체크아웃(이동)
$ git checkout <branch>

# 브랜치를 옮기거나 브랜치명 변경하기
$ git checkout -m <branch> <new branch>
				or
$ git checkout -M <branch> <new branch>
```

#### - `cherry-pick`

```bash
# 특정 커밋 선택하여 합치기
$ git cherry-pick <commit>

# 커밋하지 않고 선택하여 합치기
$ git cherry-pick -n <commit>
```

#### - `merge`

```bash
# 현재 브랜치에서 다른 브랜치와의 diff를 확인하고 합친다.
$ git checkout <끌어올 브랜치>
$ git merge <따라갈 브랜치>
$ git push

# 커밋하지 않고 합치기
$ git merge --no-commit <branch>

# 브랜치의 이력을 다른 브랜치에 합치기
$ git merge --squash <branch>
```

#### - `reset`

```bash
# 커밋되지 않고 스테이징된 변경사항 재설정
$ git reset HEAD <file> [<file>]
```

#### - `branch`

```bash
# 현재 branch 상황 확인
$ git branch

# 원격 브랜치 목록 보기
$ git branch -r

# 지역과 원격을 포함한 모든 브랜치 목록 보기
$ git branch -a

# 브랜치 삭제
	# 삭제할 브랜치가 현재 브랜치에 합쳐졌을 경우
	$ git branch -d <branch>

	# 삭제할 브랜치가 현재 브랜치에 합쳐지지 않았어도 삭제
	$ git branch -D <branch>

# 현재 브랜치에서 새로운 브랜치 생성
$ git branch <new branch>

# 현재 브랜치에서 새로운 브랜치 생성하고 체크아웃하기
$ git branch -b <new branch>

# 다른 시작지점에서 브랜치 생성하기
$ git branch <new branch> <location>

# 기존의 브랜치를 새로운 브랜치로 덮어쓰기
$ git branch -f <branch> [<new branch location>]
```

### 4.원격저장소

#### - `clone`

```bash
# 저장소 복제
$ git clone <repo>

# 마지막 200개의 커밋만 포함한 저장소 복제
$ git clone --depth 200
```

#### - `remote`

```bash
# 새로운 원격 저장소 추가
$ git remote add <custom repo name> <repo url>

# 원격 저장소 목록 출력
$ git remote -v

# 원격 저장소에서 쓸모가 없어진 원격 브랜치 제거하기
$ git remote prune <remote repo>

# 원격 저장소 제거, 관련 브랜치 제거
$ git remote rm <remote repo>
```

#### - `push`

```bash
# 지역 브랜치를 원격 브랜치에 푸싱하기
$ git push <remote repo> <local branch>:<remote branch>

# 지역 브랜치를 동일한 이름의 원격 브랜치에 푸싱하기
$ git push <remote repo> <local branch>

# ex) origin 브랜치를 master 브랜치로 푸싱한다.
$ git push origin master

# 특정 브랜치에 정의된 remote repository가 있다면(기본 원격 원점이 사용된다)
$ git push
```

#### - `pull`

```bash
# 원격 저장소에서 변경 사항을 가져와 현재 브랜치에 합치기
$ git pull <remote repo>

# origin 저장소에서 변경 사항을 가져와 현재 브랜치에 합치기
$ git pull
```

#### - `fetch`

```bash
# origin 저장소에서 합치지 않고 지역 브랜치로 변경 사항 가져오기
$ git fetch

# 원격 저장소에서 합치지 않고 지역 브랜치로 변경사항 가져오기
$ git fetch <remote repo>
```

#### - `rm`

```bash
기본적으로 파일 삭제 -> commit 해야함

1. Untracked 파일 삭제
- 일반적 bash 파일 삭제, rm -rf 사용

2. Tracked 파일 삭제
2-1. 로컬 디렉토리와 git 저장소에서 모두 삭제
$ git rm <filename>
$ git commit -m 'Delete reason'

2-2. 로컬에서는 삭제하지 않지만 git에서는 삭제
# (git add로 커밋하지 말아야할 파일을 커밋했을 경우)
# 이 방법 사용하면 로컬에서는 파일 유지, 저장소에서만 파일 삭제 가능
$ git rm --cached <filename>
$ git commit -m 'Delete reason'

3. 기타
# -f 변경사항을 커밋하지 않았을 경우 강제로 삭제
$ git rm -f <filename>

# -r 디렉토리 삭제
$ git rm -r <directory name>
```

## Github을 이용한 협업

- Github은 본질적으로 한 명이 저장소 관리자가 되어야한다.
- 프로젝트 초기생성은 팀장이 함

```
# 폴더 생성 후 git 시작
$ git init .

# git 환경 체크
$ ls .git

# local git configuration 확인
$ cat .git/config            #refs 폴더 속 git의 해쉬 존재

$ git status
```

- 협업 중 문제 발생시 : Issue

```
Issues에 추가 가능, 태그도 달 수 있다.
```

### Case 1

```
- 동일 파일 동시작업 X

1. 작업 시간을 나눈다    or   2. 작업 폴더(파일)을 나눈다.
```

```
git pull하기 전,
항상
$ git add ~
$ git commit -m '~'
하자

```

- 만약 다른 파일을 push 해서 conflict 생겼을 때,

```
VIM이 자동으로 open됨
- esc
$ :wq
$ git pull

Auto merge된다!
: 즉, 같은 파일을 수정하지 않으면 됨
```

- 결론 : 같은 시간대에, 같은 파일을 수정하지 말자!

## ERROR handling

- `git warning: CRLF will be replaced by LF`

```
https://blog.jaeyoon.io/2018/01/git-crlf.html

이는 맥 또는 리눅스를 쓰는 개발자와 윈도우 쓰는 개발자가 Git으로 협업할 때 발생하는 Whitespace 에러다. 유닉스 시스템에서는 한 줄의 끝이 LF(Line Feed)로 이루어지는 반면, 윈도우에서는 줄 하나가 CR(Carriage Return)와 LF(Line Feed), 즉 CRLF로 이루어지기 때문이다. 따라서 어느 한 쪽을 선택할지 Git에게 혼란이 온 것이다.

해답은 core.autocrlf 를 켜는 것!

그러므로 윈도우 사용자의 경우 이러한 변환이 항상 실행되도록 다음과 같은 명령어를 입력한다. 물론 시스템 전체가 아닌 해당 프로젝트에만 적용하고 싶다면 —global 을 빼주면 된다.

$ git config --global core.autocrlf true
```

- `remote: HTTP Basic: Access denied`

```
오류 : gitlab repository에서 local로 clone하던 중 에러발생
원인 : clone 시 계정 입력 패스워드 잘못 입력
해결 : git bash 관리자 권한에서 명령어 입력
$ git config --system --unset credential.helper
```

- Git clone/push : `fatal : autentication error`

```
- credential error : config 저장된 id/pw가 맞지 않음

해결:
$ git config --global --credential.helper
- credential 정보를 리셋해주는 코드
* 관리자 권한 필요
```

- can't find remote repository <~~~>

```
- credential error : config에 저장된 id 값이 해당 원격저장소를 볼 수 있는 권한이 없음
```

- Git can't detect local changes, can't add

  - possible solution 1: https://stackoverflow.com/questions/16993082/why-doesnt-git-recognize-that-my-file-has-been-changed-therefore-git-add-not-w/24316479

  ```
  git update-index --no-assume-unchanged path/to/file
  # If that doesn't help a reset may be enough for other weird cases.

  # In practice I found removing the cached file and resetting it to work:

  git rm --cached path/to/file
  git reset path/to/file
  ```

  - possible solution 2: https://stackoverflow.com/questions/10759034/git-ignoring-a-directory-its-like-it-doesnt-exist

  ```
  # 실제로 해결한 방법, cache를 삭제하고 commit, add 한다.

  git rm --cached a/b/c
  git commit -m "removed phantom a/b/c dir"
  git add a/b/c
  git commit -m "finally able to add a/b/c"
  ```

  - possible solution 3: `.gitignore`

  ```
  # gitignore 파일에 해당 디렉토리가 추가되어있을 수도 있다. 확인하고 수정할 것
  ```

- `error: RPC failed; curl transfer closed with outstanding read data remaining`
- https://stackoverflow.com/questions/38618885/error-rpc-failed-curl-transfer-closed-with-outstanding-read-data-remaining

```
원인: git pull, 혹은 git clone 중 remote 데이터의 용량이 너무 크거나 인터넷 속도가 너무 느려서 버퍼를 감당하지 못하기 때문.
해결:
1. shallow clone 후 unshallow fetch를 통해 두번에 나눠 데이터를 가져온다.
$ git clone http://github.com/large-repository --depth 1
$ cd large-repository
$ git fetch --unshallow

2. 버퍼 사이즈를 증가시킨다
$ git config --global http.postBuffer 524288000

```
