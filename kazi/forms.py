from django import forms
from .models import Kazi
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class KaziForm(forms.ModelForm):
    Work_Files=forms.FileField(required=True,widget=forms.FileInput(attrs={
        'required'
        'class':'form-control images',
        'multiple':True,
        
    }))
    
    class Meta:
        model = Kazi
        fields = ['course','work','unit','description','due','terms']
        labels ={
            'course':'Course Name',
            'work':'Type Of Work',
            'unit':'Unit',
            'descripion':'Description',
            'due':'Date Due'
        }
        
        widgets ={
            'course':forms.Select(attrs={'class':'form-control course''required'}),
            'work':forms.Select(attrs={'class':'form-control worktype''required'}),
            'unit':forms.TextInput(attrs={'class':'form-control unit''required'}),
            'description':forms.CharField(widget=CKEditorWidget()),
            'due': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control due ','type': 'datetime-local' }),
            'terms':forms.CheckboxInput(attrs={'class':'form-control terms''required'})
        }
        # 'application_deadline': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control application_deadline ','placeholder': 'Select a date','type': 'datetime-local' }),
        #     'job_done_date': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control job_done_date ','placeholder ': 'Select a date','type': 'datetime-local' }),
        
        
        # def __init__(self,*args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.form_id ='kazi_form'
        #     self.helper.form_class ='kazi-form'
        #     self.helper.form_method ='post'
        #     self.helper.form_action ='kazi_action'
        #     self.helper.add_input(Submit('submit','Submit'))