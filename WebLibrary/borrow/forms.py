from django import forms
from .models import Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrow_date', 'return_date']