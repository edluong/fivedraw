.PHONY: run test test-deck test-hand test-game test-eng

run:
	@python3 app.py
test:
	@python3 -m unittest
test-deck:
	@python3 -m unittest test_deck

test-hand:
	@python3 -m unittest test_hand 

test-game:
	@python3 -m unittest test_game

test-eng:
	@python3 -m unittest test_pokerengine
