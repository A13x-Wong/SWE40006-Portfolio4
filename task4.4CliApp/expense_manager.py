import os
import sqlite3
from datetime import datetime

DATABASE = os.getenv("EXPENSE_DB", "expenses.db")


def get_connection():
    return sqlite3.connect(DATABASE)


def initialise_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def print_header():
    print("\n" + "=" * 58)
    print("              PERSONAL EXPENSE MANAGER CLI")
    print("=" * 58)


def add_expense():
    print("\n--- Add New Expense ---")

    description = input("Description: ").strip()

    if not description:
        print("Error: Description cannot be empty.")
        return

    print("\nCategories")
    print("1. Food")
    print("2. Transport")
    print("3. Shopping")
    print("4. Education")
    print("5. Entertainment")
    print("6. Bills")
    print("7. Other")

    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Shopping",
        "4": "Education",
        "5": "Entertainment",
        "6": "Bills",
        "7": "Other"
    }

    category_choice = input("Select category (1-7): ").strip()

    if category_choice not in categories:
        print("Error: Invalid category.")
        return

    try:
        amount = float(input("Amount (RM): ").strip())

        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return

    except ValueError:
        print("Error: Amount must be a number.")
        return

    category = categories[category_choice]
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO expenses
        (description, category, amount, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (description, category, amount, created_at)
    )

    conn.commit()
    conn.close()

    print("\nExpense added successfully.")


def view_expenses():
    conn = get_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY id ASC"
    ).fetchall()

    conn.close()

    print("\n--- Expense History ---")

    if not expenses:
        print("No expenses recorded.")
        return

    print(
        f"{'ID':<5}"
        f"{'Description':<20}"
        f"{'Category':<16}"
        f"{'Amount':>12}"
    )

    print("-" * 58)

    total = 0

    for expense in expenses:
        expense_id = expense[0]
        description = expense[1]
        category = expense[2]
        amount = expense[3]

        total += amount

        print(
            f"{expense_id:<5}"
            f"{description[:18]:<20}"
            f"{category:<16}"
            f"RM {amount:>8.2f}"
        )

    print("-" * 58)
    print(f"{'Total Spending':<41} RM {total:>10.2f}")


def spending_summary():
    conn = get_connection()

    expenses = conn.execute(
        "SELECT amount FROM expenses"
    ).fetchall()

    category_totals = conn.execute(
        """
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
        """
    ).fetchall()

    conn.close()

    print("\n--- Spending Summary ---")

    if not expenses:
        print("No expenses available for analysis.")
        return

    amounts = [expense[0] for expense in expenses]

    total = sum(amounts)
    highest = max(amounts)
    lowest = min(amounts)
    average = total / len(amounts)

    print("\nSpending by Category")
    print("-" * 40)

    for category, category_total in category_totals:
        print(f"{category:<22} RM {category_total:>10.2f}")

    print("-" * 40)

    print(f"Number of Expenses : {len(amounts)}")
    print(f"Total Spending     : RM {total:.2f}")
    print(f"Average Expense    : RM {average:.2f}")
    print(f"Highest Expense    : RM {highest:.2f}")
    print(f"Lowest Expense     : RM {lowest:.2f}")


def delete_expense():
    view_expenses()

    try:
        expense_id = int(
            input("\nEnter expense ID to delete: ").strip()
        )

    except ValueError:
        print("Error: Expense ID must be a number.")
        return

    conn = get_connection()

    expense = conn.execute(
        "SELECT id FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()

    if expense is None:
        conn.close()
        print("Error: Expense ID does not exist.")
        return

    conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()

    print("Expense deleted successfully.")


def show_menu():
    print_header()

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Spending Summary")
    print("4. Delete Expense")
    print("5. Exit")


def main():
    initialise_database()

    while True:
        show_menu()

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            spending_summary()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("\nExpense Manager closed successfully.")
            print("=" * 58)
            break

        else:
            print("\nError: Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()