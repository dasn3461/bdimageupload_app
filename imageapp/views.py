from django.shortcuts import render
from .models import Image
from .forms import FormImage

# Create your views here.

def home(request):
    if request.method =='POST':
        form=FormImage(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=FormImage()
    img=Image.objects.all()
    return render(request, 'imageapp/home.html', {'form':form, 'images':img})
    
