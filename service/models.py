from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
User = settings.AUTH_USER_MODEL
from django.urls import reverse
# Create your models here.


def my_slugify_function(content):
    return content.replace('_', '-').lower()




class Category(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_category',on_delete=models.CASCADE,null = False)
    title = models.CharField(_("Category "), max_length=50)
    slug = AutoSlugField(populate_from='title',slugify_function = my_slugify_function)
    description =models.TextField(_("About Category "))
    is_published =models.BooleanField(default =False)   
    created_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_service',on_delete=models.CASCADE,null = False)      
    title = models.CharField(_("Service Title"), max_length=50)
    slug = AutoSlugField(populate_from='title',slugify_function = my_slugify_function)
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)    
    description =RichTextField()
    # image = models.ImageField(_("Image"), upload_to='kazi/services', height_field=None, width_field=None, max_length=None)
    updated_date = models.DateTimeField(auto_now=True,)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("service-detail", kwargs={"slug": self.slug})
    @property
    def photo_url(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
        
class EducationLevel(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_education_level',on_delete=models.CASCADE,null = False)
    level = models.CharField(_("Education Level "), max_length=50)
    slug = AutoSlugField(populate_from='level',slugify_function = my_slugify_function)
    description =models.TextField(_("About EDucation Level "))
    is_published =models.BooleanField(default =False)
    created_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.level
    # def get_absolute_url(self):
    #     return reverse("service-detail", kwargs={"slug": self.slug})
    
    
class WorkType(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='education_work',on_delete=models.CASCADE,null = False)
    work = models.CharField(_("Work Type "), max_length=50)
    slug = AutoSlugField(populate_from='work',slugify_function = my_slugify_function)
    education_level = models.ForeignKey(EducationLevel, verbose_name=_("Education Level"), on_delete=models.CASCADE)
    description =models.TextField(_("About Work Type "))
    is_published =models.BooleanField(default =False)
    created_date =models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.work
    # def get_absolute_url(self):
    #     return reverse("service-detail", kwargs={"slug": self.slug})
    
class Pricing(models.Model):
    user =models.ForeignKey(User, editable= False, related_name='user_pricing',on_delete=models.CASCADE,null = False)
    education =models.ForeignKey(EducationLevel, verbose_name=_("Education Level"), on_delete=models.CASCADE)
    work = models.ForeignKey(WorkType, verbose_name=_("Work Type"), on_delete=models.CASCADE)
    price = models.IntegerField(_("Price"))
    slug = AutoSlugField(populate_from=['education','level','price'],slugify_function = my_slugify_function)
    is_published =models.BooleanField(default =False)
    is_featured = models.BooleanField(default = False)
    created_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.price
    
