from decimal import Decimal

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import Sum, F
from django.forms import ModelForm, forms
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=67, null=False)
    email = models.EmailField(max_length=58)
    password = models.CharField(max_length=58)
    password_repeat = models.CharField(max_length=58)


class vendor(models.Model):
   vendorname = models.CharField(max_length=67, null=False)
   vendoremail = models.EmailField(max_length=58)
   vendortype = models.CharField(max_length=58)
   vendorpassword = models.CharField(max_length=58)


class venuep(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   type = models.CharField(max_length=100)
   hallsize = models.CharField(max_length=58)
   seats = models.IntegerField()
   rooms = models.IntegerField()
   number = models.IntegerField()
   checks = models.CharField(max_length=100,null=True)
   about = models.TextField(max_length=98)
   image = models.ImageField(max_length=100)

class invi(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   ctype = models.CharField(max_length=100)
   boxed = models.ImageField(max_length=100,null=True)
   uboxed = models.ImageField(max_length=100,null=True)
   scroll = models.ImageField(max_length=100,null=True)
   bprice = models.IntegerField()
   unprice  = models.IntegerField(null=True)
   sprice = models.IntegerField(null=True)
   othprice=models.CharField(max_length=80,null=True)
   otherc = models.CharField(max_length=100,null=True)
   otheri = models.ImageField(max_length=100,null=True)
   about = models.TextField(max_length=98)
   other = models.ImageField(max_length=100)

class pandii(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   experi = models.CharField(max_length=100)
   number = models.IntegerField()
   service = models.CharField(max_length=100)
   lang = models.CharField(max_length=100,null=True)
   about = models.TextField(max_length=98)
   image = models.ImageField(max_length=100)

class decor(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   special = models.CharField(max_length=100)
   about = models.TextField(max_length=98,null=True)
   image = models.ImageField(max_length=100)

class cater(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   type = models.CharField(max_length=100)
   style = models.CharField(max_length=100)
   otherstyle=models.CharField(max_length=100,null=True)
   package = models.CharField(max_length=100)
   others = models.CharField(max_length=58)
   about = models.TextField(max_length=98,null=True)
   image = models.ImageField(max_length=100)

class photo(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   package = models.CharField(max_length=100)
   price = models.CharField(max_length=100)
   ameniti = models.CharField(max_length=100)
   about = models.TextField(max_length=98,null=True)
   image = models.ImageField(max_length=100)

class make(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   makeup = models.CharField(max_length=100)
   offer = models.CharField(max_length=100)
   about = models.TextField(max_length=98,null=True)
   image = models.ImageField(max_length=100)

class band(models.Model):
   name = models.CharField(max_length=58)
   style = models.CharField(max_length=100)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   event = models.CharField(max_length=100)
   others = models.CharField(max_length=100,null=True)
   about = models.TextField(max_length=98)
   image = models.ImageField(max_length=100)

class djchoreo(models.Model):
   name = models.CharField(max_length=58)
   vendor = models.CharField(max_length=100)
   address = models.CharField(max_length=58)
   number = models.IntegerField()
   genres = models.CharField(max_length=100)
   othergen = models.CharField(max_length=58)
   choreo = models.CharField(max_length=100,null=True)
   otherchoreo = models.CharField(max_length=58)
   about = models.TextField(max_length=98)
   image = models.ImageField(max_length=100)


class Wishlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   venuep = models.ForeignKey(venuep, on_delete=models.DO_NOTHING)
   invi = models.ForeignKey(invi, on_delete=models.DO_NOTHING)
   pandii = models.ForeignKey(pandii, on_delete=models.DO_NOTHING)
   decor = models.ForeignKey(decor, on_delete=models.DO_NOTHING)
   cater = models.ForeignKey(cater, on_delete=models.DO_NOTHING)
   photo = models.ForeignKey(photo, on_delete=models.DO_NOTHING)
   make = models.ForeignKey(make, on_delete=models.DO_NOTHING)
   band = models.ForeignKey(band, on_delete=models.DO_NOTHING)
   djchoreo = models.ForeignKey(djchoreo, on_delete=models.DO_NOTHING)



class vendortable(models.Model):
   name = models.CharField(max_length=58)
   address = models.CharField(max_length=58)
   vendortype=models.CharField(max_length=58)
   customerid=models.CharField(max_length=58)
   type = models.CharField(max_length=100,null=True)
   hallsize = models.CharField(max_length=58,null=True)
   seats = models.IntegerField(null=True)
   rooms = models.IntegerField(null=True)
   number = models.IntegerField()
   checks = models.CharField(max_length=100, null=True)
   about = models.TextField(max_length=98)
   image = models.ImageField(max_length=100)
   ctype = models.CharField(max_length=100,null=True)
   boxed = models.ImageField(max_length=100, null=True)
   uboxed = models.ImageField(max_length=100, null=True)
   scroll = models.ImageField(max_length=100, null=True)
   bprice = models.IntegerField(null=True)
   unprice = models.IntegerField(null=True)
   sprice = models.IntegerField(null=True)
   othprice = models.CharField(max_length=80, null=True)
   otherc = models.CharField(max_length=100, null=True)
   otheri = models.ImageField(max_length=100, null=True)
   other = models.ImageField(max_length=100,null=True)
   experi = models.CharField(max_length=100,null=True)
   service = models.CharField(max_length=100,null=True)
   lang = models.CharField(max_length=100, null=True)
   special = models.CharField(max_length=100,null=True)
   catertype = models.CharField(max_length=100,null=True)
   style = models.CharField(max_length=100,null=True)
   otherstyle = models.CharField(max_length=100, null=True)
   package = models.CharField(max_length=100,null=True)
   others = models.CharField(max_length=58,null=True)
   photopackage = models.CharField(max_length=100,null=True)
   price = models.CharField(max_length=100,null=True)
   ameniti = models.CharField(max_length=100,null=True)
   makeup = models.CharField(max_length=100,null=True)
   offer = models.CharField(max_length=100,null=True)
   bandstyle = models.CharField(max_length=100,null=True)
   event = models.CharField(max_length=100,null=True)
   bandothers = models.CharField(max_length=100, null=True)
   vendor = models.CharField(max_length=100,null=True)
   genres = models.CharField(max_length=100,null=True)
   othergen = models.CharField(max_length=58,null=True)
   choreo = models.CharField(max_length=100,null=True)
   otherchoreo = models.CharField(max_length=58,null=True)
   status=models.CharField(max_length=58,null=True)

class quotation(models.Model):
   vendorid = models.CharField(max_length=100)
   customeri=models.CharField(max_length=100)
   vendortyp=models.CharField(max_length=100,null=True)
   type=models.CharField(max_length=100,null=True)
   fdate = models.DateField(max_length=100)
   ldate = models.DateField(max_length=100)
   fname = models.CharField(max_length=100)
   lname = models.CharField(max_length=100)
   email = models.EmailField(max_length=100)
   mob = models.CharField(max_length=100)
   ame = models.CharField(max_length=100,null=True)
   guest = models.CharField(max_length=100,null=True)
   rooms = models.CharField(max_length=100,null=True)
   ftype = models.CharField(max_length=100,null=True)
   style = models.CharField(max_length=100,null=True)
   ctype = models.CharField(max_length=100,null=True)
   gender = models.CharField(max_length=100,null=True)
   etype = models.CharField(max_length=100,null=True)
   who = models.CharField(max_length=100,null=True)
   budget = models.CharField(max_length=100,null=True)
   service = models.CharField(max_length=100,null=True)
   airfunct = models.CharField(max_length=100,null=True)
   at = models.CharField(max_length=100,null=True)
   refunct = models.CharField(max_length=100,null=True)
   card = models.CharField(max_length=100,null=True)
   itype = models.CharField(max_length=100,null=True)


class res(models.Model):
   cusid=models.CharField(max_length=100)
   vendori=models.CharField(max_length=100)
   amt=models.CharField(max_length=100)
   comment=models.CharField(max_length=100)

class carty(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      status = models.BooleanField(default=False)
      added_on = models.DateTimeField(auto_now_add=True, null=True)
      update_on = models.DateTimeField(auto_now=True, null=True)
      amount=models.CharField(max_length=100)
      tamount = models.CharField(max_length=100, null=True)
      vendort = models.ForeignKey(vendortable, on_delete=models.CASCADE, null=True)



      def __str__(self):
         return self.user.username


class order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   cart_ids = models.CharField(max_length=250, null=True)
   vendor_id = models.CharField(max_length=250, null=True)
   tamount= models.CharField(max_length=250, null=True)
   invoice_id = models.CharField(max_length=250, null=True)
   status = models.BooleanField(default=False, null=True)
   processed_on = models.DateTimeField(auto_now_add=True, null=True)

class orders(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   cart_ids = models.CharField(max_length=250, null=True)
   vendor_id = models.CharField(max_length=250, null=True)
   tamount= models.CharField(max_length=250, null=True)
   invoice_id = models.CharField(max_length=250, null=True)
   status = models.BooleanField(default=False, null=True)
   processed_on = models.DateTimeField(auto_now_add=True, null=True)













