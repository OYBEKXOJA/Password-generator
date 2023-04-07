from django.shortcuts import render
import random
# Create your views here.
def Home(request):
    
    return render(request,'password/home.html')
def Password(request):
    harflar=list("abcdefghijklmnopqrstuvwxvz")
    uzunlik=int(request.GET.get('uzunlik'))
    if request.GET.get('uppercase'):
        harflar.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('specials'):
        harflar.extend(list('!@#$%^&*'))
    if request.GET.get('number'):
        harflar.extend(list('0123456789'))
    password=""
    for char in range(uzunlik):
        password+=random.choice(harflar)
    return render(request,'password/password.html',{'password':password})