from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.


def index(request):
    context = {'test': 'HELLO THIS IS A TEST'}
    return render(request, 'fitboi_photo/index.html', context)


def user_image_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        # form.save()
        #     return redirect('success')
        if form.is_valid():
            print("IS VALIDDDDDD")
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'fitboi_photo/user_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
