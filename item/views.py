from django.shortcuts import render,get_list_or_404
from .models import Item

# Create your views here.
def Detail(request ,pk):
    item = Item.objects.get(pk = pk)    
    return render(request,'detail.html' , {'item' : item})