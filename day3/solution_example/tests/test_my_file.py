# File: tests/test_my_file.py

from my_file import calculate_incidence, classify_risk

def test_calculate_incidence():
    assert calculate_incidence(5, 1e6, 'area51') == 0.5
    assert calculate_incidence(0, 1, 'area51') == 0
    assert calculate_incidence(0, 0, 'area51') is None

def test_classify_risk():
    assert classify_risk(None, 'area51') == "unknown"
    assert classify_risk(5,'area51') == "low"
    assert classify_risk(50, 'area51') == "low"
    assert classify_risk(100, 'area51') == "high" 