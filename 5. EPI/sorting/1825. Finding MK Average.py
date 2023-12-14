class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream_m = deque()
        

    def addElement(self, num: int) -> None:
        self.stream_m.append(num) 
        if len(self.stream_m) > self.m:
            self.stream_m.popleft()


    def calculateMKAverage(self) -> int:
        if len(self.stream_m) < self.m:
            return -1
            
        arr = list(self.stream_m)
        heapq.heapify(arr)
        bottomk = [heapq.heappop(arr) for i in range(self.k)]
        leftover = [heapq.heappop(arr) for i in range(self.m-(self.k*2))]

        return int(sum(leftover)/len(leftover)) if len(leftover) > 0 else 0


        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
