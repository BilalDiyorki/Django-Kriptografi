#sanal ortam içim;
#venv\Scripts\activate
#deactivate
#pip install (venv açıkken)

#>>> python manage.py shell
from accounts.models import CustomUserModel
from django.shortcuts import get_object_or_404
ikbal = get_object_or_404(CustomUserModel, id=3)
ikbal.public_key
ibrahim = get_object_or_404(CustomUserModel, id=4)
ibrahim.public_key

mesaj="bu şifrelenmesi beklenen mesaj"

# Şifreleme işlemi
sifrelenmis_mesaj = ikbal.mesaj_sifrele_ve_kaydet(ibrahim.public_key,mesaj)
sifrelenmis_mesaj

# İzla Oluşturma işlemi
imza = ikbal.imza_olustur(sifrelenmis_mesaj)
imza


# Çözme işlemi
cozulmus_mesaj = ibrahim.mesaj_coz_ve_kaydet(sifrelenmis_mesaj)
cozulmus_mesaj 

# İmza kontrol etme işlemi
imza_dogrula = ibrahim.imza_dogrula(ikbal.public_key,imza,sifrelenmis_mesaj) 
imza_dogrula  



"""
(venv) C:\Users\Getap-PC\Desktop\django-kriptoloji>python manage.py shell
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from accounts.models import CustomUserModel
>>> from django.shortcuts import get_object_or_404
>>> ikbal = get_object_or_404(CustomUserModel, id=3)
>>> ikbal.public_key
'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAi4zojQAZL53CLR0GuSfT\nAEReF3G5dQvNAE7ldNx6zFKSyMt3nLqecGEnqMJiq9RR6f+Vo+oIElCTaa2fNlLP\nGBEB80yaKgZoP86VEKgxd1LLYH63EKHc81KdzVfdMnxCYvNRlh1okCHcb9GlL1NU\nuEsL/V0nCEdtgx0z33ZdJzpXtqGM/eLzhxqqfeOjdJ9dJR14iE+WSNWWU3uGWHQt\ns49vuOe3QwqesqaK3riOgluHHAQZCiaryMjXmDsGJCDnMfJ3N/Fixhw9nvcbmWsd\ngHi5AQArpjuM3hMwYi+Ncy4q9ERKfscxSWtIoRbP43mv9TNJql5lgub7l0mxcsXH\nWwIDAQAB\n-----END PUBLIC KEY-----\n'
>>> ibrahim = get_object_or_404(CustomUserModel, id=4)
>>> ibrahim.public_key
'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmFmHGTtFMF3GxABl1nne\nXcohkS0EKPRZTuHJhTJacjeulbsylnb0udcHxORiEXFJ7I5NOdr/1wUwV40bYRjj\nqNONN3C9ImeuXzmyM/iytKKp0HN38ZvSFHWYipZwmLP7iNZlJhQ3D0KujYCwEFas\nuX749TgyG9+hLba6f7mQI78wkQ1Zm14ms+SOMXfTyYwd9Qj8ay+Xco22WTQzHdNh\nhrrwvWoMz5oTfcONE8/UJYeSv/192MXU3kqo/r3YzEOVoB8WpyL1lB7lpQJxVv1o\nsEz7hjJFKLGEY9mUpW8xqIICfopT/Ccqkmzk1vi5G2vSwzGeeSNYBmirYjc/s2Bq\nuQIDAQAB\n-----END PUBLIC KEY-----\n'
>>> sifrelenmis_mesaj = ikbal.mesaj_sifrele_ve_kaydet(ibrahim.public_key,"bu şifrelenmesi beklenen mesaj")
>>> sifrelenmis_mesaj
b"=\xa1U\x10zB{\xb1\x8cw\x13u\x98\xe3\x9f\xd9\xf6{F\x81\\\x1dgC\x1e\xe1\x10j\xc2\x8c\xf5\x86\xe7\x80\xf7\x1e\xcf\xa4\xf6\\o\xfdXGA\xacck\x88l\xb8\x92\x80\xc4\x14l\xa5\xeb$\x9c\xe1\xd1%u\xd8\xc9\xb2\xa9\xb2\x80\\\xb4\x10\xc7\xe6\xe0\xea\x90|\xfeX\x12\x92'\x1dg\r\xe9\xa4\x08\xd3\xe6p\x90\xbc4\xa0\xfb}\xfa\xa3\x9a\xfar\x81Z\xf1o\xaco(\x9bpQ\r^\x83\xcd\x90\xfb\x9c\x11\xfb\x14(Ew\x9c\xaa'\t\xb5\xd1$\x9e&\x82Z\xfd\x90\xfe;\xc6\x93\xd8\x7f\xb1C\x84#3^\xb8w!\x1f\x90#O\xa5\x96\xad\xec\xb4I\x8d\xd8\xfcj\xec\x10\x17\x87\xc0\xa5\xb4M\xfcv\xf5\xdc&\x96]E4\x98#F\xa8\xbbQl\xae\x98\xe1j\x94\x06p\xe6D\x8c\x8b\x8c[\xb4\x14X\xb5\x1a.\xe2m\x004z\xd00\x1f=p\x18\xfb\xff\xffV\xbf9[?m\xf9x\xb7\xd9\xc1\xd5\xb2qp<\xa2^2\x8d\x85\x11r\x0f\xc1\xb4\xe8Y\xf5w"
>>> imza = ikbal.imza_olustur("bu şifrelenmesi beklenen mesaj")
>>> imza
b'\x1f\x84\xd9\xbd\xad(@\x8b z\xa6\xeaxsO@\xb4\xb0\xe3\xee\x13)m\x7fa\xd9\x89\x1d\x10\xd8\xff\x8ea4\xa2\x93[\x81\xb0\x16>\x9fS\x07\x12s%\xb1J\xd0\x83\x9b\x9b\xde\x91#\xdcsy8\x93\x8e\xec\x14\xac}\xcen0(\xf2\xc3T\xc8\xb9S$\x9c\x8a\xc2_\x8a\xa7TX\xd1\xfa\xb5\x87R\xbb\x9f:\xd5\'\x1bD\xd4\xe4\xe0\x15i\x9e\xd7\xa2\x04e\x9f\xc5\xd8\x80\xf8\x14\xf2!\x92\xd62m\xc0\x17\x04]\x80\xd9\x9b\x1e\x9c;\x17z\x1d\x12oDc\xe5R#\x85\xaa\x13\x84\x8d8\x0e\xeb\xfa\xc5;\x0b\xc0\xc1\x11\x15z\xae\x895=\x0e+u\x06\xf7:\xc33\xd7\\\x92\\z#\x85\xc5Lt\xcf\xfb\xbe~c\x88*\xbf\xc4\x9as\x00B$\xafUm\x08-F\',\xbd\xdb\x88\x06\x02\x8b4\xa5\xf0\xa7\xfb\xbc\x8f\xba\x18,\x81p/y\x92\xbb\xac\xe9u\xb9ZW\x08\xc4\x89\xff\xe7\xa7Y\x8c\xc8h2\x9e<b\xabUT^"\x92\xc0.\x1c*\xcb\x85\xafp'
>>> imza_dogrula = ibrahim.imza_dogrula(ikbal.public_key,imza,"bu şifrelenmesi beklenen mesaj") 
>>> imza_dogrula  
True
>>> cozulmus_mesaj = ibrahim.mesaj_coz_ve_kaydet(sifrelenmis_mesaj)
>>> cozulmus_mesaj                                                 
b'bu \xc5\x9fifrelenmesi beklenen mesaj'
>>>

"""


"""
(venv) C:\Users\Getap-PC\Desktop\django-kriptoloji>python manage.py shell
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from accounts.models import CustomUserModel
>>> from django.shortcuts import get_object_or_404
>>> ikbal = get_object_or_404(CustomUserModel, id=3)
>>> ikbal.public_key
'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAi4zojQAZL53CLR0GuSfT\nAEReF3G5dQvNAE7ldNx6zFKSyMt3nLqecGEnqMJiq9RR6f+Vo+oIElCTaa2fNlLP\nGBEB80yaKgZoP86VEKgxd1LLYH63EKHc81KdzVfdMnxCYvNRlh1okCHcb9GlL1NU\nuEsL/V0nCEdtgx0z33ZdJzpXtqGM/eLzhxqqfeOjdJ9dJR14iE+WSNWWU3uGWHQt\ns49vuOe3QwqesqaK3riOgluHHAQZCiaryMjXmDsGJCDnMfJ3N/Fixhw9nvcbmWsd\ngHi5AQArpjuM3hMwYi+Ncy4q9ERKfscxSWtIoRbP43mv9TNJql5lgub7l0mxcsXH\nWwIDAQAB\n-----END PUBLIC KEY-----\n'
>>> ibrahim = get_object_or_404(CustomUserModel, id=4)
>>> ibrahim.public_key
'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmFmHGTtFMF3GxABl1nne\nXcohkS0EKPRZTuHJhTJacjeulbsylnb0udcHxORiEXFJ7I5NOdr/1wUwV40bYRjj\nqNONN3C9ImeuXzmyM/iytKKp0HN38ZvSFHWYipZwmLP7iNZlJhQ3D0KujYCwEFas\nuX749TgyG9+hLba6f7mQI78wkQ1Zm14ms+SOMXfTyYwd9Qj8ay+Xco22WTQzHdNh\nhrrwvWoMz5oTfcONE8/UJYeSv/192MXU3kqo/r3YzEOVoB8WpyL1lB7lpQJxVv1o\nsEz7hjJFKLGEY9mUpW8xqIICfopT/Ccqkmzk1vi5G2vSwzGeeSNYBmirYjc/s2Bq\nuQIDAQAB\n-----END PUBLIC KEY-----\n'
>>> sifrelenmis_mesaj = ikbal.mesaj_sifrele_ve_kaydet(ibrahim.public_key,"bu şifrelenmesi beklenen mesaj")
>>> sifrelenmis_mesaj
b"e\xbc@F\xfec\x7fmZ|\x9d\xa5\xc3\xf0.\xdd\x89\xd6\nM\x07\xd7\x18\x7f\x83Nd\xc7\xe2\x11:\xdd\x01.\x1e^\xef\xc3\xa0\xbf\xe3$i\x1bY\x1f8\xed\xc7\xc6\xc6(\x06\x15\xdb\x12\xd1\xd3\xc5P\x06\xed_\xb0T\xc0>\x0c\xbe\xd9\xe4\xa2@\x1e\xd9\xcb\xa9\x19\x873\xd1\x9fy\xa3\x15\x18\xc6\xbe-A\x11\x08\x1da\xc3\xa6\t\xcb\xeb\x16\xab\xfbXb\x86`\x17r\xc0Qv\xd6\xa9\x11\xfe\xf8\xf9\x10\xe0\x07\xd3\xd6\x8a\x9aiL\x86Qt\x08n\xb0qG\xf6\xb4\xc1\xd4\xc7t\x85^Gf\xc1\xd7\xf0Z\xf7\xab\xad\r\xaa\xdf>apG\xc3\xf4\x89\xc0\xbe>A\xb7iH#\x8cq\x7f\x8a\xf5\xd1\xdb\t\x91T\xedG\xae\xb6\xb9\xb0\xea\xf27\xd2VBP\xe5q\xefM\x1e\x8e\xb4\xf8\xdc\xc8\x97\xc3y\xa7\x95EVa\xa6R'o\xea\xb7\xac\xdf\x1ezi\x15Q\x02q\x13\xef\x0bkaL\x86\xa1\x93\x8f\xf2>r\xdcS\xd0)\xad%\x13\xcc\x16k\xc4\xd1\x93\xf0\x9b\xde\xa4<"       
>>> imza = ikbal.imza_olustur("bu şifrelenmesi beklenen mesaj")
>>> imza
b'.\x1fsA;\x19\x9a\xd6\xfa\x05@\x1e\xc9.\x18\xc9\xde\xf4\xdb\x04\x15!L\x90"\x0c\xa9\xfdl\x7f\xe9\xc2\xdf\x99\x98c\xa5r=\x92\xbc1\x9aHX\x84\x11d\x1a\xdb\xd1#\x11\xee\xb2l*\xb7\xb6\x1f\x0c\xb7\x16.{\xd3\xce\xe9\xcd\x84\x06fhf\x9bw\x91\xad\x94\xad\x97\x9c\xa2\x93\x8d\x05\x95\xf6\xc0\x98\xb3\xab\x89\xe2X\xa0\xa4\x02\xd7\xb1\x00kd\xfe\x92x\xa5j6\xc0\x08\x9a6\xcc\xecE\xec]\xf3T\xdcU\xf7\x9b\x88\xb9\x0b\x0f0\xcbao\xa5:\xc3;D\xf9\x1f=\xfe\xb7\x04K%\x16\x03$I\xac)\x0f\xd9\x11\xc0\xaf\xe8&\x19\xbb\x08\xcf\x81\xa8\xef^\xb1\xb5\xd6=\x95\x12\xb3\xdaKP\xa0s\xc9|M\xa4\xf7\xea\x10\x93\xd4$$\xee\xd4\xb7B\x87\xd2\xcd\x1aYK\x9e<\xf9\xb0\xccY{\xe0nJ\n&\xcd\x18\x8a\x10]\xb0\xef\xc2\xc2\xfa?\x99\xd7\xf6\x97\xa3k\x06\x05U\x04s\xe3\xffLl"\xfc\xbdA\xe4\xa3d|-z\x11\x02\xbf\xfc\xf3\xb0\xe3\x80\xd1'
>>> cozulmus_mesaj = ibrahim.mesaj_coz_ve_kaydet(sifrelenmis_mesaj)
>>> cozulmus_mesaj
'bu şifrelenmesi beklenen mesaj'
>>> imza_dogrula = ibrahim.imza_dogrula(ikbal.public_key,imza,cozulmus_mesaj) 
>>> imza_dogrula  
True
>>> 

"""