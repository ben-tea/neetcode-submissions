class MinStack:

    def __init__(self):
        self.con = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        self.con.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[len(self.min_stack) - 1], val))


        

    def pop(self) -> None:
        self.con.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.con[len(self.con) - 1]
        

    def getMin(self) -> int:
        return self.min_stack[len(self.con) - 1]

        
