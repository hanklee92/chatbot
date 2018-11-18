from django.forms import ModelForm, TextInput
from .models import City
from .models import Answer

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Ask me anything'}),
        } #updates the input class to have the correct Bulma class and placeholder

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['sentence']
        widgets = {
            'sentence': TextInput(attrs={'class' : 'input', 'placeholder': 'Ask me anything'})
        }
