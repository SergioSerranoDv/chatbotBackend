from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from  .models import Website_Model

class HelloView(View):
    def get(self, request):
        website_instance = Website_Model()
        websites = website_instance.get_all_websites()
        print(websites)
        return HttpResponse('Hello, World!, ' + str(websites))

    
# Create your views here.
