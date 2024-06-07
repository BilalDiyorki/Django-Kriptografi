from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from accounts.models import CustomUserModel
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required(login_url='accounts:giris')
def decode_mail(request):

    ikbal = get_object_or_404(CustomUserModel, id=3)
    print("ikbal.public_key")
    print(ikbal.public_key)

    ibrahim = get_object_or_404(CustomUserModel, id=4)
    print("ibrahim.public_key")
    print(ibrahim.public_key)

    if request.method == 'POST':

        if request.POST.get('public_key') and request.POST.get('imza') and request.POST.get('decode') and request.POST.get('sifrelenmis_mesaj'):

            sifrelenmis_mesaj = request.POST.get('sifrelenmis_mesaj')
            print("sifrelenmis_mesaj")
            print(sifrelenmis_mesaj)

            cozulmus_mesaj = request.user.mesaj_coz_ve_kaydet(sifrelenmis_mesaj)

            public_key = request.POST.get('public_key')
            print("public_key")
            print(public_key)

            imza = request.POST.get('imza')
            print("imza")
            print(imza)

            imza_dogrula = request.user.imza_dogrula(public_key,imza,sifrelenmis_mesaj) 


            context={
                'imza' : imza,
                'sifrelenmis_mesaj' : sifrelenmis_mesaj,
                'cozulmus_mesaj' : cozulmus_mesaj,
                'imza_dogrula' : imza_dogrula
            }
            return render(request,'decode_mail.html',context)

        else:
            print("33333333")

            messages.warning(request,'Hatalı Bir İşlem Yaptınız.')
            return render(request,'decode_mail.html')
    else:
        print("222222222222")
        return render(request,'decode_mail.html')