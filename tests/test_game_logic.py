from logic_utils import check_guess, get_initial_game_state, validate_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_initial_game_state():
    state = get_initial_game_state()
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_validate_guess_within_range():
    ok, error = validate_guess(97, 1, 100)
    assert ok is True
    assert error is None


def test_validate_guess_out_of_range_high():
    ok, error = validate_guess(101, 1, 100)
    assert ok is False
    assert error == "Please guess between 1 and 100."
