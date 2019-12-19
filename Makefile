.PHONY: run test-deck test-hand test-game

run:
	@python3 app.py

test-deck:
	@python3 test_deck.py

test-hand:
	@python3 test_hand.py

test-game:
	@python3 test_game.py
