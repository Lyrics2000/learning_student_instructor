from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(
        attrs={
            "type":"text" ,"class":"form-control"

        }
    ))


class QuestionCreate(forms.Form):
    quiz = forms.CharField(widget=forms.TextInput(
        attrs={
            "type":"text" ,"class":"form-control"

        }
    ))
