from django.shortcuts import render, redirect
from games.models import Games
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


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


def create_new_game(request):
    if request.method == 'POST':
        game_title = request.POST['game_title']
        player_1 = request.user
        game_state = "State"
        game_obj = Games(game_title=game_title, player_1=player_1, game_state=game_state)
        game_obj.save()
        return redirect('home')

    else:
        return render(request, "Create_new_game.html", {})

