class ROI:
   
    def __init__(self, expenses, income, total_investment, rate_of_return):
        self.expenses = expenses
        self.income = income
        self.rate_of_return = rate_of_return
        self.total_investment = total_investment
    
    def calculate_expenses(self):
        print(f"Your current expenses are {self.expenses}")
        change_expenses = input('Would you like to change or keep you expenses amount? ')
        if change_expenses.lower() == 'keep':
            return
        elif change_expenses.lower() == 'change':
            expense_amount = input('What is your new expense amount? ')
            if int(expense_amount) > 0:
                self.expenses = expense_amount
            else:
                print('please enter a valid amount.')
        else:
            print("Command invalid. Please enter 'change' or 'keep' ")
    
    def calculate_income(self):
        print( f'Your current income is {self.income}')
        change_income = input("would you like to change or keep your income amount? ")
        if change_income.lower() == 'keep':
            return
        elif change_income.lower() == 'change':
            income_amount = input('What is your new income amount? ')
            if int(income_amount) > 0:
                self.income = int(income_amount)
            else:
                print('please enter a valid amount.')
        else:
            print("Command invalid. Please enter 'change' or 'keep' ")
    
    def calculate_total_invests(self):
        print( f'Your current total invstment is {self.total_investment}')
        change_investment = input("would you like to change or keep your total investment amount? ")
        if change_investment.lower() == 'keep':
            return
        elif change_investment.lower() == 'change':
            investment_amount = input('What is your new income amount? ')
            if int(investment_amount) > 0:
                self.total_investment = investment_amount
            else:
                print('please enter a valid amount.')
        else:
            print("Command invalid. Please enter 'change' or 'keep' ")
   
    def calculate_roi(self):
        margin = int(self.income) - int(self.expenses)
        if margin != 0:
            self.rate_of_return = int(margin)/int(self.total_investment)
        else:
            self.rate_of_return = 0
        print(f"Your current ROI is {self.rate_of_return * 100}%.")
        
        
    
bigger_pockets = ROI(0, 0, 0, 0)

def run():
    while True:
        response = input("Would you like to change your 'income', 'expneses', 'total investment' or 'calculate roi'? ")
        
        if response.lower() == 'income':
            bigger_pockets.calculate_income()
        elif response.lower() == 'expenses':
            bigger_pockets.calculate_expenses()
        elif response.lower() == 'total investment':
            bigger_pockets.calculate_total_invests()
        elif response.lower() == 'calculate roi':
            bigger_pockets.calculate_roi()
        else:
            print('Enter a valid command')
run()

