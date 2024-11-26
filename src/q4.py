def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if isinstance(s, str):
        return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Scenario 1
result1 = string_reverse("Hello World")
print(result1)

# Scenario 2
result2 = string_reverse("Python")
print(result2)
