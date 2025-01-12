# Define the list of numbers
numbers = [1, 2, 3, 4]

# Example 1: Using a predefined function with map()
def square(x):
    return x ** 2  # This function squares the given number

# Use map() to apply the square function to every element in the numbers list
squared_numbers = map(square, numbers)

# Convert the map object to a list and print it
print(list(squared_numbers))  # Output: [1, 4, 9, 16]

# Example 2: Using a lambda function with map()
# Lambda function to square a number
squared_numbers_lambda = map(lambda x: x ** 2, numbers)

# Convert the map object to a list and print it
print(list(squared_numbers_lambda))  # Output: [1, 4, 9, 16]

# Explanation of how map works:
# - map() applies the function (either a predefined function or a lambda function) to each element in the iterable (numbers list).
# - It returns a map object, which is an iterator. We convert it to a list to display the results.

# Example 3: Using multiple iterables with map()
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use map() to add corresponding elements from list1 and list2
# The lambda function takes two arguments (x, y) and adds them together.
result = map(lambda x, y: x + y, list1, list2)

# Convert the map object to a list and print the result
print(list(result))  # Output: [5, 7, 9]

# Explanation of how map works with multiple iterables:
# - When you pass multiple iterables, the function provided to map() must accept the same number of arguments as there are iterables.
# - In this case, we added corresponding elements from list1 and list2 (e.g., 1+4, 2+5, 3+6).

# Conclusion:
# - map() is useful when you want to apply the same operation to every element in one or more iterables.
# - It helps reduce the need for explicit loops and can be more efficient with large datasets because it returns an iterator, not a full list.
# - You can use predefined functions or lambda functions with map(), making it versatile and concise.
