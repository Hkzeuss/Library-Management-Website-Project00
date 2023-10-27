from django import forms
from django.core.exceptions import ValidationError
from your_app.models import CustomUser

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    student_id = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        student_id = cleaned_data.get('student_id')

        # Kiểm tra mật khẩu nhập lại
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Mật khẩu không khớp.")

        # Kiểm tra ID trùng
        if CustomUser.objects.filter(ID_student=student_id).exists():
            raise ValidationError("ID đã tồn tại. Vui lòng chọn ID khác.")