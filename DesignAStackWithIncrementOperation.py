class CustomStack :

    def __init__(self, maxSize) :
        
        self.maxSize = maxSize

        self.Stack = []
        

    def push(self, x) :
        
        if len(self.Stack) < self.maxSize :
            
            self.Stack += [x]


    def pop(self) :
        
        if len(self.Stack) > 0 :

            top = self.Stack[-1]

            self.Stack.pop()

            return top

        else :

            return -1
        

    def increment(self, k, val) :

        if k < len(self.Stack) :

            for i in range(k) :

                self.Stack[i] += val

        
        else :

            for i in range(len(self.Stack)) :

                self.Stack[i] += val


St = CustomStack(3)

St.push(1)

print(St.Stack)

St.push(2)

print(St.Stack)

St.push(3)

print(St.Stack)

St.push(4)

print(St.Stack)

print(St.pop())

print(St.Stack)

St.increment(2, 100)

print(St.Stack)