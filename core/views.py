from django.shortcuts import render
from item.models import Category,Item

# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold = False)
    category = Category.objects.all()
    
    return render(request,'home.html',{
        'items':items,
        'categories' : category,
    })


def contact(request):
    return render(request,'contact.html')