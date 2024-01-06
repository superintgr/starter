import threading
import time

# Shared buffer among functions
shared_buffer = []

# Lock to synchronize access to the shared buffer
buffer_lock = threading.Lock()

# Number of functions monitoring the common thread
num_functions = 6

# Counter to track acknowledgment from functions
acknowledgment_counter = 0

def monitor_function(index):
    global acknowledgment_counter

    while True:
        # Simulating work in each function
        time.sleep(1)
        
        # Simulating external worker changing the buffer
        with buffer_lock:
            shared_buffer.append(f"Change by Function {index}")

        # Record relativistic timestamp
        timestamp = time.time()

        # Acknowledge the change
        with buffer_lock:
            acknowledgment_counter += 1

            # Check if all functions have acknowledged the change
            if acknowledgment_counter == num_functions:
                acknowledgment_counter = 0  # Reset counter
                print(f"All functions acknowledged the change at timestamp {timestamp}")
                # Perform further actions if needed

# Create and start monitoring threads
threads = []
for i in range(num_functions):
    thread = threading.Thread(target=monitor_function, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish (in this case, they run indefinitely)
for thread in threads:
    thread.join()
