class MaxStack:
    def __init__(self): # Fill this in.
        self.data = []
        self.maxVals = []

    def push(self, val): # Fill this in.
        if self.maxVals and val >= self.maxVals[-1]:
            self.maxVals.append(val)
        else:
            self.maxVals.append(val)
        self.data.append(val)


    def pop(self): # Fill this in.
        if self.data:
            top = self.data.pop()
            if top == self.maxVals[-1]:
                self.maxVals.pop()
            return top
        else:
            return 0
    
    def max(self): # Fill this in.
        if self.maxVals:
            return self.maxVals[-1]
        else:
            return 0

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2