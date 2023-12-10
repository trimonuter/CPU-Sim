from PriorityQueue import PriorityQueue, PriorityQueueArray
from Process import Process
from random import randrange
from time import time

maxPrio = 100
n = 500000

# pq = PriorityQueueArray()
# proc = [Process(f'Process {i}', randrange(1, maxPrio)) for i in range(1, n + 1)]

# start = time()

# for p in proc:
#     pq.Push(p)
    
# while not pq.IsEmpty():
#     # print(pq.Pop())
#     pq.Pop()
    
# end = time()

# totalTime = (end - start) * 1000
# formatTime = "{:.2f} ms".format(totalTime)
# print(f'\nTotal time taken: {formatTime}')

pq = PriorityQueue()
proc = [Process(f'Process {i}', randrange(1, maxPrio)) for i in range(1, n + 1)]

start = time()

for p in proc:
    pq.Push(p)
    
while not pq.IsEmpty():
    # print(pq.Pop())
    pq.Pop()
    
end = time()

totalTime = (end - start) * 1000
formatTime = "{:.2f} ms".format(totalTime)
print(f'\nTotal time taken: {formatTime}')