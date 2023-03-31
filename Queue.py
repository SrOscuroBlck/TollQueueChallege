class nodeQueue(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

def arrival(queue, element):
    node = nodeQueue(element)
    node.data = element
    if queue.front is None:
        queue.front = node
    else:
        queue.rear.next = node
    queue.rear = node
    queue.size += 1
    
def departure(queue):
    data = queue.front.data
    queue.front = queue.front.next

    if queue.front is None:
        queue.rear = None
    
    queue.size -= 1
    return data

def emptyQueue(queue):
    return queue.front is None

def getSize(queue):
    return queue.size

def inFront(queue):
    return queue.front.data

def moveToRear(queue):
    data = departure(queue)
    arrival(queue, data)
    return data

def sweepQueue(queue):
    auxQueue = Queue()
    while not emptyQueue(queue):
        data = departure(queue)
        print(data)
        arrival(auxQueue, data)
        
    while not emptyQueue(auxQueue):
        data = departure(auxQueue)
        arrival(queue, data)
        
def sweepMovingToRear(queue):
    i = 0
    while i < queue.size:
        data = moveToRear(queue)
        print(data)
        i += 1