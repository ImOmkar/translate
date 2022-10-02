import requests
from django.shortcuts import render

# to generate image
from .quote2image import convert

# Create your views here.



#error view
def error_404_view(request, exception):
    return render(request, 'error_pages/404.html')
#error view


def home(request):
    return render(request, 'translate/home.html')


def translate(request):
    text = request.POST.get('text_data')
    translated_data = requests.get(f'http://aksharamukha-plugin.appspot.com/api/public?source=Devanagari&target=Modi&text={text}')

    context = {
        "translated_data": translated_data.text,
    }
    return render(request, 'translate/translated_data.html', context)


def translated_data(request):
    return render(request, 'translate/translated_data.html')
