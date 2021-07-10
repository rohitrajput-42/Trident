from django.shortcuts import render
from django.views import View

class Product_list(View):
    def get(self, request):
        return render(request, 'list.html')