import threading
import time

def timer_function(delay):
    print("Timer started...")
    time.sleep(delay)
    print("Timer expired!")


    
delay = int(input("Enter the delay time (in seconds): "))
    
timer_thread = threading.Thread(target=timer_function, args=(delay,))
timer_thread.start()
print('after thread')

# Optionally, you can join the timer_thread if you want the main thread to wait for it to finish.
# timer_thread.join()


 
