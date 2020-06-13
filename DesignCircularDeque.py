class MyCircularDeque :

    def __init__(self, k) :
        
        self.Size = k

        self.Queue = []


    def insertFront(self, value) :
        
        if len(self.Queue) < self.Size :

            self.Queue.insert(0, value)

            return True

        return False


    def insertLast(self, value) :

        if len(self.Queue) < self.Size :

            self.Queue += [value]

            return True

        return False
        

    def deleteFront(self) :
        
        if len(self.Queue) != 0 :

            self.Queue.pop(0)

            return True

        return False


    def deleteLast(self) :
        
        if len(self.Queue) != 0 :

            self.Queue.pop()

            return True

        return False      


    def getFront(self) :
        
        if len(self.Queue) != 0 :

            return self.Queue[0]

        return -1


    def getRear(self) :
        
        if len(self.Queue) != 0 :

            return self.Queue[-1]

        return -1


    def isEmpty(self) :
        
        if len(self.Queue) == 0 :

            return True

        return False


    def isFull(self) :

        if len(self.Queue) == self.Size :

            return True

        return False
