import logging as lg

# Setting up logging configuration
# The log messages will be stored in a file named "test2.log" with a logging level of DEBUG.
# The format specifies the log message with the timestamp.
lg.basicConfig(filename="test2.log", level=lg.DEBUG, format="%(asctime)s %(message)s")

# Shutting down logging at the end to ensure all messages are written to the log file
lg.shutdown()

# Creating a mixed list with integers, strings, and a nested list
l = [1, 2, 3, 4, 5, 6, 7, [5, 6, 7], "aneeqah", "ashraf"]

# Two empty lists to store integers and strings separately
l1_int = list()  # This will hold all integers
l2_str = list()  # This will hold all strings

# Start logging to track the flow of the program
lg.debug("Logging started")

# Iterate through the elements of the list 'l'
for i in l:
    # Log each iteration with the current value of 'i'
    lg.info(f"Iterating the list, current value: {i}")

    # Check if the current item is a list
    if type(i) == list:
        lg.info("Item is a list, iterating through its elements")

        # Iterate through the elements of the nested list
        for j in i:
            lg.info(f"Checking if the nested element is of type integer: {j}")

            # Check if the nested item is an integer
            if type(j) == int:
                lg.info(f"Found an integer in the nested list: {j}")
                l1_int.append(j)  # Append the integer to the list of integers
    # If the current item is an integer, append it to the integer list
    elif type(i) == int:
        lg.info(f"Found an integer: {i}")
        l1_int.append(i)
    else:
        # If the item is a string, append it to the string list
        if type(i) == str:
            lg.info(f"Found a string: {i}")
            l2_str.append(i)

# Log the final result after processing the list
lg.info(f"Extracted integers: {l1_int}")
lg.info(f"Extracted strings: {l2_str}")
