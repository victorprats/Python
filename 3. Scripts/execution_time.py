# https://docs.python.org/3/library/time.html
import time


start_time = time.process_time()

# your code

end_time = time.process_time()

# Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process. 
print("Total execution time (seconds): {}".format(end_time - start_time)) 

