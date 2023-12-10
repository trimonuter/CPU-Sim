from PriorityQueue import PriorityQueue, PriorityQueueArray
from Process import Process
from random import randint, uniform
from time import time, sleep
import os
from termcolor import colored

# Miscelanneous Functions
clear = lambda: os.system('clear')

# Variables
maxPrio = 100
nMin = 1000
nMax = 30000
filenameHeap = 'bruteforce-heap.csv'
filenameArray = 'bruteforce-array.csv'

with open(filenameArray, 'w') as file:
    print(filenameArray)
    file.write("Processes,Time,CPUutil,Throughput,AvgWaiting\n")
    for n in range(nMin, nMax + 1, 1000):
        processes: [Process] = []
        for i in range(1, n + 1):
            burst = uniform(1 / 10000, 10 / 10000)
            priority = randint(1, 100000)
            processes.append(Process(f'Process_{i}', priority, burst))
        
        # Priority Queue - Heap Representation
        data = {}
        start = time()
        pqHeap = PriorityQueueArray()

        # 1 - Queue insertion
        for p in processes:
            pqHeap.Push(p)
            
            arrivalTime = time() - start
            data[p.name] = arrivalTime

        # 2 - Processing highest priority task
        CPUstart = time()
        process = 0
        waitingTime = 0
        totalBurst = 0
        while not pqHeap.IsEmpty():
            p: Process = pqHeap.Pop()
            
            process += 1
            currTime = (time() - start) + p.burstTime
            totalBurst += p.burstTime
            p.arrivalTime = data[p.name]
            waitingTime += (currTime - p.arrivalTime - p.burstTime)
                
        # 3 - Calculate time taken
        timeTaken = (time() - start) + totalBurst
        CPUutil = ((timeTaken - (CPUstart - start)) / timeTaken) * 100
        throughput = process / timeTaken
        avgWaitingTime =  waitingTime / process
        
        timeFormat = colored("{:.2f} sec".format(timeTaken), 'yellow') 
        CPUutilFormat = colored("{:.2f}%".format(CPUutil), 'yellow') 
        throughputFormat = colored("{:.0f} processes/sec".format(throughput), 'yellow') 
        avgWaitingTimeFormat = colored("{:.2f} sec".format(avgWaitingTime), 'yellow')
        
        print(f'Finished {colored(f"n = {n}", "green")}, Time = {timeFormat}, CPUutil = {CPUutilFormat}, throughput = {throughputFormat}, avgWait = {avgWaitingTimeFormat}')
        
        file.write("{},{:.2f},{:.2f},{:.0f},{:.2f}\n".format(n, timeTaken, CPUutil, throughput, avgWaitingTime))