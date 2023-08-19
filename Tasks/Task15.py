#Using while loop, create lw() and create loop and print a's and create one more function b and create infinite loop.
#Call a and b both functions together in parallel
#Find a way to run a and b parallelly

import threading
import time

# Function to be executed in the loop 'a'
def lw():
    a = 0
    while a < 5:
        print("Function lw() - a:", a)
        a += 1
        time.sleep(1)

# Function to be executed in the loop 'b' (an infinite loop)
def b():
    while True:
        print("Function b() - Running in an infinite loop")

# Create and start the threads
thread_a = threading.Thread(target=lw)
thread_b = threading.Thread(target=b)

# Start both threads
thread_a.start()
thread_b.start()

# Wait for both threads to finish (this will not terminate for thread_b)
thread_a.join()
