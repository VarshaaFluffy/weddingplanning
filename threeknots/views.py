from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.db.models.fields import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .forms import Signup,VSignup,Vvendor,Cvendor,Pvendor,Dvendor,CaterVendor,PhotoVendor,MakeVendor,Bandvendor,DJChoreoVendor,quoto,Respon,Photowed,Chwed,DJwed,Dwed,Mwed,Cwed,Bwed,Iwed,Pwed,pack
from .models import login,venuep,Wishlist,vendor,vendortable,quotation,res,carty,order,orders


# Create your views here.
def home(request):
    return render(request, "home.html")
def h(request):
    return render(request, "h.html")

def goldpackage(request):
    return render(request, "goldpackage.html")

def silverpackage(request):
    return render(request, "silverpackage.html")

def platinumpackage(request):
    return render(request, "platinumpackage.html")

def accept(request):
    context = {}

    pid = request.GET["pid"]
    result=vendortable.objects.filter(id=pid).update(status='1')
    result.save()
    context["result"] = result
    return render(request, "home.html", context)
def update_product(request):
    context = {}
    cats = vendortable.objects.all().order_by("vendortype")

    context["category"] = cats

    pid = request.GET["pid"]
    product = get_object_or_404(vendortable, id=pid)
    context["product"] = product

    if request.method == "POST":
        pn = request.POST["pname"]
        ct_id = request.POST["pcat"]
        pr = request.POST["pp"]
        sp = request.POST["sp"]
        des = request.POST["des"]

        cat_obj = vendortable.objects.get(id=ct_id)

        product.product_name = pn
        product.product_category = cat_obj
        product.product_price = pr
        product.sale_price = sp
        product.details = des
        if "pimg" in request.FILES:
            img = request.FILES["pimg"]
            product.product_image = img
        product.save()
        context["status"] = "Changes Saved Successfully"
        context["id"] = pid
    return render(request, "update_product.html", context)


def delete_product(request):
    context = {}
    if "pid" in request.GET:
        pid = request.GET["pid"]
        prd = get_object_or_404(vendortable, id=pid)
        context["product"] = prd

        if "action" in request.GET:
            prd.delete()
            context["status"] = str(prd.product_name) + " removed Successfully!!!"
    return render(request, "deleteproduct.html", context)

def adverts(request):
    user = request.user.id
    result = vendortable.objects.filter(customerid=user)
    result2 = vendortable.objects.filter(status="0")
    return render(request, "adverts.html",{'result':result,'result2':result2})

def response(request):
    user=request.user.id
    result=quotation.objects.filter(vendorid=user)
    result2=res.objects.filter(cusid=user)
    result3=quotation.objects.filter(vendortyp='package')
    form = Respon()
    if request.method == 'POST':
        form = Respon(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('index')


    return render(request, "response.html",{'result':result,'result2':result2,'result3':result3,'form': form})

def vendor(request):
    form = VSignup()
    if request.method == 'POST':
        form = VSignup(request.POST)
        tp = request.POST["value"]

        if form.is_valid():
            user = form.save(commit=False)
            user.vendorpassword = make_password(user.vendorpassword)
            user.is_vendor = True
            user.save()
            username = form.cleaned_data.get('vendorname')
            messages.success(request, 'Account is created for ' + username)

        if tp =="venuevendor":
            return redirect('venuevendor')
        elif tp =="invivendor":
            return redirect('invivendor')

    context = {'form': form}
    return render(request, "vendor.html",context)

def vendorlogin(request):
    if request.method == 'POST':
        vendorname = request.POST.get('vendorname')
        vendorpassword = request.POST.get('vendorpassword')

        user = authenticate(vendorname=vendorname, vendorpassword=vendorpassword)

        if user is not None:
            vendorlogin(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'vendorlogin.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'login.html')


def submit(request):
    return render(request, "submit.html")

def package(request):
    if request.user.is_authenticated:
        form = pack(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')

    return render(request, "package.html", { 'form': form, 'usr': usr})

def dashboard(request):
    return render(request, "dashboard.html")

def index(request):
    if request.user.is_authenticated:
        # If a user is logged in, redirect them to a page informing them of such
        return render(request,'login.html')
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.is_customer = True
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)
            return redirect('login')



    context = {'form': form}
    return render(request, 'index.html', context)


def venue(request):
    result= vendortable.objects.filter(vendortype='venue')
    return render(request, "venue.html",{'result':result})

def ravimahal(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = quoto(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.ame = request.POST.getlist('ame[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/ravimahal.html',{'result':result,'form': form,'usr':usr})

def wedband(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Bwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.etype = request.POST.getlist('etype[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/wedband.html',{'result':result,'form': form,'usr':usr})

def wedcater(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Cwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.ftype = request.POST.getlist('ftype[]')
                answer.style = request.POST.getlist('style[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-catering/wedcater.html',{'result':result,'form': form,'usr':usr})

def wedchoreo(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Chwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.ctype = request.POST.getlist('ctype[]')
                answer.etype = request.POST.getlist('etype[]')
                answer.who = request.POST.getlist('who[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/wedchoreo.html',{'result':result,'form': form,'usr':usr})

def weddecor(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Dwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.service = request.POST.getlist('service[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/weddecor.html',{'result':result,'form': form,'usr':usr})

def weddingpandit(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Pwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.service = request.POST.getlist('service[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/weddingpandit.html',{'result':result,'form': form,'usr':usr})

def weddj(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = DJwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)

                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/weddj.html',{'result':result,'form': form,'usr':usr})

def wedinvitation(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Iwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.itype = request.POST.getlist('itype[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/wedinvitation.html',{'result':result,'form': form,'usr':usr})

def wedmakeup(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Mwed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/wedmakeup.html',{'result':result,'form': form,'usr':usr})

def wedphoto(request,id):
    result=get_object_or_404(vendortable,id=id)
    if request.user.is_authenticated:
        form = Photowed(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.service = request.POST.getlist('service[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')

    else:
        return redirect('index')
    return render(request,'wedding-venues/wedphoto.html',{'result':result,'form': form,'usr':usr})


def venuevendor(request):
    form = Vvendor(request.POST, request.FILES)
    usr=request.user.id
    if request.method == 'POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.checks =request.POST.getlist('checks[]')
            answer.save()
            return redirect('home')
        else:
            return redirect('index')

    return render(request, "venuevendor.html", {'form': form,'usr':usr})

def invivendor(request):
    if request.user.is_authenticated:
        form = Cvendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.ctype = request.POST.getlist('ctype[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "invivendor.html", {'form': form,'usr':usr})

def panditvendor(request):
    if request.user.is_authenticated:
        form = Pvendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.service = request.POST.getlist('service[]')
                answer.lang = request.POST.getlist('lang[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "panditvendor.html", {'form': form,'usr':usr})

def decorvendor(request):
    if request.user.is_authenticated:
        form = Dvendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.special = request.POST.getlist('special[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "decorvendor.html", {'form': form,'usr':usr})

def cateringvendor(request):
    if request.user.is_authenticated:
        form = CaterVendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.catertype = request.POST.getlist('catertype[]')
                answer.caterstyle = request.POST.getlist('caterstyle[]')
                answer.package = request.POST.getlist('package[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')

    return render(request, "cateringvendor.html", {'form': form,'usr':usr})

def photovendor(request):
    if request.user.is_authenticated:
        form = PhotoVendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.ameniti = request.POST.getlist('ameniti[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "photovendor.html", {'form': form,'usr':usr})


def makeupvendor(request):
    if request.user.is_authenticated:
        form = MakeVendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.makeup = request.POST.getlist('makeup[]')
                answer.offer = request.POST.getlist('offer[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "makeupvendor.html",  {'form': form,'usr':usr})



def djvendor(request):
    if request.user.is_authenticated:
        form = Bandvendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.event = request.POST.getlist('event[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "djvendor.html",  {'form': form,'usr':usr})





def musicdjvendor(request):
    if request.user.is_authenticated:
        form = DJChoreoVendor(request.POST, request.FILES)
        usr = request.user.id
        if request.method == 'POST':
            if form.is_valid():
                answer = form.save(commit=False)
                answer.genres = request.POST.getlist('genres[]')
                answer.choreo = request.POST.getlist('choreo[]')
                answer.save()
                return redirect('home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    return render(request, "musicdjvendor.html", {'form': form, 'usr': usr})

def invitation(request):
    result = vendortable.objects.filter(vendortype='invitation')
    return render(request, "invitation.html", {'result': result})

def pandit(request):
    result = vendortable.objects.filter(vendortype='pandit')
    return render(request, "pandit.html", {'result': result})


def decorators(request):
    result = vendortable.objects.filter(vendortype='decorators')
    return render(request, "decorators.html", {'result': result})


def catering(request):
    result = vendortable.objects.filter(vendortype='catering')
    return render(request, "catering.html", {'result': result})


def photography(request):
    result = vendortable.objects.filter(vendortype='photography')
    return render(request, "photography.html", {'result': result})


def makeup(request):
    result = vendortable.objects.filter(vendortype='makeup')
    return render(request, "makeup.html", {'result': result})


def band(request):
    result = vendortable.objects.filter(vendortype='band')
    return render(request, "band.html", {'result': result})


def djchoreo(request):
    result = vendortable.objects.filter(vendortype='DJ&Choreo')
    return render(request, "djchoreo.html", {'result': result})

def liked(request):
    wishlist = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user_id=request.user.pk)
        else:
            print("Please login")
            return redirect("login")

    return render(request, template_name='wishlist.html', context={"wishlist": wishlist})


def add_to_wishlist(request):
    if  request.POST and 'attr_id' in request.POST:
        if request.user.is_authenticated:
            data = Wishlist.objects.filter(user_id = request.user.pk,venuep_id_id = int(request.POST['attr_id']))
            if data.exists():
                data.delete()
            else:
                Wishlist.objects.create(user_id = request.user.pk,venuep_id_id = int(request.POST['attr_id']))
    else:
        print("No Product is Found")

    return redirect("/")





def wishlist(request):
    context = {}
    items = carty.objects.filter(user__id=request.user.id, status=False)
    context["items"] = items
    usr1 = request.user.id

    if request.user.is_authenticated:
        if request.method == "POST":
            pid = request.POST["pid"]
            amt=request.POST["amt"]
            is_exist = carty.objects.filter(vendort_id=pid, user_id=request.user.id, status=False)
            if len(is_exist) > 0:
                context["msz"] = "Item Already Exists in Your Wishlist"
                context["cls"] = "alert alert-warning"
            else:
                product = get_object_or_404(vendortable, id=usr1)

                usr = get_object_or_404(User, id=usr1 )
                c = carty(user=usr, vendort=product,amount=amt)
                c.save()
                context["msz"] = "{} Added in Your Cart".format(product.name)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request, "wishlist.html", context)

def booking(request):
    context = {}
    items = carty.objects.filter(user__id=request.user.id, status=False)
    total = carty.objects.aggregate(Sum("amount"))
    context["items"] = items
    context["total"] = total
    usr1 = request.user.id

    if request.user.is_authenticated:
        is_exist = carty.objects.filter(user__id=request.user.id, status=False)
        if len(is_exist) > 0:
            context["msz"] = "Item Already Exists in Your Wishlist"
            context["cls"] = "alert alert-warning"
        else:
            product = get_object_or_404(vendortable, id=usr1)
            context["msz"] = "{} Added in Your Cart".format(product.name)
            context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request, "booking.html",context)

def get_cart_data(request):
    items = carty.objects.filter(user__id=request.user.id, status=False)
    sale,total =0,0
    for i in items:
        sale += float(i.amount)
        total += float(i.amount)


    res = {
        "total":total,"offer":sale,
    }
    return JsonResponse(res)

def change_quan(request, item_id):
    if request.method == 'POST':
        cart = carty.remove(item_id)
        return HttpResponse(json.dumps(cart), content_type="application/json")
    return HttpResponse(json.dumps({"status": "error"}), content_type="application/json")


def order(request):
    items = carty.objects.filter(user_id=request.user.id, status=False)
    vendort = ""
    amt = 0
    inv = "INV10001-"
    cart_ids = ""
    p_ids = ""

    for j in items:
        vendort += str(j.vendort.id) + "\n"
        p_ids += str(j.vendort.id) + ","
        amt += float(j.amount)
        inv += str(j.id)
        cart_ids += str(j.id) + ","

    usr = User.objects.get(username=request.user.username)
    usr1=request.user.id
    ord = orders(user_id=usr1, cart_ids=cart_ids, vendor_id=p_ids, tamount=amt)
    ord.save()
    ord.invoice_id = str(ord.id) + inv

    ord.save()
    request.session["order_id"] = ord.id
    messages.success(request, "Your Order Has been Placed")
    return redirect('/')

def order_history(request):
        context = {}
        all_orders = []
        order = orders.objects.filter(user_id=request.user.id).order_by("-id")
        for orde in order:
            vendor_i = []

            for id in orde.vendor_id.split(",")[:-1]:

                try:
                    pro = vendortable.objects.get(id=id)
                    vendor_i.append(pro)
                    print(pro)
                    ord = {
                        "order_id": orde.id,
                        "vendor_id":vendor_i,
                        "invoice": orde.invoice_id,
                        "status": orde.status,
                        "date": orde.processed_on,
                        "tamount": orde.tamount,
                    }
                    all_orders.append(ord)
                    context["order_history"] = all_orders

                except ObjectDoesNotExist:
                 messages.error(request, "You do not have an active order")
                 context["order_history"] = all_orders
            return render(request, "order_history.html", context)
        return render(request, "order_history.html", context)