import heapq
from Process import Process, GetPriority

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def Push(self, item:Process):
        heapq.heappush(self.heap, (item.priority, self.count, item))
        self.count += 1

    def Pop(self):
        return heapq.heappop(self.heap)[-1]

    def IsEmpty(self):
        return len(self.heap) == 0
    
class PriorityQueueArray:
    def __init__(self):
        self.queue: [Process] = []
        
    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def Push(self, item:Process):
        self.queue.append(item)
        pos = len(self.queue) - 1
    
        while (pos > 0 and GetPriority(self.queue[pos]) < GetPriority(self.queue[pos - 1])):
            self.swap(pos, pos - 1)
            pos += -1

    def Pop(self):
        if not self.IsEmpty():
            return self.queue.pop(0)
        else:
            return None

    def IsEmpty(self):
        return len(self.queue) == 0