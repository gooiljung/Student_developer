from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import PhotoForm
# Create your views here.
from .models import Photo
from django.contrib.auth.models import User


def detail(request, pk):
    photo = get_object_or_404(Photo, pk = pk)
    context = dict()
    context['photo'] = photo
    return render(request, 'photos/detail.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'GET':
        form = PhotoForm()
    elif request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photos:detail', pk=photo.pk)
    context = {
        'form': form
    }
    return render(request, 'photos/edit.html', context)


def index(request):
    photos = Photo.objects.all().order_by('-pk')
    context = dict()
    context['photos'] = photos

    return render(request, 'photos/list.html', context)


def delete(request):
    #1.POST 요청으로 온 PK 값을 받아서 Photo 모델이 맞는지 찾는다.

    if request.method=='POST':
        photo_id =request.POST['pk']
        try:
            photo=Photo.objects.get(pk=photo_id, user=request.user)

        except:

            return redirect('photos:detail', pk=photo_id)
        photo.delete()
    #2.틀릴 경우, 다시 해당 페이지/ 맞을경우 photo를 삭제하고, list 페이지를 보여준다.

    return redirect('photos:list')

class UserCreateView(CreateView):
    template_name = 'accounts/create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('create_done')

class UserCreateDone(TemplateView):
    template_name = 'accounts/login.html'

