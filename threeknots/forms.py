from django.forms import ModelForm
from django import forms
from .models import login,venuep,invi,pandii,decor,cater,photo,make,band,djchoreo,vendor,vendortable,quotation,res


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# define the class of a form
# model=login
#username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
 #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   # password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class Signup(ModelForm):
   class Meta:
       model = User
       fields = ['username','email','password']

class pack(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','vendortyp','type']

class VSignup(ModelForm):
   class Meta:
       model = vendor
       fields = ['vendorname','vendoremail','vendortype','vendorpassword']

class Vvendor(ModelForm):
    class Meta:
        model = vendortable
        fields = ['name','address','customerid','vendortype','type','hallsize','seats','rooms','number','about','image']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
           'hallsize': forms.TextInput(attrs={'placeholder': 'hallsize'}),
           'seats': forms.TextInput(attrs={'placeholder': 'name'}),
            'rooms': forms.TextInput(attrs={'placeholder': 'venue type'}),
            'number': forms.TextInput(attrs={'placeholder': 'address'}),

       }

class quoto(ModelForm):
    class Meta:
        model=quotation
        fields = ['fdate', 'ldate', 'fname', 'lname', 'email',
                  'mob', 'guest', 'rooms','vendortyp']

class Pwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','vendortyp']

class Iwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','card','budget','vendortyp']

class Bwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','vendortyp']

class Dwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','budget','guest','vendortyp']

class Cwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','vendortyp']

class Mwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','guest','airfunct','at','refunct','vendortyp']

class DJwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','gender','vendortyp']

class Chwed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','vendortyp']

class Photowed(ModelForm):
    class Meta:
        model = quotation
        fields = ['fdate', 'ldate','fname','lname', 'email',
                  'mob','vendortyp']

class Cvendor(ModelForm):
    class Meta:
        model = vendortable
        fields = ['name', 'address','customerid','vendortype', 'number',
                  'image','about',]
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
            'number': forms.TextInput(attrs={'placeholder': 'number'}),

       }

class Pvendor(ModelForm):
    class Meta:
        model =  vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'experi', 'number',
                  'image', 'about']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
           'experi': forms.TextInput(attrs={'placeholder': 'experience'}),

       }

class Dvendor(ModelForm):
    class Meta:
        model =vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'number',
                  'image', 'about']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
       }

class CaterVendor(ModelForm):
    class Meta:
        model =vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'number',
                  'image', 'about']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
       }

class PhotoVendor(ModelForm):
    class Meta:
        model =vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'photopackage','price', 'number',
                  'image', 'about',]
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
       }

class MakeVendor(ModelForm):
    class Meta:
        model =vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'number',
                  'image', 'about']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
       }

class Bandvendor(ModelForm):
    class Meta:
        model =vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'bandstyle', 'number',
                  'image', 'about']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
       }

class DJChoreoVendor(ModelForm):
    class Meta:
        model =vendortable
        fields = ['name', 'address', 'customerid', 'vendortype', 'vendor', 'number',
                  'image', 'about']
        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'name'}),
           'address': forms.TextInput(attrs={'placeholder': 'address'}),
       }
class Respon(ModelForm):
    class Meta:
        model = res
        fields = ['amt', 'comment', 'cusid', 'vendori']