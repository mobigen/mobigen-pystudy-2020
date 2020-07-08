## Git의 목적
- Git은 Linux 개발 당시 코드를 관리하기 위해 사용된 BitKeeper를 대신하기 위해 개발되었다.  
- 리눅스의 창시자인 Linus Torvalds가 주도해 개발되었고 다음과 같은 목표성을 가지고 개발되었다.
  - 빠른속도
  - 단순한구조
  - 비선형적 개발 -> 수많은 브랜치를 통한 확장적 개발
  - 완벽한 분산
  - 리눅스 커널과 같은 대형 프로젝트에도 유용할 것.

## Git의 특징
- Git은 모든 문자열의 변경 사항을 로깅해 관리한다. 이때 바뀐 부분이 있는지 없는지를 체크하고 등록하는 것을 커밋이라 한다.  
- Git을 사용하는 모든 프로젝트는 커밋된 로그가 있으면 추적가능하고, 해당 버전으로 다시 되돌아 가는것도 가능하다.  
&nbsp;&nbsp; \* Git의 소스도 Github에 공개되어 있다. 실제로 클론을 하고 처음 Linus Torvalds의 개발 로그를 확인해보면 "Git From the Hell"과 함께 그당시의 코드도 확인할 수 있다.  
- 이처럼 추적관리가 가능하기 때문에 깃을 협업 도구로 사용할때는 커밋로그도 관리할 필요가 있다.  

## Github과 Git
- Git은 버전을 관리하기 위한 하나의 소프트웨어이다. 이를 서버에 올려서 관리되도록 하는 플랫폼이 Github이다.  
- 명령어 중에 remote, push, pull과 같은 기능들을 Github과의 연동을 위해 존재하는 것이라고 생각할 수 있다.

## 기본적인 Git 명령어
- add / commit
- branch / checkout
- remote
- push / pull
- stash
- log
  - 참고 : 김정환님 블로그 [https://github.com/jeonghwan-kim/git-usage]

## 협업
- 다수의 구성원이 Git을 활용할 시에는 일종의 규칙이 필요하다. 이를 위한 가이드라인으로 제시된 것이 git-flow이다.  
- 하지만 이것은 가이드라인이고 협업 당사자들끼리 규칙을 만들어 가는 것이 필요하다.  
- 본 레포의 협업 규칙 (다양한 의견을 통해 지속적인 수정 필요)
  - 개인 계정으로 Fork (Original to Upstream Repository)
  - 로컬 환경으로 Clone (Upstream Repo to Local Env)
  - 코드 개발이후 Upstream Repo로 Push
  - Fork된 Repo에서 Original Repo로 Pull Request를 보내고 스스로 original repo에 적용


## 참고자료
- Git 공식 매뉴얼 [https://git-scm.com/book/ko/v2]
- 생활코딩 Git 강의 [https://opentutorials.org/module/3733/22434]
  - "수업을 마치며" 섹션에 Git과 연관된 수많은 강의가 존재함.