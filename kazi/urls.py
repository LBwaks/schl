from django.urls import path
from .views import KaziCreateView,KaziListView,AssignCreateView,AssignListView,KaziDetailView,KaziUpdateView,KaziDeleteView

urlpatterns = [
    path('',KaziListView.as_view(),name='kazi'),
    path('add-work',KaziCreateView.as_view(),name="add-work"),
    path('<slug>',KaziDetailView.as_view(),name='kazi-detail'),
    path('edit/<slug>',KaziUpdateView.as_view(),name='edit-kazi'),
    path('delet/<slug>',KaziDeleteView.as_view(),name='delete-kazi'),
    
    # path('add/',kazi,name='add'),
    path('assign/<kazi_id>',AssignCreateView.as_view(),name='assign'),
    path('',AssignListView.as_view(),name='assigning'),
   
]
