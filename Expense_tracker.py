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
    input("Enter expense name: ")

def save_expense_to_file():
    print(f"Saving User Expense")
   

def summarize_expenses():
    print(f"Summarizing User Expense")




if __name__ == "__main__":
    main()
