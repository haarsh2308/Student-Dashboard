from django import forms
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [ 'title', 'description']

class dashboardform(forms.Form):
    text= forms.CharField(max_length=100,label="Search")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [ 'title', 'is_completed']