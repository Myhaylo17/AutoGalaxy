from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    login_input = forms.CharField(
        label="Логін або Email",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Введіть логін або email'
        })
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Введіть пароль'
        })
    )




class RegisterForm(UserCreationForm):
    # Додаємо поле email, робимо його обов'язковим
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # Вказуємо поля, які мають бути у формі:
        # беремо стандартне поле 'username' і додаємо наше 'email'
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # Додаємо Bootstrap клас 'form-control' до всіх полів
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'