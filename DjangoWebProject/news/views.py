from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def news(request):
    news = Articles.objects.order_by('text_date')
    return render(request, 'news/newsh.html', {'news':news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма введена некорректно'

    form = ArticlesForm()

    data = {
        'form' : form
    }
    return render(request, 'news/create.html', data)