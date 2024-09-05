
from django import forms

class CartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)



from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

