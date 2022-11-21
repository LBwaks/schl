from django.urls import path
from service.views import ServiceListView,ServiceDetailView

urlpatterns = [
    path('',ServiceListView.as_view(),name='services'),
    path('<slug>',ServiceDetailView.as_view(),name='service-detail')
]

