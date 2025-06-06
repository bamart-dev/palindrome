import pytest
from main import palindrome


def test_palindrome_palindrome_returns_true():
    value = "kayak"

    result = palindrome(value)

    assert result


def test_palindrome_nonpalindrome_returns_false():
    value = "palindrome"

    result = palindrome(value)

    assert not result


def test_palindrome_palindrome_first_letter_capital_returns_true():
    value = "Mom"

    result = palindrome(value)

    assert result


def test_palindrome_nonpalindrome_first_letter_capital_returns_false():
    value = "Lake"

    result = palindrome(value)

    assert not result


def test_palindrome_mixed_case_palindrome_returns_true():
    value = "RaCeCaR"

    result = palindrome(value)

    assert result


def test_palindrome_mixed_case_nonpalindrome_returns_false():
    value = "HeLlO"

    result = palindrome(value)

    assert not result


def test_palindrome_empty_string_raises_error():
    value = ""

    with pytest.raises(ValueError):
        palindrome(value)


def test_palindrome_palindrome_int_input_returns_true():
    value = 1111

    result = palindrome(value)

    assert result


def test_palindrome_nonpalindrome__int_input_returns_false():
    value = "1212"

    result = palindrome(value)

    assert not result


def test_palindrome_palindrome_nonalphanum_string_returns_true():
    value = "#@@#"

    result = palindrome(value)

    assert result


def test_palindrome_nonpalindrome_nonalphanum_string_returns_false():
    value = "!$!$"

    result = palindrome(value)

    assert not result


def test_palindrome_onechar_input_returns_true():
    value1 = 0
    value2 = "1"
    value3 = "a"
    value4 = "B"

    result1 = palindrome(value1)
    result2 = palindrome(value2)
    result3 = palindrome(value3)
    result4 = palindrome(value4)

    assert result1
    assert result2
    assert result3
    assert result4
