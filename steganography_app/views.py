from django.shortcuts import render
from PIL import Image
import stepic
import io
# Create your views here.
def home(request):
    return render(request, 'home.html')

def hide_text_image(image, text):
    data = text.encode('utf-8')
    return stepic.encode(image, data)

def encryption_view(request):
     message = ""
     if request.method == "POST":
         text = request.POST['text']
         image_file = request.FILES['image']
         image = Image.open(image_file)

         if image.format != 'PNG':
            image = image.convert('RGBA')
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

         new_image = hide_text_image(image, text)
         image_path = 'encrypted_images/' + 'new_' + image_file.name
         new_image.save(image_path)
         message = "Text has been encrypted in the image"


     return render(request, 'encryption.html', locals())

def decryption_view(request):
    text = ""
    if request.method == "POST":
        image_file = request.FILES['image']
        image = Image.open(image_file)

        if image.format != 'PNG':
            image = image.convert('RGBA')
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            image = Image.open(buffer)
        text = extract_text_from_image(image)
    return render(request, 'decryption.html', locals())

def extract_text_from_image(image):
    data = stepic.decode(image)
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data
