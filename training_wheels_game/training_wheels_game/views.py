from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from game_logic.tictactoe.main import TicTacToeGame
from games.models import Game
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from training_wheels_game.forms import CreateNewGameModelForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('my_games')


@login_required
def game_list(request):
    games_info = Game.objects.filter(player_1=request.user)
    context = {
        "game_list": games_info
    }
    return render(request, "my_games.html", context)


@login_required
def available_game_list(request):
    games_info = Game.objects.filter(Q(player_2__isnull=True) | Q(player_1__isnull=True)).exclude(Q(player_1=request.user) | Q(player_2=request.user))
    print(str(games_info.query))
    context = {
        "game_list": games_info
    }
    return render(request, "available_games.html", context)


@login_required
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

    return render(request, 'Create_new_game.html', {'form': form})


@login_required
def game_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    context = {
        "game": game
    }
    return render(request, 'game_board.html', context)


def home(request):
    if request.user.is_authenticated:
        return redirect('my_games')
    return render(request, "home.html")


@login_required
def join_game_view(request, game_id):
    game = Game.objects.get(pk=game_id)
    TicTacToeGame().start_game(game, request.user)
    return redirect('game_view', game_id=game_id)

