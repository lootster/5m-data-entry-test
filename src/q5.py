def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if (type(num) in [int, float] and type(divisor) in [int, float]):
        return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

# Scenario 1
result1 = check_divisibility(10, 2)
print(result1)

# Scenario 2
result2 = check_divisibility(7, 3)
print(result2)
