#Create a generator function temperature_simulator that yields random temperature readings between -10 and 35 degrees Celsius every second.Write a loop that simulates this for 10 seconds and prints each temperature reading.


import random
import time
def temperature_simulator():
    while True:
        yield random.uniform(-10, 35)  
simulator = temperature_simulator()
for _ in range(10):
    temp = next(simulator)
    print(f"Temperature reading: {temp:.2f}°C")
    time.sleep(1) 
