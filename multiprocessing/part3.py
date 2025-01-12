import multiprocessing

# Producer function: Places items in the queue
def producer(q):
    # Loop to produce 10 items
    for i in range(10):
        q.put(i)  # Places the integer `i` into the queue (this is the producer generating data)
    
    # After producing all items, the producer adds a special item (None) to signal the consumer to stop
    q.put(None)  # Graceful termination signal for the consumer to stop processing

# Consumer function: Retrieves and processes items from the queue
def consume(q):
    while True:
        try:
            # The consumer waits for an item from the queue
            item = q.get()  # Retrieves the next item from the queue (this blocks if the queue is empty)
            
            # If the retrieved item is None, it indicates no more data and the consumer should stop
            if item is None:  
                break  # Exit the loop (and the consumer process) when None is encountered
            
            print(item)  # Process the item (here, just printing it)
        
        except Exception as e:
            print(f"Error: {e}")  # If any error occurs (e.g., queue issues), print it

# Main block of code, executed only if the script is run as the main program
if __name__ == "__main__":
    # Create a multiprocessing queue to allow communication between processes
    queue = multiprocessing.Queue()  # This will hold data passed from producer to consumer
    
    # Create two separate processes: one for the producer and one for the consumer
    m1 = multiprocessing.Process(target=producer, args=(queue,))  # Process for producing data
    m2 = multiprocessing.Process(target=consume, args=(queue,))   # Process for consuming data
    
    # Start both processes
    m1.start()  # Start the producer process
    m2.start()  # Start the consumer process
    
    # Wait for both processes to complete their tasks
    m1.join()  # Wait for the producer process to finish
    m2.join()  # Wait for the consumer process to finish

# After the producer process finishes, the consumer is signaled to stop by receiving `None` from the queue
