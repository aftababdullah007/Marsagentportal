# portal/forms.py
from django import forms
from .models import LeaveRequest, Complaint, Resignation, DEPARTMENT_CHOICES

class BaseStyledForm(forms.ModelForm):
    """Add Bootstrap .form-control to inputs & textareas automatically."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect, forms.Select)):
                field.widget.attrs.update({'class': 'form-control'})
        # style selects too
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})


class LeaveRequestForm(BaseStyledForm):
    class Meta:
        model = LeaveRequest
        fields = ["employee_name", "department", "joining_date", "date", "reason"]  # ✅ added joining_date
        widgets = {
            "joining_date": forms.DateInput(attrs={"type": "date"}),  # ✅ widget
            "date": forms.DateInput(attrs={"type": "date"}),
            "reason": forms.Textarea(attrs={"rows": 4}),
        }


class ComplaintForm(BaseStyledForm):
    class Meta:
        model = Complaint
        fields = ["agent_name", "department", "joining_date", "complaint_against", "complaint_text"]  # ✅ added joining_date
        widgets = {
            "joining_date": forms.DateInput(attrs={"type": "date"}),  # ✅ widget
            "complaint_text": forms.Textarea(attrs={"rows": 5}),
        }


class ResignationForm(BaseStyledForm):
    class Meta:
        model = Resignation
        fields = ["employee_name", "department", "joining_date", "date", "reason"]  # ✅ added joining_date
        widgets = {
            "joining_date": forms.DateInput(attrs={"type": "date"}),  # ✅ widget
            "date": forms.DateInput(attrs={"type": "date"}),
            "reason": forms.Textarea(attrs={"rows": 4}),
        }
