def main():
    print(f"Running Expense Tracker!")

    # Get user input for expense.
    get_user_expense()


    #Write their expense to a file.
    save_expense_to_file()


    #Read file and summarize expenses.
    summarize_expenses()
  

def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, {expense_amount}")

    expense_categories = ["🥞Food", "🏠Home", "💼Work", "🎊Fun", "✨Misc", "🩺Health"]


    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        break


def save_expense_to_file():
    print(f"Saving User Expense")
    

def summarize_expenses():
    print(f"Summarizing User Expense")
 



if __name__ == "__main__":
    main()
