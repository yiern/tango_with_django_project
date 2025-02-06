from django import forms
from rango.models import Page,Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text= "Enter category name")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial= 0)
    likes = forms.IntegerField(widget= forms.HiddenInput(), initial =0)
    slug = forms.CharField(widget= forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm:
    title = forms.CharField(max_length=128, help_text= "please enter title of page")
    url = forms.URLField(max_length=200, help_text= "Please enter URL of page here")
    views = forms.IntegerField(widget= forms.HiddenInput(),initial=0)

    class Meta:
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values; we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include (don't include the category field).
        # fields = ('title', 'url', 'views')
