from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class CustomUserModel(AbstractUser):
    public_key = models.TextField(editable=False, verbose_name="Genel Anahtar")
    private_key = models.TextField(editable=False, verbose_name="Özel Anahtar")

    # E-posta alanını mecburi ve benzersiz yapmak için:
    email = models.EmailField(unique=True, null=False, blank=False)

    class Meta:
        db_table = 'user'
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        
        created = not self.pk  
        if created:
            # RSA anahtar çiftini oluştur
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            public_key = private_key.public_key()

            # Anahtarları PEM formatında seri hale getir ve string olarak sakla
            self.private_key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8')
            self.public_key = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')     
        super().save(*args,**kwargs)

    def imza_olustur(self, sifrelenmis_mesaj):
        sifrelenmis_mesaj = bytes.fromhex(sifrelenmis_mesaj)  # Hex string'i bytes'a dönüştür
        private_key = serialization.load_pem_private_key(
            self.private_key.encode('utf-8'),
            password=None,
            backend=default_backend()
        )
        imza = private_key.sign(
            sifrelenmis_mesaj,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return imza.hex()  # Hex formatında string olarak döndür

    def imza_dogrula(self, gonderen_genel_anahtari, imza, sifrelenmis_mesaj):
        sifrelenmis_mesaj = bytes.fromhex(sifrelenmis_mesaj)  # Hex string'i bytes'a dönüştür
        imza = bytes.fromhex(imza)  # Hex string'i bytes'a dönüştür
        public_key = serialization.load_pem_public_key(
            gonderen_genel_anahtari.encode('utf-8'),
            backend=default_backend()
        )

        try:
            public_key.verify(
                imza,
                sifrelenmis_mesaj, 
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"İmza doğrulama hatası: {e}")
            return False

    def mesaj_sifrele_ve_kaydet(self, alicinin_genel_anahtari, icerik):
        public_key = serialization.load_pem_public_key(
            alicinin_genel_anahtari.encode('utf-8'),
            backend=default_backend()
        )

        sifrelenmis_mesaj = public_key.encrypt(
            icerik.encode('utf-8'),  # İçeriği byte formatına dönüştür
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return sifrelenmis_mesaj.hex() # Hex formatında string döndür

    def mesaj_coz_ve_kaydet(self, sifrelenmis_mesaj):
        sifrelenmis_mesaj = bytes.fromhex(sifrelenmis_mesaj)  # Hex string'i bytes'a dönüştür
        private_key = serialization.load_pem_private_key(
            self.private_key.encode('utf-8'),
            password=None,
            backend=default_backend()
        )

        cozulmus_mesaj = private_key.decrypt(
            sifrelenmis_mesaj,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return cozulmus_mesaj.decode('utf-8')


