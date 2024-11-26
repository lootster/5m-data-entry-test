def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if type(x) not in [int, float] or type(y) not in [int, float]:
        return -1

    x, y = y, x
    print(f"x = {x}, y = {y}")


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Scenario 1
result = swap("Apple", 10)
if result == -1:
    print(result)

# Scenario 2
swap(9, 17)
