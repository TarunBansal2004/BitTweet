from django import forms 
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']
        mood = forms.ChoiceField(
            choices=[('Happy', 'Happy'), ('Sad', 'Sad'), ('Nostalgic', 'Nostalgic')],
            widget=forms.Select(attrs={'class': 'form-control'})
        )
