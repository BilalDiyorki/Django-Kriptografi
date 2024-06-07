from django.shortcuts import redirect, render 
from accounts.models import CustomUserModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:giris')
def kisiler(request):
    # Admin panel yetkisine sahip olmayan tüm kullanıcıları al
    users = CustomUserModel.objects.filter(is_staff=False)

    context={
        'users':users
    }
    return render(request, 'pages/kisiler.html', context )