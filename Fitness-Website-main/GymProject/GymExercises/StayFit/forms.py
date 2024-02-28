from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))




from .models import GExercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = GExercise
        fields = ['name' , 'muscle_group', 'video', 'difficulty_level']

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))