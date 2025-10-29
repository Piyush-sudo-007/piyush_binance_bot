import pytest
from src.validation import validate_symbol, validate_positive_number

def test_validate_symbol_ok():
    assert validate_symbol('BTCUSDT') == 'BTCUSDT'

def test_validate_symbol_bad():
    with pytest.raises(ValueError):
        validate_symbol('bad symbol!')

def test_validate_positive_number_ok():
    assert validate_positive_number('0.1') == 0.1

def test_validate_positive_number_bad():
    with pytest.raises(ValueError):
        validate_positive_number('-1')
