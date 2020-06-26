.PHONY: run test test-deck test-hand test-game test-eng test-player

run:
	@python3 app.py
# https://stackoverflow.com/a/33729602/4376173
# https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-s
# -b to hide print statements
test:
	@python3 -m unittest discover tests -b
	
test-deck:
	@python3 -m unittest tests.test_deck

test-hand:
	@python3 -m unittest tests.test_hand 

# -b to hide print statements
test-game:
	@python3 -m unittest tests.test_game -b

test-eng:
	@python3 -m unittest tests.test_pokerengine

test-player:
	@python3 -m unittest tests.test_player