class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1 = int(num1.split("+")[0])
        n2 = int(num1.split("+")[1].replace("i", ""))
        
        n3 = int(num2.split("+")[0])
        n4 = int(num2.split("+")[1].replace("i", ""))

        num = (n1 * n3) - (n2 * n4)
        i = (n1 * n4) + (n2 * n3)
        return str(num) + "+" + str(i) + "i"
