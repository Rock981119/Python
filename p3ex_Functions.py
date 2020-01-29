# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

def add_subtract(first_number,second_number,operator):
    if operator.lower == "add":
        result = first_number + second_number
        return result
    elif operator.lower == "subtract":
        result = first_number - second_number
        return result

result1 = add_subtract(6,4,"add")
print(result1)

result2 = add_subtract(6,4,"subtract")
print(result2)

result3 = add_subtract(6,4,"divide")
print(result3)