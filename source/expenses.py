import csv
from datetime import datetime

# File to store expenses
expense_file = 'expenses.csv'

# Function to add an expense
def add_expense():
    # Get expense details from the user
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")

    # Open the expense file in append mode and write the expense details
    with open(expense_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    try:
        # Open the expense file in read mode and display each expense
        with open(expense_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")
    except FileNotFoundError:
        # Handle the case where the expense file does not exist
        print("No expenses found. Add some expenses first.")

# Function to get a summary of expenses
def get_summary():
    expenses = {}
    total_expense = 0.0

    try:
        # Open the expense file in read mode to calculate the summary
        with open(expense_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                total_expense += amount
                if category in expenses:
                    expenses[category] += amount
                else:
                    expenses[category] = amount

        # Display the total expense and the breakdown by category
        print(f"Total Expense: {total_expense}")
        for category, amount in expenses.items():
            print(f"Category: {category}, Amount: {amount}")
    except FileNotFoundError:
        # Handle the case where the expense file does not exist
        print("No expenses found. Add some expenses first.")

# Main menu
def main():
    while True:
        # Display the main menu and get the user's choice
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # Perform the selected action
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            get_summary()
        elif choice == '4':
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()