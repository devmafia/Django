from django import forms
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get("message")
        if "spam" in message.lower():
            raise forms.ValidationError("We do not accept spam messages.")
        return cleaned_data
    
class FeedbackForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    feedback = forms.CharField(widget=forms.Textarea, required=True)

    def clean_full_name(self):
        data = self.cleaned_data['full_name']
        if not data.replace(" ", "").isalpha():
            raise forms.ValidationError("Full name should only contain letters.")
        return data

    def clean_feedback(self):
        feedback = self.cleaned_data['feedback']
        if "complaint" in feedback.lower():
            raise forms.ValidationError("We do not accept complaints in the feedback.")
        return feedback
