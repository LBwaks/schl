from django.contrib import admin
from .models import WorkType,Course,Kazi,KaziFiles,EducationLevel

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display =('id','title','description',)
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
admin.site.register(Course,CourseAdmin)


class WorkTypeAdmin(admin.ModelAdmin):
    list_display =('title','description',)
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
admin.site.register(WorkType,WorkTypeAdmin)


class KaziAdmin(admin.ModelAdmin):
    list_display =('user','kazi_id','level','course','work','unit', 'description','due','updated_date','created_date')
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
admin.site.register(Kazi,KaziAdmin)

class FilesAdmin(admin.ModelAdmin):
    list_display= ('kazi','files')
admin.site.register(KaziFiles,FilesAdmin)


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_dispaly =('id','level','description')
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user = request.user
            obj.save()
    
