import multiprocessing

# creating a function 
def square(n):
    return n**2

if __name__ == "__main__":

    # beginnig a process
    with multiprocessing.Pool(processes = 4) as pool:
        # here pool func returns a list of results/ or we can say the bulk results of the function square

        # now we use map function to apply the function square to each element in the list [1,2,3,4, 5,6,7,8,9,10]
        results = pool.map(square, [1,2,3,4,5,6,7,8,9,10])
        # here it will take the data one by one and then process the data through the function square and then return the result in the list
        print(results)
    