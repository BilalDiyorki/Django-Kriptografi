from django.urls import path
from post.views import mail_gonder, decode_mail

app_name = 'post'

urlpatterns = [
    path('send_mail', mail_gonder, name='send_mail'),
    path('decode_mail', decode_mail, name='decode_mail'),
]