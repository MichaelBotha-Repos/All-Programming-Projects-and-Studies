##class QueueError(IndexError):  # Choose base class for the new exception.
##   pass

class Queue:
    def __init__(self):      
        self.QList = []
        
    def put(self, elem):
        self.QList.append(elem)  

    def get(self):
        if len(self.QList)>0:
            val = self.QList[0]
            del self.QList[0]
            return val
        else:
            raise QueueError
        
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self): 
        if len(self.QList) >0:
            return False
        else:
            return True
    

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

print(que.__dict__)
print(hasattr(que,'QList'))
print(que.QList)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
