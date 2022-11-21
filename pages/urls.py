from django.urls import path
from .views import AboutListView,ContactCreateView

urlpatterns = [
    path('about',AboutListView.as_view(),name='about-us'),
    path('contact/',ContactCreateView.as_view(),name='contact')
]
