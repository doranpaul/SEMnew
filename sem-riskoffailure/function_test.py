import pytest
from function import calculate_risk_of_failure


def test_normal_input():
    lec, lab, supp, can = 20, 15, 30, 40
    engagement_score = calculate_risk_of_failure(lec, lab, supp, can)
    expected_score = calculate_risk_of_failure(lec, lab, supp, can)  # Value calculated based on function
    assert engagement_score == expected_score, f"Expected {expected_score} but got {engagement_score}"

def test_invalid_input_non_number():
    with pytest.raises(ValueError, match="All input values must be numbers."):
        calculate_risk_of_failure("yes", 15, 30, 40)

def test_invalid_input_exceeds_total():
    with pytest.raises(ValueError, match="Input values must not exceed their respective totals."):
        calculate_risk_of_failure(40, 15, 30, 40)

def test_mixed_invalid_inputs():
    with pytest.raises(ValueError, match="All input values must be numbers."):
        calculate_risk_of_failure("no", -15, 60, 40)

def test_min_engagement_score():
    assert calculate_risk_of_failure(0, 0, 0, 0) == 0

def test_max_engagement_score():
    assert calculate_risk_of_failure(33, 22, 44, 50) == 100

def test_negative_values():
    with pytest.raises(ValueError, match="Input values must not exceed their respective totals."):
        calculate_risk_of_failure(-1, 15, 30, 40)