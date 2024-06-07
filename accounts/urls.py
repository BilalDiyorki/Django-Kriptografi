from django.urls import path
from accounts.views import cikis, kayit, kisiler
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('giris', auth_views.LoginView.as_view(
        template_name = 'pages/giris.html'
    ), name='giris'),
    path('cikis', cikis, name='cikis'),
    path('kayit', kayit, name='kayit'),
    path('kisiler', kisiler, name='kisiler'),
]