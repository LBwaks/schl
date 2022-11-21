from django.urls import path
from .views import test,kazi, KaziCreateView

urlpatterns = [
    path('',test,name='test'),
    path('add/',kazi,name='add'),
    path('add-work',KaziCreateView.as_view(),name="add-work")
]
