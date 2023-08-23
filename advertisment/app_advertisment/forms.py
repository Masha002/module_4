from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.ModelForm):
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                               min_value=0, label='Цена')
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}), label='Изображение', required=False)

    def clean_title(self):
        titles = self.cleaned_data['title']
        if titles[0]=='?':
            raise ValidationError('Заголовок объявления не может начинаться с вопросительного знака!')
        return titles
    
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description' : forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'auction' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
    
