class MyCalendarTwo:

    def __init__(self):
        self.arr = []

    def check(self, start: int, end: int) -> bool:
        count = 0
        for i in self.arr:
            if i[1] > start and i[0] < end:
                count += 1
                if count > 1:
                    return True
        return False

    def book(self, start: int, end: int) -> bool:
        for i in self.arr:
            if i[1] > start and i[0] < end:
                new_start = max(start, i[0])
                new_end = min(end, i[1])
                overlap = self.check(new_start, new_end)
                if overlap:
                    return False
                
        self.arr.append([start, end])
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
