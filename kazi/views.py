from django.shortcuts import render
from .forms import KaziForm, AssignForm,EditKaziForm
from .models import Kazi, KaziFiles, Assignee
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.shortcuts import get_object_or_404

# Create your views here.


class KaziListView(ListView):
    model = Kazi
    template_name = "kazi/kazi.html"
    queryset = Kazi.objects.select_related(
        "user",
        "level",
        "course",
        "work",
    ).all()


class KaziCreateView(CreateView):
    model = Kazi
    form_class = KaziForm
    template_name = "kazi/add-kazi.html"

    def form_valid(self, form):
        files = self.request.FILES.getlist("images")
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        for i in files:
            KaziFiles.objects.create(kazi=f, image=i)
        return super(KaziCreateView, self).form_valid(form)
    
class KaziDetailView(DetailView):
    model = Kazi
    template_name = "kazi/kazi-detail.html"
    
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context[""] = 
        # return context
class KaziUpdateView(UpdateView):
    model = Kazi
    template_name = "kazi/edit-kazi.html"
    form_class = EditKaziForm
    def form_valid(self, form):
        files = self.request.FILES.getlist("images")
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        for i in files:
            KaziFiles.objects.create(kazi=f, image=i)
        return super(KaziUpdateView, self).form_valid(form)
    
class KaziDeleteView(DeleteView):
    model = Kazi
    template_name = "kazi/delete-kazi.html"
    success_url= reverse_lazy('home')


    



class AssignCreateView(CreateView):
    model = Assignee
    template_name = "kazi/assign.html"
    form_class = AssignForm
    # kazi = get_object_or_404(Kazi,id= 6)
    # kazi.status ='ASSIGNED'
    # kazi.save()
    # print(kazi.job_id)
    def form_valid(self, form):
        assign = form.save(commit=False)
        assign.kazi_id = self.kwargs["kazi_id"]

        kazi = get_object_or_404(Kazi, id=self.kwargs["kazi_id"])
        kazi.status = "ASSIGNED"
        kazi.save()
        print(kazi.job_id)

        assign.save()
        # if assign.save():

        return super(AssignCreateView, self).form_valid(form)


class AssignListView(ListView):
    model = Assignee
    template_name = "kazi/assign_list.html"
    queryset = Assignee.objects.select_related("assignee", "kazi").all()

    # for data in queryset:
    #     print(data.assignee.id)
