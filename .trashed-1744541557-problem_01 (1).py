num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

if num2 != 0:
    quotient_result = round(num1 / num2, 2)
else:
    quotient_result = "undefined"

print(f"The sum is {sum_result}")
print(f"The difference is {diff_result}")
print(f"The product is {prod_result}")
print(f"The quotient is {quotient_result}")