from django import forms

class RatingForm(forms.Form):
    url = forms.URLField(label='URL of the App')
    name = forms.CharField(max_length=100, required=False)
    # interval_in_minutes = forms.IntegerField(label='Interval (minutes)', min_value=1, help_text='Specify the time interval in minutes.', disabled=True)
