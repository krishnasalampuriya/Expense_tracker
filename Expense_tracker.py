import calendar
import datetime
from Expense import Expense

def main():
    budget = 2000
    # get expense from user
    expense = get_expense()
    # store the expense in file
    store_expense(expense)
    # give user the summary
    expense_summary(budget)

def get_expense():
    
    name = input("expense name : ")
    amount = float(input("expense amount : "))
    while True : 
        print("Select expense Category")
        categories = ['Food', 'Fun', 'work', 'home', 'Misc']
        for i , category in enumerate(categories):
            print(f"{i+1}. {category}")
        category = int(input())
        if category-1 in range(len(categories)):
            break
        else: print("Please Select a valid number")
        
    expense = Expense(name, amount, categories[category-1])
    return expense

def store_expense(expense):
    
    with open("expenses.csv",'a') as f :
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def expense_summary(budget):
    print("Your Expense Summary")
    summary_dict = {}
    # read all the file lines
    with open("expenses.csv",'r') as f:
        # for each line
        for line in f:
            # add the amount to the category key in dict
            name, amount, category = line.strip().split(',')
            amount = float(amount)
            if category in summary_dict:
                summary_dict[category] += amount
            else: summary_dict[category] = amount
            # print(f"{name},{amount},{category}")
        # iterate through dict and print total of each category
    total = 0
    for x in summary_dict:
        print(f"{x} : {summary_dict[x]}")
        total += float(summary_dict[x])

    print(f"Your total Expenses = {total}")
    
    remaining_budget = budget - total
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f"👉 Budget Per Day: ${daily_budget:.2f}")
    
    
    # print total remaining budget and this month's


if __name__ == "__main__":
    main()