import csv
import os
from datetime import datetime
from typing import List, Dict

DATA_FILE = "expenses.csv"
FIELDNAMES = ["date", "description", "category", "amount"]


def init_data_file() -> None:
    """Ensure the CSV file exists and has a header row."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_expenses() -> List[Dict[str, str]]:
    """Load all expenses from the CSV file."""
    init_data_file()
    with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_expense(description: str, category: str, amount: float, date_str: str) -> None:
    """Append a new expense to the CSV file."""
    init_data_file()
    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(
            {
                "date": date_str,
                "description": description,
                "category": category,
                "amount": f"{amount:.2f}",
            }
        )


def prompt_for_expense() -> None:
    """Interactively ask the user for expense details and save them."""
    print("\n=== Add a New Expense ===")
    today_str = datetime.today().strftime("%Y-%m-%d")

    date_input = input(f"Date (YYYY-MM-DD) [default {today_str}]: ").strip()
    if not date_input:
        date_input = today_str

    # Validate date
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    category = input("Category (e.g., food, transport, rent): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    amount_str = input("Amount: ").strip()
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number (e.g., 12.50).")
        return

    save_expense(description, category, amount, date_input)
    print("Expense saved successfully!")


def list_expenses() -> None:
    """Print all expenses in a table-like format."""
    print("\n=== All Expenses ===")
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'Date':<12} {'Description':<25} {'Category':<15} {'Amount':>10}")
    print("-" * 65)
    for exp in expenses:
        print(
            f"{exp['date']:<12} "
            f"{exp['description']:<25.25} "
            f"{exp['category']:<15.15} "
            f"{exp['amount']:>10}"
        )


def show_summary_by_category() -> None:
    """Show total spent per category."""
    print("\n=== Summary by Category ===")
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals: Dict[str, float] = {}
    for exp in expenses:
        category = exp["category"]
        try:
            amount = float(exp["amount"])
        except ValueError:
            continue  # Skip malformed rows
        totals[category] = totals.get(category, 0.0) + amount

    print(f"{'Category':<20} {'Total Spent':>12}")
    print("-" * 35)
    for category, total in sorted(totals.items(), key=lambda x: x[0].lower()):
        print(f"{category:<20} {total:>12.2f}")


def print_menu() -> None:
    print("\n========== Expense Tracker ==========")
    print("1. Add a new expense")
    print("2. List all expenses")
    print("3. Show summary by category")
    print("4. Exit")
    print("=====================================")


def main() -> None:
    init_data_file()
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            prompt_for_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            show_summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
