from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Loginform(forms.Form):
	email = forms.CharField(widget=forms.TextInput)
	password  = forms.CharField(widget=forms.PasswordInput)


class loginmodel(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'email','type':'text' ,'name':'email' ,'placeholder':'email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'username','type':'text' ,'name':'username' ,'placeholder':'username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','id':'password','type':'password' ,'name':'password' ,'placeholder':'password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','id':'password','type':'password' ,'name':'password2' ,'placeholder':'password'}))
	
	class Meta:
		model  = User
		fields = ('email','username','password1','password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		print(user)
		user.set_password(user.password)
		if commit:
			user.save()
			print('')
		return user