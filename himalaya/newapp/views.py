from django.shortcuts import render
from .forms import ImageForm
from .models import Image, UploadedImage, IPAddress
from .middleware import ImageUploadLimitMiddleware
from .utils import get_client_ip

def index(request):

    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save() 

            client_ip = get_client_ip(request)
            try:
                ip_address_obj = IPAddress.objects.get(ip=client_ip)
            except IPAddress.DoesNotExist:
                ip_address_obj = IPAddress.objects.create(ip=client_ip)

            uploaded_image = UploadedImage.objects.create(
                image=obj.image, 
                ip_address=ip_address_obj
            )

            return render(request, "newapp/index.html", {"obj": obj})

    else:
        form = ImageForm()

    img = Image.objects.all()
    return render(request, "newapp/index.html", {"img": img, "form": form})
