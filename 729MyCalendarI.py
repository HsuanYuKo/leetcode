class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        # self.arr.append([start, end])
        for i in self.arr:
            if i[1] > start and i[0] < end:
                return False
        self.arr.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
