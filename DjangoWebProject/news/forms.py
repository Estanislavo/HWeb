from .models import Articles, User
from django.forms import ModelForm, TextInput, DateInput, TimeInput, Textarea, PasswordInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'text_date']

        widgets = {
            'title' : TextInput(attrs={
                'placeholder' : 'Название статьи',
                'class' : 'form-control'
            }),

            'anons': TextInput(attrs={
                'placeholder': 'Анонс статьи',
                'class': 'form-control'
            }),

            'full_text': Textarea(attrs={
                'placeholder': 'Текст статьи',
                'class': 'form-control'
            }),

            'text_date': DateInput(attrs={
                'placeholder': 'Дата загрузки',
                'class': 'form-control'
            }),
        }

def UsernameForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password']

        widjets = {
            'login': TextInput(attrs={
                'placeholder': 'Название статьи',
                'class': 'form-control'
            }),

            'password': PasswordInput(attrs={
                'placeholder': 'Название статьи',
                'class': 'form-control'
            }),

        }