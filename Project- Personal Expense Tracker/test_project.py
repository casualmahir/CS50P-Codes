import pytest

from project import (
    add_expense,
    format_expenses_table,
    load_expenses,
    validate_amount,
    validate_category,
)


def test_validate_amount():
    assert validate_amount("10.5") == 10.5
    assert validate_amount("50") == 50.0
    assert validate_amount("3.14159") == 3.14  # rounded to 2 decimals
    with pytest.raises(ValueError):
        validate_amount("-5")
    with pytest.raises(ValueError):
        validate_amount("0")
    with pytest.raises(ValueError):
        validate_amount("abc")
    with pytest.raises(ValueError):
        validate_amount("nan")
    with pytest.raises(ValueError):
        validate_amount("inf")


def test_validate_category():
    assert validate_category("food") == "Food"
    assert validate_category("TRANSPORT") == "Transport"
    assert validate_category("  rent  ") == "Rent"
    with pytest.raises(ValueError):
        validate_category("")
    with pytest.raises(ValueError):
        validate_category("   ")


def test_format_expenses_table():
    sample_data = [["Food", "15.0", "Lunch"], ["Transport", "5.0", "Bus"]]
    output = format_expenses_table(sample_data)
    assert "Food" in output
    assert "Total Spent: $20.00" in output
    assert format_expenses_table([]) == "No expenses recorded yet."


def test_add_and_load_expenses(tmp_path):
    # tmp_path is a temporary folder, so the real expenses.csv is never touched
    file = str(tmp_path / "test_expenses.csv")
    add_expense("Food", 15.0, "Lunch, with friends", filename=file)
    add_expense("Transport", 5.5, "Bus", filename=file)
    assert load_expenses(filename=file) == [
        ["Food", "15.0", "Lunch, with friends"],
        ["Transport", "5.5", "Bus"],
    ]


def test_load_expenses_missing_file(tmp_path):
    assert load_expenses(filename=str(tmp_path / "missing.csv")) == []
