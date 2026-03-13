from logic_utils import check_guess, get_initial_game_state, validate_guess, parse_guess

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


# ============================================================================
# EDGE CASE TESTS: Parse Guess
# ============================================================================

def test_parse_guess_negative_number():
    """Test that negative numbers parse successfully (validation catches them later)."""
    ok, guess, error = parse_guess("-50")
    assert ok is True
    assert guess == -50
    assert error is None


def test_parse_guess_decimal_string():
    """Test that decimal strings fail gracefully."""
    ok, guess, error = parse_guess("50.5")
    assert ok is False
    assert guess is None
    assert error == "That is not a whole number."


def test_parse_guess_with_whitespace():
    """Test that leading/trailing whitespace is handled correctly."""
    ok, guess, error = parse_guess("  42  ")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_guess_special_characters():
    """Test that strings with special characters fail gracefully."""
    ok, guess, error = parse_guess("50!")
    assert ok is False
    assert guess is None
    assert error == "That is not a whole number."


def test_parse_guess_non_numeric_string():
    """Test that pure non-numeric strings (like 'hello') fail gracefully."""
    ok, guess, error = parse_guess("hello")
    assert ok is False
    assert guess is None
    assert error == "That is not a whole number."


def test_parse_guess_empty_input():
    """Test that empty input is rejected with clear error message."""
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_guess_zero():
    """Test that zero is parsed as a valid integer (validation rejects it)."""
    ok, guess, error = parse_guess("0")
    assert ok is True
    assert guess == 0
    assert error is None


def test_parse_guess_very_large_number():
    """Test that very large numbers parse without overflow issues."""
    ok, guess, error = parse_guess("999999999999999")
    assert ok is True
    assert guess == 999999999999999
    assert error is None


# ============================================================================
# EDGE CASE TESTS: Validate Guess (Range Boundaries)
# ============================================================================

def test_validate_guess_at_lower_boundary():
    """Test that the exact lower boundary is valid."""
    ok, error = validate_guess(1, 1, 100)
    assert ok is True
    assert error is None


def test_validate_guess_at_upper_boundary():
    """Test that the exact upper boundary is valid."""
    ok, error = validate_guess(100, 1, 100)
    assert ok is True
    assert error is None


def test_validate_guess_below_lower_boundary():
    """Test that values below the lower boundary are rejected."""
    ok, error = validate_guess(0, 1, 100)
    assert ok is False
    assert error == "Please guess between 1 and 100."


def test_validate_guess_above_upper_boundary():
    """Test that values above the upper boundary are rejected."""
    ok, error = validate_guess(101, 1, 100)
    assert ok is False
    assert error == "Please guess between 1 and 100."


def test_validate_guess_negative_number():
    """Test that negative numbers are rejected."""
    ok, error = validate_guess(-50, 1, 100)
    assert ok is False
    assert error == "Please guess between 1 and 100."


def test_validate_guess_very_large_number():
    """Test that very large numbers are rejected when out of range."""
    ok, error = validate_guess(999999999999999, 1, 100)
    assert ok is False
    assert error == "Please guess between 1 and 100."


# ============================================================================
# EDGE CASE TESTS: Check Guess (Boundary Values)
# ============================================================================

def test_check_guess_at_boundaries():
    """Test that boundary values work correctly in win condition."""
    # Lower boundary
    outcome, message = check_guess(1, 1)
    assert outcome == "Win"
    
    # Upper boundary (example with 100)
    outcome, message = check_guess(100, 100)
    assert outcome == "Win"


def test_check_guess_just_outside_boundaries():
    """Test behavior when guess is just outside boundary values."""
    secret = 50
    
    # One above
    outcome, message = check_guess(51, secret)
    assert outcome == "Too High"
    
    # One below
    outcome, message = check_guess(49, secret)
    assert outcome == "Too Low"


# ============================================================================
# END-TO-END EDGE CASES: Full Input Validation Flow
# ============================================================================

def test_full_flow_negative_number_rejected():
    """Full flow: negative number parses but validation rejects it."""
    ok, guess, error = parse_guess("-50")
    assert ok is True
    assert guess == -50
    
    # Validation should catch it
    valid, val_error = validate_guess(guess, 1, 100)
    assert valid is False
    assert "Please guess between 1 and 100" in val_error


def test_full_flow_decimal_input_rejected_at_parse():
    """Full flow: decimal input fails at parse stage (graceful)."""
    ok, guess, error = parse_guess("50.5")
    assert ok is False
    assert guess is None
    assert error == "That is not a whole number."


def test_full_flow_valid_boundary_guess():
    """Full flow: valid boundary guess successfully processes."""
    ok, guess, error = parse_guess("100")
    assert ok is True
    assert guess == 100
    
    # Should be valid
    valid, val_error = validate_guess(guess, 1, 100)
    assert valid is True
    assert val_error is None
    
    # Should compare correctly
    outcome, message = check_guess(guess, 50)
    assert outcome == "Too High"
