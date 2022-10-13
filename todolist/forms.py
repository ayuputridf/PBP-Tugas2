from django import forms

class ToDoListForm(forms.Form):
    task_title = forms.CharField(label="Title")
    task_description = forms.CharField(label="Description", widget=forms.Textarea)
