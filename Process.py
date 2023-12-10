class Process:
    def __init__(self, name, priority, burst):
        self.name = name
        self.priority = priority
        self.burstTime = burst        
        self.arrivalTime = 0

    def __repr__(self):
        return "{} (Priority: {}), Burst = {:.2f} ms".format(self.name, self.priority, self.burstTime * 1000)
    
    
def GetPriority(item: Process):
    return item.priority