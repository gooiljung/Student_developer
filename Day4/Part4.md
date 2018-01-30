## Adim.py에서 모델에 데이터 넣기

Photo 모델을 이용하여 데이터베이스를 넣는다. view에 관련기능을 구현해도 되지만 Django의 장점 중 하나인 Admin 기능을 이용해서 자료를 관리한다.

***admin.py***

```
from django.contrib import admin
from .models import Photo

admin.site.register(Photo)
```
이 과정을 마치면 local/admin 으로 들어가면 ``` python manage.py createsuperuser``` 에서 만든 ID 와 Password로 접속할 수 있다.

urls.py 에는 기본적을 admin 부분에 있는 모든경로를 이미 포함해있다.
``` urlpatterns = [
  path('admin/', admin.site.urls),
  ]
```


**Photo 모델을 수정하여 데이터 삭제시 업로드한 사진도 삭제하는 방법**

- Photo class에 delete 함수를 추가한다.

```
class Photo(models.Model):
    def delete(self,*args,**kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)
```


























