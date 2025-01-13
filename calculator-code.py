#Prompt for user input.

#Function handling prompts to receive inputs for numbers to operate on, and the choiuce of which operators to use.
def prompt_menu():
    
    #
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    #Print statement to show user what operators are available.
    print("""
        Choose an operator from the list below by entering the corresponding number.
        1. Addittion
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exponentiation
        6. Division with a remainder
        """)
    
    #Setting input statement for operator
    op = int(input("Enter the number for the desired operator: "))
    return a, b, op




#Function containing equations to calculate inputs from 'def prompt_menu()'
def calculations():
    a, b, op = prompt_menu()
#If and elif statements to determine what operator to use based on user input for desired operator.
    if op == 1:
        print("Sum: {} + {} = {}".format(a,b,a+b))

    elif op == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))

    elif op == 3:
        print("Product: {} * {} = {}".format(a,b,a*b))

    elif op == 4:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Dvision by 0 not possible.")

    elif op == 5:
        print("Power: {}^{} = {}".format(a,b,a**b))

    elif op == 6:
        try:
            print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
        except:
            print("Dvision by 0 not possible.")

    #Else statement incase input statement for operator is not an available option.
    else:
        print("Invalid Choice. Please select from list.")
    
    #Calls calculator loop function after printing results to ask user if they want to run another calculation.
    calculator_loop()



#Function run after 'def calculations' to determine whether the user wants to run another calculation.
def calculator_loop():
    choice = input("Do you want to run another calculation? (Y , N): ")
    if choice.upper() == "Y":
        calculations()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input!")
        calculator_loop()




#Calling of calculations() to trigger app running.
calculations()