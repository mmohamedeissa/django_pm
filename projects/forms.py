from django import forms

from projects.models import Project


attrs = {
    'class': 'form-control',
}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category']

        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs),
            'category': forms.Select(attrs=attrs),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'status']

        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs),
            'category': forms.Select(attrs=attrs),
            'status': forms.Select(attrs=attrs),
        }


