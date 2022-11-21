from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Service
from django.shortcuts import get_object_or_404
# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = "services/services.html"
    queryset = Service.objects.all()
    

class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/service-detail.html"
    def get_context_data(self, **kwargs):        
        context = super(ServiceDetailView,self).get_context_data(**kwargs)
        service =get_object_or_404(Service, slug=self.kwargs['slug'])
        other_services = Service.objects.filter().exclude(slug=self.kwargs['slug']).order_by('?')
        context ={'service':service,'other_services':other_services}
        return context
        
