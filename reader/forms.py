from django import forms
class ReaderForm(forms.Form):
    name = forms.CharField(label="First Name", max_length=20)
    lastname = forms.CharField(label="Lastname", max_length=20 )
    age = forms.IntegerField(label="Age")
    email = forms.EmailField()


