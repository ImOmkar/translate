import os
import requests
from django.shortcuts import render
# to generate image
from .quote2image import convert, get_base64
from django.contrib import messages
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.



#error view
def error_404_view(request, exception):
    return render(request, 'error_pages/404.html')
#error view

def about(request):
    return render(request, 'translate/about.html')

def home(request):
    return render(request, 'translate/home.html')


def translate(request):
    text = request.POST.get('text_data')
    translated_data = requests.get(f'http://aksharamukha-plugin.appspot.com/api/public?source=Devanagari&target=Modi&text={text}')

    # Font Size Default to 32, Height and Width by default is 612
    img=convert(
        quote=translated_data.text,
        fg="white",
        image="media/background_images/background1.png",
        border_color="white",
        font_size=70,
        width=1200,
        height=670)

    # Save The Image as a Png file
    generated_image = img.save('media/quote.png')
    base_image = "data:image/png;base64," + get_base64(os.path.join(BASE_DIR, 'media', 'quote.png'))
    messages.success(request, "रूपांतरीत केलेला मजकूर तयार आहे.") 

    context = {
        "translated_data": translated_data.text,
        "generated_image": generated_image,
        'base_image': base_image
    }
    return render(request, 'translate/translated_data.html', context)


def translated_data(request):
    return render(request, 'translate/translated_data.html')



