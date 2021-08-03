class Algorithm:
    def __init__(self, current):
        self.current = current
        self.previous = 0
        self.nums = [self.current]
    def loop(self):
        while self.current != 1.0:
            self.previous = self.current
            if self.current % 2 == 0:  
                self.current /= 2
            else:
                self.current *= 3
                self.current += 1
            self.nums.append(self.current)
        
            



