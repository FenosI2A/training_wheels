from django.shortcuts import render, redirect
from games.models import Games
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from training_wheels_game.forms import CreateNewGameModelForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def game_list(request):
    games_info = Games.objects.all()
    context = {
        "game_list": games_info
    }
    return render(request, "home.html", context)


# def create_new_game(request):
#     if request.method == 'POST':
#         game_title = request.POST['game_name']
#         player_1 = request.user
#         game_state = "State"
#         game_obj = Games(game_title=game_title, player_1=player_1, game_state=game_state)
#         game_obj.save()
#         return redirect('home')
#
#     else:
#         return render(request, "Create_new_game.html", {})


# def create_new_game_with_form(request):
#
#     if request.method == 'POST':
#         form = CreateNewGameForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['game_name']
#             player_1 = request.user
#             game_state = "State"
#             game_obj = Games(game_title=name, player_1=player_1, game_state=game_state)
#             game_obj.save()
#             return redirect('home')
#
#     else:
#         form = CreateNewGameForm()
#
#     return render(request, 'Create_new_game.html', {})


def create_new_game_with_model_form(request):

    if request.method == 'POST':
        form = CreateNewGameModelForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.player_1 = request.user
            game.game_state = "State"
            game.save()
            return redirect('home')

    else:
        form = CreateNewGameModelForm()

    return render(request, 'Create_new_game.html', {'form' : form})
