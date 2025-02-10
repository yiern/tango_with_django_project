from django import forms
from rango.models import Page,Category
from urllib.parse import quote

max_length = 200
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=max_length, help_text= "Enter category name")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial= 0)
    likes = forms.IntegerField(widget= forms.HiddenInput(), initial =0)
    slug = forms.CharField(widget= forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=max_length, help_text= "please enter title of page")
    url = forms.URLField(max_length=200, help_text= "Please enter URL of page here")
    views = forms.IntegerField(widget= forms.HiddenInput(),initial=0)
        

    class Meta:
        model = Page

        # we can either exclude the category field from the form,
        exclude = ('category',)

        # or specify the fields to include (don't include the category field).
        # fields = ('title', 'url', 'views')
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url:
            url = quote(url, safe=':/')
            cleaned_data['url'] = url
        
        
        return cleaned_data

