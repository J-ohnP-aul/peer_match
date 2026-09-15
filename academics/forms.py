from django import forms
from .models import Unit

class AcademicProfileF(forms.Form):
  reg_no = forms.CharField(max_length=30, 
    label="Registration No",
    widget=forms.Textarea(
      attrs={
        "placeholder":"e.g. IN16/XXXXX/23"
      }
  ))
  
# unit selection forms
class StudentUnitForm(forms.Form):
    units = forms.ModelMultipleChoiceField(
        queryset=Unit.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select your current units"
    )