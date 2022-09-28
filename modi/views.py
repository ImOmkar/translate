import os
from multiprocessing import context
import re
import requests
from django.shortcuts import render

# aksharamukha import
from aksharamukha import transliterate

# html to image
from .quote2image import convert

#import form
from .forms import TranslateForm

# Create your views here.



#error view
def error_404_view(request, exception):
    return render(request, 'error_pages/404.html')
#error view



def home(request):
    return render(request, 'translate/home.html')


def translate(request):
    #transliterate.process(src, tgt, txt, nativize = True, pre_options = [], post_options = [])
    text = request.POST.get('text_data')
    translated_data = requests.get(f'http://aksharamukha-plugin.appspot.com/api/public?source=Devanagari&target=Modi&text={text}')

    # Font Size Default to 32, Height and Width by default is 612
    img=convert(
        quote=translated_data.text,
        fg="white",
        image="F:\\omkar\\translate\\env\\src\\translate\\modi\\templates\\image\\background_img.jpg",
        border_color="black",
        font_size=50,
        font_file=None,
        width=1080,
        height=450)

    # Save The Image as a Png file
    generated_image = img.save("F:\\omkar\\translate\\env\\src\\translate\\modi\\templates\\generated_images\\quote.png")

    context = {
        "translated_data": translated_data.text,
        "generated_image": generated_image
    }
    return render(request, 'translate/translated_data.html', context)


def translated_data(request):
    return render(request, 'translate/translated_data.html')
