from django.shortcuts import render

# Create your views here.

def home_view(requst):
    return render(request=requst,template_name='index.html')
