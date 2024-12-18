class Stack:
    def __init__(self) -> None:
        self.array = []
        
    def isEmpty(self):
        if self.array == []:
            return True
        return False
    
    def push(self, elem : int):
        self.array.append(elem)
        
    def top(self):
        return self.array[-1]
            
    def pop(self):
        return self.array.pop()
    
            
        
    # You can implement this class however you like