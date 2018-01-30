## Photo 앱과 모델 만들기

**Django project 만들기**

```
django-admin startproject pystagram
```

Django project local영역에서 확인하기

```
python manage.py runserver
```

**pystagram project 초기/사전 작업**

Pystagam project를 만들고 나면 데이터베이스를 동기화하는 과정을 거쳐야한다.

```
python manage.py migrate
```
위의 명령어를 주면 Django framework에서 제공하는 데이터베이스(Sqlite) 관련작업을 진행한다.

*최고 권한 이용자 만들기*

```
python manage.py createsuperuser
```

비밀번호 변경시

```
python manage.py changepassword 사용자이름
```

**Photo App 초기작업**

Django 에서는 그 프로젝트 내의 기능들을 App이라고 부르고 Django project는 이러한 App이 하나 이상 모여서 만들어진다.

```
python manage.py startapp photos
```

- admin.py 관리자 영역에서 이 App을 다루는 코드를 담는 모듈이다.
- models.py 모델을 정의하는 모듈인데 객체를 표현하는 부분이다.
- views.py URL 접근시에 화면에 내용을 표시하는 python 함수를 호출하는 내용을 담는다. 

# MVC/MTV 

MVC|MTV
----|----
Model: 데이터베이스의 테이블에 대응, 전체 데이터의 구조를 결정한다. |Model
View: 클라이언트에 보여지는 부분을 담당한다. (HTML,CSS,JS)|Template
Controller: 사용자의 요청에 따라 Model에서 데이터를 얻어와서 view에 전달하는 역할.|View

**1. phto model 만들기**

- Django project에서 모델은 db package의 models 모듈에 있는 Model 클래스를 상속받아서 작성한다.
- Django model에는 파일을 다루는 필드는 FileField가 있는데, 이미지 파일을 대상으로 하는 ImageField 도 있다. ImageField는 FileField 를 상속 받는다.
- ImageField 내에는 upload_ to, height_ field, width_ field, max_ length, storage 등이 있고 height_ field, width_ field가 ImageField의 전용 옵션이다.
- CharField 는 데이터베이스의 VARCHAR 에 대응 하고 보통 250자 정도를 보장하고, TextField 는 훨씬 더 긴 문자열을 다룬다. 둘다 max_ length 라는 필드 옵션을 제공하는데 CharField에서는 반드시 길이를 제한해줘야 한다.
- DateTimeField 날짜와 시간을 같이 다룬다. auto.now() 객체가 저장될 때 자동으로 시간정보를 담고, auto_now_add 는 객체가 처음 생성될때 시간을 담는다.

**models.py**

```
from django.db import models

class Photo(modles.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
    content = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

이 모델을 데이터베이스에 반영하려면 makemigrations 와 migrate 명령어를 이용한다. 이때 migration 하려면 settings.py에 photo 앱을 추가해야한다. (INSTALLED_APPS 밑에다가)  

**이때 image와 filtered_image 의 모델 필드는 ImageField인데, 이 모델 필드는 이미지 파일을 처리하는 도구가 필요하다. 이미지 처리 도구인 Pillow를 설치해야 한다.**

``` 
pip install Pillow
python manage.py makemigrations
python manage.py migrate
```



 

 











































