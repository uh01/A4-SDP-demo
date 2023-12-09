from django import forms
from .models import TaskModel
from category.models import CategoryModel

class TaskForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription',  'categories','is_completed',]
        # fields = '__all__'