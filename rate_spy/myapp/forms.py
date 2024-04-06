from django import forms

class RatingForm(forms.Form):
    url = forms.URLField(label='URL to the app with rating')
    interval = forms.IntegerField(label='Specify interval in min')
