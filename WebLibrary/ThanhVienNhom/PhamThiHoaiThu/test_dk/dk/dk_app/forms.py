from django import forms
from django.core.exceptions import ValidationError
import re  # Để sử dụng biểu thức chính quy (regular expressions)

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=10, validators=[RegexValidator(regex='^[0-9]*$', message='Mã sinh viên chỉ được chứa số', code='invalid_student_id')])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@st.vju.ac.vn"):
            raise ValidationError("Email phải có định dạng @st.vju.ac.vn")

        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        # Sử dụng biểu thức chính quy để kiểm tra mật khẩu
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%^&*])[A-Za-z\d@#$!%^&*]{8,}$', password):
            raise ValidationError("Mật khẩu phải chứa ít nhất một chữ thường, một chữ hoa, một số, và một kí tự đặc biệt (@#$!%^&*) và có ít nhất 8 ký tự")

        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Mật khẩu không khớp. Vui lòng nhập lại!")

        return confirm_password
