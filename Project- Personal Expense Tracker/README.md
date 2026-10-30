# Personal Expense Tracker

#### Video URL: <https://youtube.com/shorts/3dl-pVNvixl>

#### Description:
Personal Expense Tracker is a simple yet powerful Command Line Interface (CLI) application written in Python. It helps users manage their daily financial expenditures by allowing them to log expenses, categorize them, store data persistently in a CSV file, and view a formatted summary table along with total expenditure calculations.

### Motivation and Purpose
Managing personal finances is an essential skill, but full-fledged financial software can often feel overwhelming. This project provides a lightweight, terminal-based alternative where users can quickly record transactions without dealing with unnecessary complexity. The application ensures that financial data is preserved locally across sessions in a standard `expenses.csv` spreadsheet format.

### Features
1. **Expense Logging**: Users can add new expenses with a specified category (e.g., Food, Transport, Rent), numerical amount, and a brief description.
2. **Input Validation**: Ensures that amounts are positive, finite numbers and that categories are not left empty, preventing invalid data entry.
3. **Persistent Data Storage**: All transactions are automatically appended to a CSV file (`expenses.csv`).
4. **Formatted Expense Summary**: Displays all recorded expenses in a clean, tabular format using the `tabulate` library, complete with a total expenditure calculation.
5. **Interactive Menu**: The menu keeps returning after each action until the user chooses to exit.
6. **Automated Testing**: Unit tests implemented with `pytest` ensure that validation logic, file saving and loading, and formatting functions work as expected.

### How to Run
Install the dependencies, then start the program:

```
pip install -r requirements.txt
python project.py
```

To run the tests:

```
pytest test_project.py
```

The file `expenses.csv` is created automatically the first time an expense is added.

### File Structure and Functions

#### `project.py`
This is the main driver file for the application. It contains the interactive menu loop and the helper functions:
- `main()`: Shows the CLI menu in a loop, prompting users for input and calling the appropriate functions until the user chooses Exit.
- `validate_amount(amount_str)`: Converts a string to a positive floating-point number, rounds it to two decimal places, and returns it. Raises a `ValueError` for non-numeric input, zero, negative numbers, `nan`, and `inf`.
- `validate_category(category_str)`: Validates that the category is not empty (or only spaces) and formats it with a capital first letter for consistency. Raises a `ValueError` if the input is empty.
- `add_expense(category, amount, description, filename)`: Appends a validated expense record as a new row in the CSV file.
- `load_expenses(filename)`: Reads all expense records from the CSV file and returns them as a list of lists. Returns an empty list if the file does not exist yet.
- `format_expenses_table(expenses)`: Accepts a list of expense records, builds a grid table using `tabulate`, calculates the total of all expenses, and returns the complete formatted string.

#### `test_project.py`
This file contains automated `pytest` tests for the functions in `project.py`:
- `test_validate_amount()`: Tests valid inputs, rounding, and rejection of negative numbers, zero, text, `nan`, and `inf`.
- `test_validate_category()`: Verifies category formatting and rejection of empty or spaces-only strings.
- `test_format_expenses_table()`: Tests table rendering, the total calculation, and empty list handling.
- `test_add_and_load_expenses()`: Saves expenses to a temporary CSV file and checks that they load back correctly, including a description that contains a comma.
- `test_load_expenses_missing_file()`: Checks that a missing file gives an empty list instead of an error.

#### `requirements.txt`
Lists third-party Python dependencies required to run the project: `tabulate` for formatted output and `pytest` for automated testing.

#### `expenses.csv`
A comma-separated values file created automatically to store recorded expenses across application sessions.
