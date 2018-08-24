from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={"placeholder": "What's on your mind?", "class": "form-control"}))

    class Meta:
        model = Tweet
        fields = [
            # "user",
            "content",
        ]
    ''' We better do model-wide validation
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "fuck":
            raise forms.ValidationError("Cannot be rude!")
        return content
    '''
