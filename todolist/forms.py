from django import forms

class TaskForm(forms.Form):
    task_title = forms.CharField(label="Title")
    task_description = forms.CharField(label="Description", widget=forms.Textarea)