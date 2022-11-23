from django.urls import path
from .views import AboutListView,ContactCreateView,HomeView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('about',AboutListView.as_view(),name='about-us'),
    path('contact/',ContactCreateView.as_view(),name='contact')
]
