from PriorityQueue import PriorityQueue, PriorityQueueArray
from Process import Process
from random import randrange
from time import time
import os
from termcolor import colored

# Miscelanneous Functions
clear = lambda: os.system('clear')

# Variables
maxPrio = 1000
nMax = 100000
filename = 'bruteforce-heap.csv'

with open(filename, 'w') as file:
    for n in range(1000, nMax + 1, 1000):
        processes: [Process] = [Process(f'Process_{i}', randrange(1, maxPrio), 0) for i in range(1, n + 1)]
        data = {}
        start = time()
        
        # Priority Queue - Heap Representation
        pqHeap = PriorityQueue()

        # 1 - Queue insertion
        for p in processes:
            pqHeap.Push(p)
            
            arrivalTime = time() - start
            data[p.name] = arrivalTime

        # 2 - Processing highest priority task
        while not pqHeap.IsEmpty():
            p: Process = pqHeap.Pop()
            p.arrivalTime = data[p.name]
                
        # 3 - Calculate time taken
        end = time()
        timeTaken = (end - start)
        timeFormat = colored("{:.2f} sec".format(timeTaken), 'yellow') 
        print(f'Finished {colored(f"n = {n}", "green")}, Time = {timeFormat}')
        
        file.write("{},{:.2f}\n".format(n, timeTaken))