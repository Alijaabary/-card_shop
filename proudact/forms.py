from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from .models import Product, prouductcardshop




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'handle', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
  


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["image", 'name', 'handle', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      



class ProductAttachmentForm(forms.ModelForm):
    class Meta:
        model = prouductcardshop
        fields = ["file", 'name', 'is_free', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
 

ProductCardShoptModelFormSet = modelformset_factory(
    prouductcardshop,
    form=ProductAttachmentForm,
    fields = ['file', 'name','is_free', 'active'],
    extra=0,
    can_delete=True
)

ProductCardShoptModelFormSet = inlineformset_factory(
    Product,
    prouductcardshop,
    form = ProductAttachmentForm,
    formset = ProductCardShoptModelFormSet,
    fields = ['file', 'name','is_free', 'active'],
    extra=0,
    can_delete=True
)