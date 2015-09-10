from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    def setFieldSize(self):
        self.fields['message'].widget.attrs = {'rows': '4', 'cols': '25'}
