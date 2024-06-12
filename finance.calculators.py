# 10 -012 Capstone Project
import math

# Print calculation option 
introduction = """ 
investment - to calculate the amount of interestyou'll earn on your interest 
bond       - to calculate the amount you'll have to pay on a home loan \n
Enter either 'investment' or 'bond' from the menu abov to proceed:"""

# Pre-define two possibilities for user input
paths = ["investment", "bond"]

# Create while loop to prompt selection of investment and/ or bond 
    # Request selection from user
    # Convert input to lowercase to ensure case insensitivity 
       # If 'investment,' prompt input of deposit, interest percent and years.
            # Create while loops to ensure a numerical inputs for each option
                # If numeric, continue
while True:
    Query_path = input(f"{introduction : < 76}")
    query_path = Query_path.lower()
    if query_path in paths:  
        if query_path == "investment":
            while True: 
                deposit = input("How much would you like to deposit? ") # If not, re-enter
                if deposit.isnumeric():
                    break
                else: 
                    print("Please be sure to enter a number (e.g 5000):")
            while True:
                interest_percent= input("What is the percentage of your interest rate? ") #if not, reenter
                if interest_percent.isnumeric():
                    break
                else:
                    print("Please be sure to enter a number (e.g. 8% = '8')")
            interest_percent_div100 = int(interest_percent) / 100
            while True:
                years = input("""{For how long do you plan on investing?   
            (Please give your answer in years) """) #if not, reenter
                if years.isnumeric():
                    break
                else:
                    print("Please be sure to enter a number (e.g 5 years = '5')")

            # Pre-define two possibilties for user input
            interest_paths = ["simple", "compound"]

            # Create while loop to prormpt selction of either 'simple,' or 'compound.'
                 # Request selection from user 
                 # Convert input to lowercase to ensure case insensitivity
                    # Calculate and display 'simple,' else 'compound' output to two decimal places
            while True: 
                inTerest = input("""Would you prefer a simple or compound interest plan?
                (Please type your answer)  """)
                interest = inTerest.lower()
                if interest in interest_paths:
                    if interest == "simple":
                        simple_output_sum = float(deposit) * (1 + interest_percent_div100 * float(years))
                        simple_output = round(simple_output_sum, 2)
                        print(F"{"You will pay a total of £"} {simple_output} {"with interest rates applied."}") 
                        break
                    elif interest == "compound":
                        compound_output = float(deposit) * math.pow((1 + interest_percent_div100 ) ,float(years))
                        # ROUND FUNCTION ISNT WORKING
                        print(F"{"You will pay a total of £"} {round (compound_output, 2)} {" with interest rates applied."}")
                        break
        
        # Else, if 'bond:'
            # Create while loops to ensure numerical inputs of house value, annual interest and repayment time
                 # If Numeric, continue
            # Calculate monthly interest 
            # Calculate and display bond output to two decimal places   
        elif query_path == "bond":
            while True:
                house_value = input("What is the current value of your house? ")
                if house_value.isnumeric():
                    break
                else:
                    print("Please be sure to enter a number (e.g. 500000)")
            while True:
                annual_interest = input("What is your annual interest rate? ") 
                if annual_interest.isnumeric():
                    break
                else:
                    print("PLease be sure to enter a number (e.g. 8% = '8')")
            monthly_interest = (float(annual_interest) / 100) / 12
            while True:
                time_months = input("Over how many months do you plan to repay your bond?")
                if time_months.isnumeric():
                    break
                else: 
                    print("Please be sure to enter a number (e.g. 18) ")
            bond_output = float(monthly_interest) * float(house_value) / (1 - (1 + float(monthly_interest)) ** ( - int(time_months)))
            print(F"{"You will need to pay £"} {round (bond_output, 2)} { " per month."}")
            break 
        
    else:
        print(F"ERROR: This field requires you to type 'investment' or 'bond.' Please try again - ")
              