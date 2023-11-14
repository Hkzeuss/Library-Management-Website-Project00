from .models import Profile
from django.forms.models import ModelForm
from django.forms.widgets import FileInput

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_img': FileInput()
        }
