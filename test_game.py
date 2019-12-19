from game import Game

game = Game(1,2,0)

game.update_turn_state(2)

print(game.current_turn_state())

player_bet = 10

print('Player Bet: {}'.format(player_bet))


game.add_pot_size(player_bet)

print('Adding new player bet...')
print('{} should be the same as {}'.format(game.current_pot_size(),player_bet))

print('Resetting everything..')

game.reset_game()

print(game.current_pot_size())
print('{} should be predeal'.format(game.current_turn_state()))
