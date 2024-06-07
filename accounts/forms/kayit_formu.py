from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUserModel

class KayitFormu(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
