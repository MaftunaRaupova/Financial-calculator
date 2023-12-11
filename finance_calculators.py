""" The code asks the user investment type. 
Depending the option user chooses it will calculate the outcome. 
Invesment types: bond or investment
Options are 'simple' or 'compound' """

import math

investment = "Investment- to calculate the amount of the interest you'll earn on your investment"
print(investment)
bond = "Bond- to calculate the amount you'll have to pay on a home loan"
print(bond)
print()
user_input = input("Enter either 'investment' or  'bond' from the menu above to proceed: ")

if user_input.lower() != "bond" and user_input.lower() != "investment" : 
    print("Wrong entry, please check your response. ")
    exit

if user_input.lower() == "investment" :
    deposit = int(input("The amount of deposit: "))
    interest_rate = int(input("The interest rate (as percentage): "))/100
    length_year = int(input("The number of years planning to invest: "))
    
    interest_option = input("Would you like 'simple' or 'compound' interest: ")
    if interest_option.lower() == "simple" : 
        s_total_amount = deposit * (1 + interest_rate * length_year)
        print(int(s_total_amount))
    if interest_option.lower() == "compound" :
        c_total_amount = deposit * math.pow((1 +interest_rate), length_year)
        print(int(c_total_amount))

if user_input.lower() == "bond" :
    house_value = int(input("The value of the house: ")) 
    interest_rate = int(input("Enter the interest rate: "))/(100*12)
    length_months = int(input("Enter the number of the months to repay the bond: "))
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate)**(-length_months))
    print(int(repayment))

