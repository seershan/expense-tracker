# Expense Tracker

A simple command-line expense tracker written in Python. This tracker allows you to add, view, and delete expenses, storing the data in a CSV file.

## Features

- Add expenses with date, description, category, and amount.
- View all recorded expenses.
- Delete selected expenses.


## Installation

1. Clone the repository or download the script `expense_tracker.py`.

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

2. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `expense_tracker.py`.
3. Run the script using Python.

```bash
python expense_tracker.py
```

4. Follow the menu prompts to add, view, or delete expenses.

## How It Works

- The expenses are stored in a CSV file named `expenses.csv` in the same directory as the script.
- Each expense consists of the following fields:
  - Date (YYYY-MM-DD)
  - Description
  - Category
  - Amount

### Main Menu

```
Expense Tracker
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit
```

### Adding an Expense

- Prompts the user to enter the date, description, category, and amount.
- Saves the entered data to `expenses.csv`.

### Viewing Expenses

- Reads and displays all expenses from `expenses.csv`.

### Deleting an Expense

- Lists all expenses with an index number.
- Prompts the user to enter the number of the expense to delete.
- Deletes the selected expense from `expenses.csv`.

## Example

Here's a quick example of how to use the expense tracker:

1. Run the script:

```bash
python expense_tracker.py
```

2. Add an expense:

```
Enter the date (YYYY-MM-DD): 2024-06-12
Enter the description: Coffee
Enter the category: Food
Enter the amount: 3.50
Expense added successfully!
```

3. View expenses:

```
Date: 2024-06-12, Description: Coffee, Category: Food, Amount: $3.50
```

4. Delete an expense:

```
1. Date: 2024-06-12, Description: Coffee, Category: Food, Amount: $3.50
Enter the number of the expense to delete: 1
Expense deleted successfully!
```

## Acknowledgments

- Inspired by the need for a simple and effective way to track personal expenses.
- Thanks to the Python community for the excellent libraries and resources.
