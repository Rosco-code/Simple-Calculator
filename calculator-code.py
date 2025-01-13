#Prompt for user input.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

#Operators for calculation of 'a' with 'b'.
print("Sum: {} + {} = {}".format(a,b,a+b))
print("Difference: {} - {} = {}".format(a,b,a-b))
print("Product: {} * {} = {}".format(a,b,a*b))
print("Quotient: {} / {} = {}".format(a,b,a/b))
print("Power: {}^{} = {}".format(a,b,a**b))
print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
