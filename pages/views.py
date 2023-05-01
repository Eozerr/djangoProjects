from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from pages.models import Hasta

#Hasta tarafı
def index(request):
    return render(request, 'index.html')


def hgiris(request):
    if request.method == "POST":
        tcno = request.POST.get('tcno')
        password = request.POST.get('password')

        try:
            hasta = Hasta.objects.get(tcno=tcno, password=password)
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
    return render(request, 'hrandevual.html')
def hrbilgi(request):
    return render(request, 'hrandevubilgi.html')
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
    return render(request, 'dgiris.html')
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



