from django.contrib import admin
from .models import Category,Service
from django.template.defaultfilters import truncatechars
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display =('title','description')
     def save_model(self, request,obj, form, change):
         if not obj.user_id:
             obj.user = request.user
             obj.save()
             
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display =('title','category','description'
                #    ,'image'
                   )
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
    def get_description(self,obj):
        return truncatechars(obj.description, 35)
    get_description.short_description= 'Description'
    

          
     
 