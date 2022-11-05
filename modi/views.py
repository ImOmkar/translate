import os
import glob, random
from django.shortcuts import render
#from time import process_time

# to generate image
from .quote2image import convert, get_base64
from .dev_to_modi import dev_to_modi

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
    text = request.POST.get('text_data').replace("#", "").replace("&", "")
    translation = dev_to_modi(text)

    #to select random .png file from the folder
    img_files = ["media/diwali_background/*.*"]
    images = glob.glob(random.choice(img_files))
    random_image = random.choice(images)

    img=convert(quote=translation, image=random_image)

    # Save The Image as a Png file
    generated_image = img.save('media/quote.png')
    base_image = "data:image/png;base64," + get_base64(os.path.join(BASE_DIR, 'media', 'quote.png'))
    #processing_time = process_time()
    messages.success(request, "रूपांतरीत केलेला मजकूर तयार आहे.") 

    context = {
        "translation": translation,
        'base_image': base_image
    }
    return render(request, 'translate/translated_data.html', context)

def translated_data(request):
    return render(request, 'translate/translated_data.html')



