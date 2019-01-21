import json


class TicTacToeGame:

    def start_game(self, game, joining_player):
        if game.active_player!=None:
            raise Exception("Cannot start game, this game has already started!")
        game.player_2 = joining_player
        game.game_state = json.dumps([['', '', ''], ['', '', ''], ['', '', '']])
        game.active_player = game.player_1
        game.save()





x = TicTacToeGame()



x.start_game()


# ZALOZENIA:
# * player_1 zawsze zaczyna.
# * player_1 zawsze gra krzyzykiem (X).
# * player_2 zawsze gra kółkiem (O)
# Format JSONa ze stanem gry:

stan_gry = [['X', 'O', ''], ['O', 'X', ''], ['', '', '']]

# Klasa ma metode start_game, ktora na wejściu przyjmuje instancje <Game> (model django z naszą grą) i updejtuje
# rekord Game na bazie dodając początkowy stan gry (pustą planszę) oraz inicjalizując active_player'a
# metoda ta rzuca błąd jeśli przekazana gra posiada już active usera
