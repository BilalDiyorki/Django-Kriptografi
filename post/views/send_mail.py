from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from accounts.models import CustomUserModel
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required(login_url='accounts:giris')
def mail_gonder(request):
    ikbal = get_object_or_404(CustomUserModel, id=3)
    print("ikbal.public_key")
    print(ikbal.public_key)

    ibrahim = get_object_or_404(CustomUserModel, id=4)
    print("ibrahim.public_key")
    print(ibrahim.public_key)

    if request.method == 'POST':

        if request.POST.get('public_key') and request.POST.get('sifrele') and request.POST.get('mesaj') and not request.POST.get('gonder'):
            print("55555555")
            mesaj = request.POST.get('mesaj')
            print("mesaj")
            print(mesaj)

            public_key = request.POST.get('public_key')
            print("public_key")
            print(public_key)

            sifrelenmis_mesaj = request.user.mesaj_sifrele_ve_kaydet(public_key,mesaj)

            print("sifrelenmis_mesaj")
            print(sifrelenmis_mesaj)

            imza = request.user.imza_olustur(sifrelenmis_mesaj)

            
            print("imza")
            print(imza)

            context={
                'imza' : imza,
                'mesaj' : mesaj,
                'sifrelenmis_mesaj' : sifrelenmis_mesaj
            }
            return render(request,'send_mail.html',context)

        elif request.POST.get('email') and request.POST.get('gonder') and request.POST.get('mesaj') and not request.POST.get('sifrele'):
            print("44444444444")

            mesaj = request.POST.get('mesaj')
            print("mesaj")
            print(mesaj)

            email = request.POST.get('email')
            print("email")
            print(email)
            
            sifrelenmis_mesaj = request.POST.get('sifrelenmis_mesaj')
            print("sifrelenmis_mesaj")
            print(sifrelenmis_mesaj)

            imza = request.POST.get('imza')
            print("imza")
            print(imza)

            mesaj =     f"Tüm İçerik :\n" \
                        f"Gönderenin Adı:{request.user.first_name}\n" \
                        f"Gönderenin Soyadı:{request.user.last_name}\n" \
                        f"Gönderenin Email Adresi:{request.user.email}\n" \
                        f"Şifrelenmiş Mesaj:{sifrelenmis_mesaj}\n" \
                        f"İmza:{imza}\n" \


            send_mail(
                subject='RSA le şifrelenmiş bir mesajınız var.',
                message=mesaj,
                from_email=None,
                recipient_list=[email],
                fail_silently= False
            )
            print("mesaj gönderildi .")
            messages.success(request,'Harika, Şifreli Mesaj Gönderildi')
            return render(request,'send_mail.html')

        else:
            print("33333333")

            messages.warning(request,'Hatalı Bir İşlem Yaptınız.')
            return render(request,'send_mail.html')
    else:
        print("222222222222")
        return render(request,'send_mail.html')