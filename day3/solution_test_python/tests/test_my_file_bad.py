# File: tests/test_my_file_bad.py

from my_file_bad import calculate_incidence, classify_risk

def test_calculate_incidence():
    assert calculate_incidence(5, 1e6) == 0.5
    assert calculate_incidence(0, 1) == 0
    assert calculate_incidence(0, 0) is None

def test_classify_risk():
    assert classify_risk(None) == "unknown"
    assert classify_risk(5) == "low"
    assert classify_risk(50) == "low"
    assert classify_risk(100) == "high" 