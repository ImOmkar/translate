from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import base64

def convert(quote, image):
        
    sentence = f"{quote}"
    
    quote = ImageFont.truetype(r"static/fonts/NotoSansModiAdvanced.ttf", 200, layout_engine=ImageFont.LAYOUT_RAQM)

    back = Image.open(image, 'r')
    img_w, img_h = back.size
    d = ImageDraw.Draw(back)

    sum = 0
    for letter in sentence:
        sum += d.textsize(letter, font=quote)[0]
    average_length_of_letter = sum / len(sentence)

    number_of_letters_for_each_line = (img_w / 1.618) / average_length_of_letter
    incrementer = 0
    fresh_sentence = ""

    for letter in sentence:
        if letter == "-":
            fresh_sentence += "\n\n" + letter
        elif incrementer < number_of_letters_for_each_line:
            fresh_sentence += letter
        else:
            if letter == " ":
                fresh_sentence += "\n"
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer += 1
    dim = d.textsize(fresh_sentence, font=quote)
    x2 = dim[0]
    y2 = dim[1]

    qx = img_w / 2 - x2 / 2
    qy = img_h / 2 - y2 / 2

    d.text((qx-1, qy-1), fresh_sentence, align="center", font=quote, fill='white')
    d.text((qx+1, qy-1), fresh_sentence, align="center", font=quote, fill='white')
    d.text((qx-1, qy+1), fresh_sentence, align="center", font=quote, fill='white')
    d.text((qx+1, qy+1), fresh_sentence, align="center", font=quote, fill='white')

    d.text((qx, qy), fresh_sentence, align="center", font=quote, fill='white')

    return back


def get_base64(image):
    img = Image.open(image)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode()
