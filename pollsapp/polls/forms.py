from django import forms
from polls.models import Question, Choice, Track
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        #fields = ( 'question_text',)
        fields= "__all__"
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        #fields = ( 'choice_text',)
        fields= "__all__"

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ( 'name',)
