import pytest
from function import suggest_improvement_plan, LECTURE_THRESHOLD, LAB_THRESHOLD, SUPPORT_THRESHOLD, CANVAS_THRESHOLD

def test_suggest_improvement_plan_below_threshold():
    # Test below thresholds
    suggestions = suggest_improvement_plan(LECTURE_THRESHOLD - 1, LAB_THRESHOLD - 1, SUPPORT_THRESHOLD - 1, CANVAS_THRESHOLD - 1)
    assert "Attend more lecture sessions to improve your overall attendance. You don't want to risk failing!" in suggestions
    assert "Increase your participation in lab sessions to boost your attendance. You don't want to risk failing!" in suggestions
    assert "Make sure to attend more support sessions for better engagement. You don't want to risk failing!" in suggestions
    assert "Spend more time on Canvas activities to meet the required attendance. You don't want to risk failing!" in suggestions

def test_suggest_improvement_plan_above_threshold():
    # Test above thresholds
    suggestions = suggest_improvement_plan(LECTURE_THRESHOLD + 1, LAB_THRESHOLD + 1, SUPPORT_THRESHOLD + 1, CANVAS_THRESHOLD + 1)
    assert "Great job, keep up the good work in your lectures!" in suggestions
    assert "Great job, keep up the good work in your lab work!" in suggestions
    assert "Great job, keep attending your support sessions!" in suggestions
    assert "Great job, keep up to date with your canvas engagement!" in suggestions

def test_suggest_improvement_plan_mixed():
    # Test mixed cases (just a couple examples for brevity)
    suggestions = suggest_improvement_plan(LECTURE_THRESHOLD + 1, LAB_THRESHOLD - 1, SUPPORT_THRESHOLD + 1, CANVAS_THRESHOLD - 1)
    assert "Great job, keep up the good work in your lectures!" in suggestions
    assert "Increase your participation in lab sessions to boost your attendance. You don't want to risk failing!" in suggestions
    assert "Great job, keep attending your support sessions!" in suggestions
    assert "Spend more time on Canvas activities to meet the required attendance. You don't want to risk failing!" in suggestions
