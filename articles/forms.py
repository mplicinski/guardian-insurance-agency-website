from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f"{str(field).capitalize()}",
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(new_data)
        content_extra_data = {
            "rows": 30,
            "class": "form-control md-textarea"
        }
        self.fields['content'].widget.attrs.update(content_extra_data)

