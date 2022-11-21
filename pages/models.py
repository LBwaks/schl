from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.
class Contact(models.Model):
    name =models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject =models.CharField(_("Subject"), max_length=50)   
    message = models.TextField(_("Message"))
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home", )
    