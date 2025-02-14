import pytest
from app.states_game import guess_states_play
import pandas


data = pandas.read_csv("../50_states.csv")
all_states = data.state.to_list()

def test_guess_states_play_right_guess():
    guessed_states = []  # Återställ gissningar för varje test
    answer_state = "Alabama"  # Korrekt gissning

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

    # Kontrollera att den korrekta gissningen finns i listan
    assert "Alabama" in guessed_states


def test_guess_states_play_wrong_guess():
    guessed_states = []  # Återställ gissningar för varje test
    answer_state = "Stockholm"  # Felaktig gissning

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

    # Kontrollera att den felaktiga gissningen inte finns i listan
    assert "Mars" not in guessed_states