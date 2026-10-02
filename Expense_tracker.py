print("===== EXPENSE TRACKER =====")
def get_expense_input(prompt, kind=float):
    while True:
        try:
            value = kind(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {kind.__name__}.")

            

expenses = []

number_of_expenses = get_expense_input("How many expenses do you want to enter? ", int)

for i in range(number_of_expenses):
    category = input(f"Enter category for expense {i + 1}: ")
    amount = get_expense_input(f"Enter amount for expense {i + 1}: $")

    expenses.append({
        "category": category,
        "amount": amount
    })
if not expenses:
   print("No expenses entered. Exiting the program.")
   exit()

total = sum(expense["amount"] for expense in expenses)
average = total / len(expenses)
highest = max(expenses, key=lambda expense: expense["amount"])
lowest = min(expenses, key=lambda expense: expense["amount"])

print("\n===== YOUR EXPENSES =====")

for i, expense in enumerate(expenses, 1):
    print(f"{i}. {expense['category']}: ${expense['amount']:.2f}")

print("\n===== RESULTS =====")
print(f"Total Expenses: ${total:.2f}")
print(f"Average Expense: ${average:.2f}")
print(f"Highest Expense: ${highest['amount']:.2f} ({highest['category']})")
print(f"Lowest Expense: ${lowest['amount']:.2f} ({lowest['category']})")

budget = get_expense_input("\nEnter your monthly budget: $", float)

if total > budget:
    over = total - budget
    print("\n⚠️ You are over budget!")
    print(f"You exceeded your budget by ${over:.2f}.")
else:
    remaining = budget - total
    print("\n✅ You are within budget!")
    print(f"You have ${remaining:.2f} left in your budget.")

print("\n===== THANK YOU =====")
print("Thank you for using the Expense Tracker!")