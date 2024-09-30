class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.arr) < self.maxSize:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            pop_num = self.arr[len(self.arr) - 1]
            self.arr.pop(len(self.arr) - 1)
            return pop_num


    def increment(self, k: int, val: int) -> None:
        if k > len(self.arr):
            for i in range(0, len(self.arr)):
                self.arr[i] += val
        else:
            for i in range(0, k):
                self.arr[i] += val
    


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
