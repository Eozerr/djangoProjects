from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from pages.forms import LoginForm, RandevuForm

from pages.models import Bolum, Doktor,  Hasta, Randevu

#Hasta tarafı
def index(request):
    return render(request, 'index.html')

def hgiris(request):
    if request.method == "POST":
        tcno = request.POST.get('tcno')
        password = request.POST.get('password')
        
        try:
            hasta = Hasta.objects.get(tcno=tcno, password=password)
            request.session['tcno'] = tcno
             # kullanıcı giriş yaptıktan sonra yönlendirileceği sayfanın adını buraya yazın
        except Hasta.DoesNotExist:
            error_message = "Geçersiz TC Kimlik No veya Şifre"
            return render(request, 'hgiris.html', {'error_message': error_message})
        
        return render(request,'hanasayfa.html')
    else:
        return render(request, 'hgiris.html')



def hanasayfa(request):
    return render(request, 'hanasayfa.html')


def hral(request):
    bolumler = Bolum.objects.all()
    tcno_degeri = request.session.get('tcno')
    form = RandevuForm(request.POST or None,tcno=tcno_degeri)
    
    if request.method == 'POST':
        # Verileri modele çevir
        
        randevu = form.save(commit=False)
        # Verileri veritabanına kaydet
        
        randevu.save()
        return redirect('hanasayfa.html')
    return render(request, 'hrandevual.html', {'form': form, 'bolumler': bolumler})


def hrbilgi(request):
    tcno = request.session.get('tcno')
    if not tcno:
        return redirect('hgiris')
    
    try:
        randevu = Randevu.objects.get(tcno=tcno)
        saat = randevu.saat
        tarih = randevu.tarih
        bolum = randevu.bolum
    except Randevu.DoesNotExist:
        randevu = None
        messages.warning(request, "Randevunuz bulunmamaktadır.")
    
    form = LoginForm()
    return render(request, 'hrandevubilgi.html', {'randevu': randevu,'saat': saat, 'tarih': tarih, 'bolum': bolum, 'form': form})
    
def hriptal(request):
    return render(request, 'hrandevuiptal.html')
def hrislem(request):
    return render(request, 'hrandevuislem.html')
def hsdegis(request):
    return render(request, 'hsifredegis.html')
def hşifreu(request):
    return render(request, 'hsifreunut.html')

#Hekim tarafı 
def daktifmuayne(request):
    return render(request, 'daktifmuayne.html')
def danasayfa(request):
    return render(request, 'danasayfa.html')
def dbilgigoruntuleme(request):
    return render(request, 'dbilgigoruntuleme.html')

def dgiris(request):
    
    if request.method == "POST":
        sifre = request.POST.get('sifre')

        try:
            doktor = Doktor.objects.get(sifre=sifre)
             # kullanıcı giriş yaptıktan sonra yönlendirileceği sayfanın adını buraya yazın
        except Doktor.DoesNotExist:
            error_message = "Geçersiz Şifre"
            return render(request, 'dgiris.html', {'error_message': error_message})
        
        return render(request,'danasayfa.html')
    else:
        return render(request,'dgiris.html') 

def drandevugoruntule(request):
    return render(request, 'drandevugoruntule.html')
def drandevuiptal(request):
    return render(request, 'drandevuiptal.html')
def drandevuislem(request):
    return render(request, 'drandevuislem.html')
def dsifredegis(request):
    return render(request, 'dsifredegis.html')
def gecmismuayne(request):
    return render(request, 'gecmismuayne.html')
def servisyatanhasta(request):
    return render(request, 'servisyatanhasta.html')
def taburcuhasta(request):
    return render(request, 'taburcuhasta.html')



