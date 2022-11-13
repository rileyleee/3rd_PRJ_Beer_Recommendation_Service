from django import forms
from community.models import Column, Event

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = "__all__"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"