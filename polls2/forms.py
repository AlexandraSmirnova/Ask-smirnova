from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
#from polls.models import Question

class ProfileUser(forms.Form):
	username = forms.CharField(label="Your Name", widget = forms.TextInput({'class':"input-xlarge", 'placeholder':"*"}))
	mail = forms.EmailField(label="Your Email", widget = forms.TextInput({'class':"input-xlarge", 'placeholder':"*"}))	
	nick = forms.CharField(label="Your Nick", widget = forms.TextInput({'class':"input-xlarge", 'placeholder':"*"}))	
	password = forms.CharField( widget = forms.PasswordInput({'class':"input-xlarge", 'placeholder':"*"}))
	passwordSecond = forms.CharField(label="Input password again", widget = forms.PasswordInput({'class':"input-xlarge", 'placeholder':"*"}))
	avatar = forms.ImageField(label="Upload your avatar", widget = forms.FileInput({'class':"input-xlarge"}), required=False	)

class NewQuestion(forms.Form):
	title = forms.CharField(min_length=10, max_length=100, widget = forms.TextInput({'class':"input-xlarge"}))
	text = forms.CharField(min_length=10, widget = forms.TextInput({'class':"input-xlarge"}))
	tags = forms.CharField(required=False, widget = forms.TextInput({'class':"input-xlarge"}))
#	class Meta:
#		model = Question
#		fields = [ 'question_title', 'question_text', 'tags']
#		labels = {
#            'question_title': 'Title',
#						'question_text': 'Text',
#        }
#		widgets = {
#            'tags': forms.TextInput(),
#        }

class EditProfile(forms.Form):
	mail = forms.EmailField(label="New Email", widget = forms.TextInput({'class':"input-xlarge"}), required=False)
	password = forms.CharField(label="New password", widget = forms.PasswordInput({'class':"input-xlarge"}), required=False)
	passwordSecond = forms.CharField(label="Input password again", widget = forms.PasswordInput({'class':"input-xlarge"}), required=False)
	avatar = forms.ImageField(label="Upload new avatar", widget = forms.FileInput({'class':"input-xlarge"}), required=False)
	


	
