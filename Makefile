.PHONY: run test test-deck test-hand test-game

run:
	@python3 app.py
test:
	@python3 -m unittest
test-deck:
	@python3 test_deck.py

test-hand:
	@python3 -m unittest test_hand 

test-game:
	@python3 -m unittest test_game
