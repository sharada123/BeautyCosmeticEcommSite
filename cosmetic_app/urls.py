from django.urls import path
from cosmetic_app import views
from cosmetic_store import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home),
    path('pdetails/<pid>',views.product_details),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('about',views.about),
    path('contact',views.contact),
    path('submitcontact',views.submitcontact),
    path('blog',views.blog),
    path('search/',views.search),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.cart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('checkout',views.checkout),
    path('billaddress',views.deliveryaddress),
    path('vieworder',views.viewOrder),
    path('placeorder/<aid>',views.placeorder),
    path('removeorder/<oid>',views.removeorder),
    path('makepayment',views.makepayment),
    path('sendmail/<uemail>/<uid>',views.sendusermail),
    path('exit',views.exit),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)