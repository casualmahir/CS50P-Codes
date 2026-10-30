# Personal Expense Tracker: a command-line app that logs expenses to a CSV file
import csv
import math

from tabulate import tabulate

FILENAME = "expenses.csv"


def main():
    # Keep showing the menu until the user chooses Exit
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            category = input("Category (e.g., Food, Transport): ").strip()
            amount = input("Amount: ").strip()
            description = input("Description: ").strip()

            # Validate first, so nothing invalid is ever written to the file
            try:
                formatted_amount = validate_amount(amount)
                category = validate_category(category)
                add_expense(category, formatted_amount, description)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            expenses = load_expenses()
            print(format_expenses_table(expenses))

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


def validate_amount(amount_str):
    """Check that the amount is a positive number and round it to 2 decimals."""
    try:
        val = float(amount_str)
    except ValueError:
        raise ValueError("Amount must be a number.")

    # float() accepts "nan" and "inf", so reject those too
    if not math.isfinite(val) or val <= 0:
        raise ValueError("Amount must be greater than zero.")
    return round(val, 2)


def validate_category(category_str):
    """Check that the category is not empty and format it as 'Food'."""
    category_str = category_str.strip()
    if not category_str:
        raise ValueError("Category cannot be empty.")
    return category_str.capitalize()


def add_expense(category, amount, description, filename=FILENAME):
    """Add one expense as a new row at the end of the CSV file."""
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, description])


def load_expenses(filename=FILENAME):
    """Read every expense from the CSV file and return them as a list of rows."""
    expenses = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    expenses.append(row)
    except FileNotFoundError:
        # No file yet simply means no expenses yet
        pass
    return expenses


def format_expenses_table(expenses):
    """Turn the expense rows into a grid table with a total at the bottom."""
    if not expenses:
        return "No expenses recorded yet."

    headers = ["Category", "Amount ($)", "Description"]
    table = tabulate(expenses, headers=headers, tablefmt="grid")

    total = sum(float(item[1]) for item in expenses)
    summary = f"\nTotal Spent: ${total:.2f}"

    return table + summary


if __name__ == "__main__":
    main()
