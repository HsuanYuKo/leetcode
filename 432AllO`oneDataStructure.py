class AllOne:

    def __init__(self):
        self.dict = {}

    def inc(self, key: str) -> None:
        if key not in self.dict:
            self.dict[key] = 1
        else:
            self.dict[key] += 1

    def dec(self, key: str) -> None:
        if self.dict[key] == 1:
            del self.dict[key]
        else:
            self.dict[key] -= 1

    def getMaxKey(self) -> str:
        Max = 0
        Max_key = ""
        for key, value in self.dict.items():
            if value > Max:
                Max_key = key
                Max = value
        return Max_key

    def getMinKey(self) -> str:
        Min = 999999
        min_key = ""
        for key, value in self.dict.items():
            if value < Min:
                min_key = key
                Min = value
        return min_key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
