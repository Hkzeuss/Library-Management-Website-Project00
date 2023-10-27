<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django import forms
from django.core.exceptions import ValidationError
import re  # Để sử dụng biểu thức chính quy (regular expressions)

class ContactForm(forms.Form):
    recipients = forms.EmailField()

    def clean_recipients(self):
        recipients = self.cleaned_data.get("recipients")
        if not recipients.endswith("@st.vju.ac.vn"):
            raise ValidationError("Email phải có định dạng @st.vju.ac.vn")

        return recipients

    def clean_password(self):
        password = self.cleaned_data.get("password")
        # Sử dụng biểu thức chính quy để kiểm tra mật khẩu
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%^&*])[A-Za-z\d@#$!%^&*]{8,}$', password):
            raise ValidationError("Mật khẩu phải chứa ít nhất một chữ thường, một chữ hoa, một số, và một kí tự đặc biệt (@#$!%^&*) và có ít nhất 8 ký tự")

        return password
>>>>>>> e9e9e38478db451add45c16f82cff72b02584075
