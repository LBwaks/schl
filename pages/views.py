from django.shortcuts import render
from django.views.generic import ListView,CreateView
from service.models import Service
from .models import Contact
from .forms import ContactForm
# Create your views here.

class AboutListView(ListView):
    model = Service
    template_name = "pages/about.html"
    queryset = Service.objects.all()
    
    
class ContactCreateView(CreateView):
    model = Contact
    template_name = "pages/contact.html"
    form_class = ContactForm
    
    def form_valid(self,form):
        form.send()
        return super().form_valid(form)


