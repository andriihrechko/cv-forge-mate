from django import forms

from users.models import User
from work_profile.models import WorkProfile


class UserDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class WorkProfileForm(forms.ModelForm):
    class Meta:
        model = WorkProfile
        fields = ("desired_position", "phone_number", "location", "summary")
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3})
        }
