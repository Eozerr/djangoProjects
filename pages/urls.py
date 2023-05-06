from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('hastagiris/',views.hgiris, name='hgiris'),
    path('hasta-anasayfa/', views.hanasayfa, name='hanasayfa'),
    path('hasta-randevu-al/', views.hral, name='hral'),
    path('hasta-randevu-bilgi/', views.hrbilgi, name='hrbilgii'),
    path('hasta-randevu-iptal/', views.hriptal, name='hriptal'),
    path('hasta-randevu-islem/', views.hrislem, name='hrislem'),
    path('hasta-sifre-degis/', views.hsdegis, name='hsdegis'),
    path('sifre-geri-al/', views.hşifreu, name='hşifreu'),
    path('doktor-anasayfa/', views.danasayfa, name='danasayfa'),
    path('doktor-giris/', views.dgiris, name='dgiris'),
    path('doktor-randevu-goruntule/', views.drandevugoruntule, name='drandevugoruntule'),
    path('doktor-randevu-islem/', views.drandevuislem, name='drandevuislem'),
    path('doktor-sifre-güncelle/', views.dsifredegis, name='dsifredegis'),

]



