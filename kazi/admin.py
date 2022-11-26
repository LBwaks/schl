from django.contrib import admin
from .models import WorkType,Course,Kazi,KaziFiles,EducationLevel,Assignee
from django.contrib.auth.models import User

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
    list_display =('user','job_id','level','course','work','unit', 'description','status','assigned_to','due','updated_date','created_date')
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
    
@admin.register(Assignee)
class AssigneeAdmin(admin.ModelAdmin):
    list_display= ('kazi','assignee','due','updated_date')
    # def save_model(self,request,obj,form,change):
    #     if not obj.user_id:
    #         obj.user = request.user
    #         obj.save()
    
