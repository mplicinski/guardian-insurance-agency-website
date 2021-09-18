from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=14, required=False)
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data ={
                "placeholder": f"{str(field).capitalize()}",
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(new_data)
        self.fields['name'].widget.attrs.update({"placeholder":"Name or Company Name"})
        message_extra_data = {
            "rows":8,
            "class":"form-control md-textarea"
        }
        self.fields['message'].widget.attrs.update(new_data)
        self.fields['phone_number'].widget.attrs.update({"placeholder":"Phone number"})