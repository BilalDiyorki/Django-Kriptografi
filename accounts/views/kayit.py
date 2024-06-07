from django.shortcuts import redirect, render 
from accounts.forms import KayitFormu
from django.contrib.auth import login, authenticate
from django.contrib import messages

def kayit(request):
    if request.method == 'POST':
        form = KayitFormu(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect ('anasayfa')
        else:
            context={
                'form':form
            }
            return render(request, 'pages/kayit.html', context )
    else:
        form = KayitFormu()
        context={
            'form':form
        }
        return render(request, 'pages/kayit.html', context )
