from django.db import models
import uuid
from .choices import job_type,course
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from ckeditor.fields import RichTextField
import random,string
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from django.urls import reverse
User = settings.AUTH_USER_MODEL
# Create your models here.


def my_slugify_function(content):
    return content.replace('_', '-').lower()

def random_string_generator(size=10,chars=string.ascii_lowercase+string.digits):
    return  ''.join(random.choice(chars) for _ in range(size))

def unique_job_id_generator(instance):
    new_job_id = random_string_generator().upper()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(job_id = new_job_id).exists()
    if qs_exists:
        return unique_job_id_generator(instance)
    return new_job_id


class WorkType(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_workType',on_delete=models.CASCADE,null = False)
    title = models.CharField(_("Work Type "), max_length=50)
    slug = AutoSlugField(populate_from='title',slugify_function = my_slugify_function)
    description =models.TextField(_("About Work Type "))
    is_published =models.BooleanField(default =False)
    is_featured = models.BooleanField(default = False)
    created_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Course(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_course',on_delete=models.CASCADE,null = False)
    title = models.CharField(_("Course Name"), max_length=50)
    slug = AutoSlugField(populate_from='title',slugify_function = my_slugify_function)
    description =models.TextField(_("About Course"))
    is_published =models.BooleanField(default =False)
    is_featured = models.BooleanField(default = False)
    created_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class EducationLevel(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_education',on_delete=models.CASCADE,null = False)
    level = models.CharField(_("Education Level "), max_length=50)
    slug = AutoSlugField(populate_from='level',slugify_function = my_slugify_function)
    description =models.TextField(_("About EDucation Level "))
    is_published =models.BooleanField(default =False)
    created_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.level

class Kazi(models.Model):
    user = models.ForeignKey(User, editable= False, related_name='user_kazi',on_delete=models.CASCADE,null = False)
    job_id = models.CharField(_("job_id"), max_length=50,blank=True)
    slug = models.UUIDField(default=uuid.uuid4,editable= False)
    level = models.ForeignKey(EducationLevel, verbose_name=_("Education Level"), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    work = models.ForeignKey(WorkType, verbose_name=_("Work Type"), on_delete=models.CASCADE)
    unit = models.CharField(_("Unit Name"), max_length=50)
    description =RichTextField()
    due = models.DateTimeField(_("Time Due"), auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=250,blank=True,null=True,default="UNASSIGNED")
    assigned_to =models.CharField(_("Assignee"), max_length=50,default=None,blank=True,null=True)
    # time = models.DateTimeField(_("Assigned  Time"),blank=True,null=True)
    
    terms =  models.BooleanField()
    updated_date = models.DateTimeField(auto_now=True,)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.job_id
    def get_absolute_url(self):
        return reverse("kazi-detail", kwargs={"slug": self.slug})
    
    
def pre_save_job_id(sender,instance,*args, **kwargs):
        if not instance.job_id:
            instance.job_id = unique_job_id_generator(instance)
pre_save.connect(pre_save_job_id,sender = Kazi)

class KaziFiles(models.Model):
    kazi = models.ForeignKey(Kazi, verbose_name=_("Kazi Files"), on_delete=models.CASCADE)
    files = models.FileField(_(""), upload_to='kazi/files', max_length=None)
    updated_date =models.DateField(auto_now=True,)
    created_date = models.DateTimeField( auto_now_add = True)
    
    # dd =models.FileField(_(""), upload_to=None, max_length=100)
    # @property
    # def photo_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
class Assignee(models.Model):
    # assigner = models.ForeignKey(User, editable= True, related_name='user_kazi_assigner',on_delete=models.CASCADE,null = False)
    kazi =models.ForeignKey(Kazi,related_name='assignee' ,on_delete=models.CASCADE)
    assignee =models.ForeignKey(User,  related_name='user_kazi_assignee',on_delete=models.CASCADE,)
    due = models.DateTimeField(_("Time Due"), auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=250,blank=True,null=True,default="WAITING")
    updated_date =models.DateField(auto_now=True,)
    created_date = models.DateTimeField( auto_now_add = True)
    
    # def __str__(self):
    #     return self.a
    def get_absolute_url(self):
        return reverse("kazi",)
    
    