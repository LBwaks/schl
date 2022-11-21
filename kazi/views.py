from django.shortcuts import render
from .forms import KaziForm
from .models import Kazi,KaziFiles
from django.views.generic import ListView,CreateView
# Create your views here.

def test(request):
    return render(request ,'pages/home.html')

def kazi(request):
    return render(request,'kazi/add-kazi.html')


class KaziCreateView(CreateView):
    model = Kazi
    form_class =KaziForm
    template_name = "kazi/add-kazi.html"
    
    def form_valid(self, form):
        files = self.request.FILES.getlist('images')
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        for i in files:
            KaziFiles.objects.create(kazi=f ,image =i)
        return super(KaziCreateView,self).form_valid(form)
    
