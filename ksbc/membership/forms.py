from django import forms
from users.models import CustomUser


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'company_name',
            'job_position'
        ]
