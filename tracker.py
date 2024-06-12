import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Description: {row[1]}, Category: {row[2]}, Amount: ${row[3]}")

def delete_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    expenses = []
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    for i, expense in enumerate(expenses):
        print(f"{i+1}. Date: {expense[0]}, Description: {expense[1]}, Category: {expense[2]}, Amount: ${expense[3]}")

    index = int(input("Enter the number of the expense to delete: ")) - 1

    if 0 <= index < len(expenses):
        del expenses[index]
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expense deleted successfully!")
    else:
        print("Invalid selection.")

def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
