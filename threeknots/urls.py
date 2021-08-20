from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('h', views.h, name='h'),
    path('order', views.order, name='order'),
    path('index', views.index, name='index'),
    path('order_history', views.order_history, name='order_history'),
    path('accept', views.accept, name='accept'),
    path('vendor', views.vendor, name='vendor'),
    path("logout", views.logout_request, name="logout"),
    path('login', views.login, name='login'),
    path('goldpackage', views.goldpackage, name='goldpackage'),
    path('silverpackage', views.silverpackage, name='silverpackage'),
    path('platinumpackage', views.platinumpackage, name='platinumpackage-'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('add-to-wishlist', views.add_to_wishlist, name='add_to_wishlist'),
    path('vendorlogin', views.vendorlogin, name='vendorlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('home', views.home, name='home'),
    path('submit', views.submit, name='submit'),
    path('package', views.package, name='package'),
    path('booking', views.booking, name='booking'),
    path('ravimahal/<int:id>',views.ravimahal,name='wedding-venues/ravimahal'),
    path('wedband/<int:id>', views.wedband, name='wedding-venues/wedband'),
    path('wedcater/<int:id>', views.wedcater, name='wedding-catering/wedcater'),
    path('wedchoreo/<int:id>', views.wedchoreo, name='wedding-venues/wedchoreo'),
    path('weddecor/<int:id>', views.weddecor, name='wedding-venues/weddecor'),
    path('weddingpandit/<int:id>', views.weddingpandit, name='wedding-venues/weddingpandit'),
    path('weddj/<int:id>', views.weddj, name='wedding-venues/weddj'),
    path('wedinvitation/<int:id>', views.wedinvitation, name='wedding-venues/wedinvitation'),
    path('wedmakeup/<int:id>', views.wedmakeup, name='wedding-venues/wedmakeup'),
    path('wedphoto/<int:id>', views.wedphoto, name='wedding-venues/wedphoto'),
    path('venue', views.venue, name='venue'),
    path('get_cart_data', views.get_cart_data, name='get_cart_data'),
    path('change_quan', views.change_quan, name='change_quan'),
    path('adverts', views.adverts, name='adverts'),
    path('response', views.response, name='response'),
    path('invitation', views.invitation, name='invitation'),
    path('pandit', views.pandit, name='pandit'),
    path('decorators', views.decorators, name='decorators'),
    path('catering', views.catering, name='catering'),
    path('photography', views.photography, name='photography'),
    path('makeup', views.makeup, name='makeup'),
    path('band', views.band, name='band'),
    path('djchoreo', views.djchoreo, name='djchoreo'),
    path('venuevendor', views.venuevendor, name='venuevendor'),
    path('invivendor', views.invivendor, name='invivendor'),
    path('photovendor', views.photovendor, name='photovendor'),
    path('makeupvendor', views.makeupvendor, name='makeupvendor'),
    path('djvendor', views.djvendor, name='djvendor'),
    path('cateringvendor', views.cateringvendor, name='cateringvendor'),
    path('panditvendor', views.panditvendor, name='panditvendor'),
    path('decorvendor', views.decorvendor, name='decorvendor'),
    path('musicdjvendor', views.musicdjvendor, name='musicdjvendor')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

