from django import forms
from employee.models import Role,Department,Employee
from django.contrib.auth.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):
	employeeid = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'please enter 5 characters without RGL or slashes eg. A0025'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'previewImage(this);'}))
	birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	startdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	dateissued = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	class Meta:
		model = Employee
		exclude = ['is_blocked','is_deleted','created','updated']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}

