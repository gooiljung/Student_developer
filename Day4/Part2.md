## Pystagram 개발환경

**Mac Os**

PIP 설치

```
python3 get-pip.py
```


파이썬 설치 

```
pip install python3
```

파이썬 가상환경 생성

```
python3 -m venv 가상환경이름
```
**가상환경 생성 이유**

- 개발을 할 경우에 버전마다 제공되는 라이브러리가 달라서
- 클라이언트가 요구하는 버전에 맞춰서 개발을 해줘야 할 경우에
- 가장 중요한 이유로는 버전 충돌문제를 해소하기 위해서



가상환경 활성화 

```
source 가상환경이름/bin/activate
```

가상환경 종료

```
deactivate
```

Django 설치

 - Django 설치 시에는 항상 python 가상환경을 만들고 가상환경을 활성화 한 후에 Django를 설치한다. 

```
pip install django
```


