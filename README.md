# 🗂Airbnb clone  
  
  
### 0~1 Chap  
**🔹1-1. pipenv를 사용해야 하는 이유**  
`pip install django==3.0` 같이 pip를 이용한 django 설치는 PC 안에 Globally하게 설치되므로 서로 다른 버전의 django 프로젝트를 실행시킬 수가 없다.  
따라서 pipenv를 이용하여 django를 설치해야 한다.  
pipenv는 윈도우 환경의 파이썬 패키지 관리자로 Bubble 같은 가상 환경 안에 django를 설치한다.  
  
**🔹1-2. pipenv를 실행하는 명령어**  
```
pipenv --three  # python 3.0 version을 사용할 수 있는 가상환경 생성 (cmd)  
pipenv shell  # 가상환경 안으로 들어가게 해주는 명령어 (vscode)
```
**❗항상 버블 안에(가상환경 안에) 있을 것❗**  
  
---
  
  
### 2 Chap  
**🔹2-1. django project를 시작하는 좋은 방법**  
django-admin startproject mysite 방식은 매우 간편하므로 초심자에게는 좋지만,  
실제의 장고 어플리케이션을 다루기엔 좋은 방식이 아니다.  
이 구조화 방식은 어플리케이션이 커지거나 여러 개발자와 협업할 때 좋지 않기 때문이다.  
강의에서 추천하는 방식은 현재 django 버전에서는 `django-admin startproject mysite .` 명령어로 대체 가능하다.

**🔹2-2. Linter and Fomatter**  
Linter : 컴파일이 없는 Runtime 언어인 파이썬의 오류를 코드 실행 전에 감지하기 위해 오류가 생길 부분을 알려주는 확장 프로그램. 파이썬에서 널리 써이는 관습도 준수할 수 있게 도와준다. 강의에서는 *flake8*을 사용했다.  
Formatter : 코드를 더 보기 좋게 자동으로 수정해주는 확장 프로그램. 강의에서는 *black*을 사용했다.

**🔹2-3. Pipfile 안의 packages and dev-packages**  
pipfile안의 [packages] : 웹 애플리케이션이 동작할 때 필요한 패키지  
pipfile안의 [dev-packages] : 개발자가 개발할 때만 필요한 패키지  
  

