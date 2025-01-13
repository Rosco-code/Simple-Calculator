#Prompt for user input.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# #Operators for calculation of 'a' with 'b'. This runs the two inputs through all 6 operator functions.
# print("Sum: {} + {} = {}".format(a,b,a+b))
# print("Difference: {} - {} = {}".format(a,b,a-b))
# print("Product: {} * {} = {}".format(a,b,a*b))
# print("Quotient: {} / {} = {}".format(a,b,a/b))
# print("Power: {}^{} = {}".format(a,b,a**b))
# print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))

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