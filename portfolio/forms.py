from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'cols': '30', 'rows': '7',
                   'placeholder': 'Write your notes or questions here...'}),
        required=True
    )
