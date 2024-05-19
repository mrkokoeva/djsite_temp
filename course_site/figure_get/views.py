from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from figure_get.forms import UploadFile

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О нас', 'url_name': 'about'}]


def handle_upload_file(file):
    with open(f"uploads/{file.name}", "wb+") as temp:
        for chunk in file.chunks():
            temp.write(chunk)


def index(request):
    if request.method == "POST":
        # handle_upload_file(request.FILES["file_upload"])
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(form.cleaned_data["file"])
    else:
        form = UploadFile()
    data = {
        'menu': menu,
        'form': form
    }
    return render(request, 'index.html', context=data)


def about(request):
    data = {
        'menu': menu
    }
    return render(request, 'about.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

