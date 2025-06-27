import pandas as pd

expense_list = []

def add_expense():
  description = input("Enter the description of the expense. ")
  amount = float(input("Enter the cost of the expense. "))
  category = input("Enter the category of the expense. ")
  date = input("Enter the date of the expense. ")
  expenses = {
    "description": description,
    "amount": amount,
    "category": category,
    "date": date
  }
  expense_list.append(expenses)
  
def view_expenses(expense_list):
  df = pd.DataFrame(expense_list)
  print(df)
  
def get_summary(expense_list):
  lst = []
  for i in expense_list:
    lst.append(i["amount"])
  total = sum(lst)
  print(f"Your total amount is: ", total)
  average = total / len(lst)
  print(f"Your average expenses is: ", average)
  
  
def save_expenses_to_csv(expense_list):
  df = pd.DataFrame(expense_list)
  df.to_csv("expense_list.csv")
  
def load_expenses_from_csv():
  df = pd.read_csv("expense_list.csv")
  print(df)
  
def main_menu():
  menu =  """
  a: add expense
  v: view expenses
  g: get summary
  s: save expenses
  l: load expenses
  m: main menu
  """
  while True:
    print(menu)
    choice = input("Choose from the following expense menu. ")
    if choice == "a":
      add_expense()
    elif choice == "v":
      view_expenses(expense_list)
    elif choice == "g":
      get_summary(expense_list)
    elif choice == "s":
      save_expenses_to_csv(expense_list)
    elif choice == "l":
      load_expenses_from_csv()
    else:
      print("Invalid choice!!!")
    choice1 = input("Do you want to exit? (Y/N)")
    if choice1 == "Y":
      break


main_menu()



