from datetime import date
from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'edu_start': forms.DateInput(attrs={'type': 'date'}),
            'edu_end': forms.DateInput(attrs={'type': 'date'}),
            'exp_start': forms.DateInput(attrs={'type': 'date'}),
            'exp_end': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'edu_start': 'Education Start Date',
            'edu_end': 'Education End Date',
            'edu_institution': 'Education Institution',
            'edu_degree': 'Education Degree',
            'exp_start': 'Experience Start Date',
            'exp_end': 'Experience End Date',
            'exp_employer': 'Experience Employer',
            'exp_position': 'Experience Position',
        }

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-field'
            
        # Dynamically restrict the calendar from picking future dates!
        today_str = date.today().strftime('%Y-%m-%d')
        self.fields['edu_start'].widget.attrs['max'] = today_str
        self.fields['edu_end'].widget.attrs['max'] = today_str
        self.fields['exp_start'].widget.attrs['max'] = today_str
        self.fields['exp_end'].widget.attrs['max'] = today_str

    def clean(self):
        cleaned_data = super().clean()
        edu_start = cleaned_data.get("edu_start")
        edu_end = cleaned_data.get("edu_end")
        exp_start = cleaned_data.get("exp_start")
        exp_end = cleaned_data.get("exp_end")
        
        # Ensure beginning date is not higher than ending date!
        if edu_start and edu_end and edu_start > edu_end:
            self.add_error('edu_start', "Start date cannot be newer than end date.")
            
        if exp_start and exp_end and exp_start > exp_end:
            self.add_error('exp_start', "Start date cannot be newer than end date.")
            
        return cleaned_data