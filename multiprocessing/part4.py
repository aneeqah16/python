import multiprocessing

# Function that squares the element at the given index of the shared array
def square(index, value):
    value[index] = value[index]**2  # Square the element at index `index` in the shared array `value`

if __name__ == "__main__":
    # Create a shared array `arr` with integer values
    # "i" specifies that the array contains integers
    arr = multiprocessing.Array("i", [2, 3, 4, 5, 6, 7, 8])  
    
    # List to hold the processes
    process = list()

    # Loop over each element in the array and create a new process for each element
    for i in range(len(arr)):
        # Create a new process, passing the index and the shared array `arr` as arguments
        m = multiprocessing.Process(target=square, args=(i, arr))
        
        # Append the created process to the process list
        process.append(m)
        
        # Start the process, which will square the value at index `i` in the shared array
        m.start()

    # Wait for all the processes to finish by calling `join` on each one
    for m in process:
        m.join()  # Ensures that the main program waits for the process to complete
    
    # Convert the shared array to a list and print the updated values (squared values)
    print(list(arr))  # After all processes complete, the array will contain squared values
