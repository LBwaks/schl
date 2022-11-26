from django import forms
from .models import Kazi,Assignee
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
        fields = ['level','course','work','unit','description','due','terms']
        labels ={
            'level':'Education Level',
            'course':'Course Name',
            'work':'Type Of Work',
            'unit':'Unit',
            'descripion':'Description',
            'due':'Date Due'
        }
        
        widgets ={
            'level':forms.Select(attrs={'class':'form-control level''required'}),
            'course':forms.Select(attrs={'class':'form-control course''required'}),
            'work':forms.Select(attrs={'class':'form-control worktype''required'}),
            'unit':forms.TextInput(attrs={'class':'form-control unit''required'}),
            'description':forms.CharField(widget=CKEditorWidget()),
            'due': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control due ','type': 'datetime-local' }),
            'terms':forms.CheckboxInput(attrs={'class':'form-control terms''required'})
        }
       
        
        
        
        
        
class EditKaziForm(forms.ModelForm):
    Work_Files=forms.FileField(required=True,widget=forms.FileInput(attrs={
        'required'
        'class':'form-control images',
        'multiple':True,
        
    }))
    
    class Meta:
        model = Kazi
        fields = ['level','course','work','unit','description','due','terms']
        labels ={
            'level':'Education Level',
            'course':'Course Name',
            'work':'Type Of Work',
            'unit':'Unit',
            'descripion':'Description',
            'due':'Date Due'
        }
        
        widgets ={
            'level':forms.Select(attrs={'class':'form-control level''required'}),
            'course':forms.Select(attrs={'class':'form-control course''required'}),
            'work':forms.Select(attrs={'class':'form-control worktype''required'}),
            'unit':forms.TextInput(attrs={'class':'form-control unit''required'}),
            'description':forms.CharField(widget=CKEditorWidget()),
            'due': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control due ','type': 'datetime-local' }),
            'terms':forms.CheckboxInput(attrs={'class':'form-control terms''required'})
        }
       
        
        
        # assgin to user
        
class AssignForm(forms.ModelForm):
    # Work_Files=forms.FileField(required=True,widget=forms.FileInput(attrs={
    #     'required'
    #     'class':'form-control images',
    #     'multiple':True,
        
    # }))
    
    class Meta:
        model = Assignee
        fields = ['assignee','due',]
        labels ={
            'assignee':'Assign Work',
            # 'work':'Type Of Work',
            # 'unit':'Unit',
            # 'descripion':'Description',
            'due':'Date Due'
        }
        
        widgets ={
            # 'course':forms.Select(attrs={'class':'form-control course''required'}),
            'assignee':forms.Select(attrs={'class':'form-control assignee''required'}),
            # 'unit':forms.TextInput(attrs={'class':'form-control unit''required'}),
            # 'description':forms.CharField(widget=CKEditorWidget()),
            'due': forms.DateInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control due ','type': 'datetime-local' }),
            # 'terms':forms.CheckboxInput(attrs={'class':'form-control terms''required'})
        }
       