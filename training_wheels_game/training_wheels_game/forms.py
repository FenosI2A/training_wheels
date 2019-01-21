from django import forms
from games.models import Game


# class CreateNewGameForm(forms.Form):
#     name_form = forms.CharField(label='Name of the Game', max_length=100)


class CreateNewGameModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('game_title',)
