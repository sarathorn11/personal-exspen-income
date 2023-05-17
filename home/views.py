from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    if request.method =='POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        print(text,amount,expense_type)
    
    profile = Profile.objects.filter(user=request.user).first()
    
    context = {'profile': profile}
    return render(request,'home.html',context)