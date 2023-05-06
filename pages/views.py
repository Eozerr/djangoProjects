from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from pages.forms import LoginForm, RandevuForm
from django.core.mail import send_mail
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
    tcno = request.session.get('tcno')
    bolumler = Bolum.objects.all()
    
    if request.method == 'POST':
        form = RandevuForm(request.POST, tcno=tcno)
        form.fields['tcno'].initial = tcno
        if form.is_valid():
            randevu = form.save(commit=False)
            randevu.save()
            print("Form is valid and submitted successfully.")
    else:
        form = RandevuForm(tcno=tcno)
    return render(request, 'hrandevual.html', {'form': form, 'bolumler': bolumler})


def hrbilgi(request):
    tcno = request.session.get('tcno')
    if not tcno:
        return redirect('hgiris')
    
    randevular = Randevu.objects.filter(tcno=tcno)
    if not randevular:
        messages.warning(request, "Randevunuz bulunmamaktadır.")
    
    return render(request, 'hrandevubilgi.html', {'randevular': randevular})
    
def hriptal(request):
    return render(request, 'hrandevuiptal.html')
def hrislem(request):
    return render(request, 'hrandevuislem.html')

def hsdegis(request):
    tcno = request.session.get('tcno')
    hasta = Hasta.objects.get(tcno=tcno)
    
    if request.method == 'POST':
        yeni_sifre = request.POST.get('yeni_sifre')
        yeni_sifre_tekrar = request.POST.get('yeni_sifre_tekrar')
        
        if yeni_sifre == yeni_sifre_tekrar:
            hasta.password = yeni_sifre
            hasta.save()
            return redirect('hanasayfa')
        else:
            messages.error(request, 'Şifreler eşleşmiyor.')
    
    return render(request, 'hsifredegis.html')

def hşifreu(request):
    if request.method == 'POST':
        tcno = request.POST.get('tcno')
        email = request.POST.get('email')
        try:
            hasta = Hasta.objects.get(tcno=tcno)
           
                # Şifre sıfırlama kodları buraya yazılacak
            send_mail(
                    'Şifre Hatırlatma',
                    f'Hasta Bilgileriniz:\nTC Kimlik No: {hasta.tcno}\nŞifreniz: {hasta.password}',
                    'fakeemail123@gmail.com', # fake Gmail hesabınızın kullanıcı adı
                    [email],
                    fail_silently=False,     
                )
            return redirect('hgiris')
            
                
        except Hasta.DoesNotExist:
            messages.warning(request, "Girilen TC kimlik numarası ile kayıtlı bir kullanıcı bulunamadı.")
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



