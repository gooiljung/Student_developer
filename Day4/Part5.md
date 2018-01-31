## Url에 View함수 연결해서 사진 출력하기

**URL Resolver**

Http request-> Django HTTP Handler -> urls ->views (<-> models) -> 직접출력 내용 만들기 or templates -> response -> HTTP Handler -> HTTP response

1. Django 에서는 URL Resolver 라는 모듈이 URL Dispatch 역할을 한다.
2. BaseHandler 클래스가 URL로 요청을 받는다.
3. RegexURLResolver 로 URL을 보낸다.
4. RegexURLResolver 가 URL에 연결된 View를 찾아서 callback함수와 인자 등을 BaseHandler 로 반환한다.
5. BaseHAndler 에서 이 함수를 실행하여 결과값인 출력물을 받아 출력한다.

- 즉 Model or View에 기능을 구현
- 이용자가 서버에 있는 자원에 접근하는 경로인 URL을 URLDispatch처리 모듈인 urls.py 에 등록하고 그 URL에 구현부를 연결한다.

**urls.py** 

- regex: 주소 패턴 (정규표현식)
- view: 연결할 View
- name: 주소 연결자 이름
- kwargs: urls 에서 View로 전달할 dict형 인자

*regex 와 view는 필수 인자 나머지 생략가능*

``` 
url(r'^hello/$', hello),
```
regex = r'^hello/$' , view = hello

**path 함수 와 url 함수의 비교**

```
path('admin/',admin.site.urls)
url(r'^admin/',admin.site.urls)

path('photos/', include('photos.urls')),
url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
```
**detail 함수 만들기 views.py**

```
from django.shortcuts import render, get_object_or_404
from .models import Photo

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    context = dict()
    context['photo'] = photo
    return render(request, 'photos/detail.html', context)
```

Django 에서는 이용자가 업로드한 파일은 MEDIA_ URL 과 MEDIA_ ROOT 라는 설정값을 참조하여 제공한다. 모델의 FileField, ImageField클래스로 지정하는 upload_to 인자는 MEDIA_ URL 과 MEDIA_ ROOT 경로 아래에 위치한다. **즉 settings.py 에 밑에 두 줄을 추가해야 image 가 나온다.**

```
MEDIA_URL = '/upload_files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```
이제 업로드된 파일은 upload_ files 라는 URL을 따르므로 urls.py에도 등록을 해야한다. upload_ files 뒤에 나오는 경로를 받은 뒤 지정된 경로에 있는 이미지 파일을 읽어서 웹브라우저에 보내고 없으면 404 에러를 발생하는데 이 작용을 django.conf.urls.static 모듈에있는 static 함수가 해준다. **urls.py에 기존 urlpatterns 아래에 추가한다.**

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
```

**render 와 HTTPResoponse**

HTTPResoponse는 Django의 view가 HTTp handler 가 건내받는 가장 기본형의 출력물이다. 그래서 HttpResponse자체는 템플릿을 같은 걸 처리하는 기능을 담고있지는 않다. 그래서 템플릿을 따로 처리하여 그려낸 rendered출력물을 문자열 그자체로 받아서 출력을 해야한다. 출력하는 부분은 게속 반복이되도록 render함수를 만든것이다.       


























