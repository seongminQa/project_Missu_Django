from .models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['email','name','nickname']

# class RecoveryIdForm(forms.Form):
#     class Meta:
#       model = User
#       fields = ['name', 'email']

#     def __init__(self, *args, **kwargs):
#         super(RecoveryIdForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = '이름'
#         self.fields['name'].widget.attrs.update({
#             'class': 'form-control',
#             'id': 'form_name',
#         })
#         self.fields['email'].label = '이메일'
#         self.fields['email'].widget.attrs.update({
#             'class': 'form-control',
#             'id': 'form_email' 
#         })


# class RegisterForm(forms.ModelForm):
#   password = forms.PasswordInput()
#   confirm_password = forms.PasswordInput()

#   class Meta:
#     model = User
#     fields = ['email','name','nickname']