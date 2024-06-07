from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def anasayfa(request):

    context={
    }
    return render(request,'anasayfa.html',context)