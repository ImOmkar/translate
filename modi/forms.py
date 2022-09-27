from django import forms

class TranslateForm(forms.Form):
    text_data = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
