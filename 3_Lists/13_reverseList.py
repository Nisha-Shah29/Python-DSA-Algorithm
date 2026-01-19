class ReverseList:
    def __init__(self, myList):
        self.myList = myList

    def reverse_list(self):
        storeList = self.myList.copy()  # copy original list
        storeList.reverse()             # reverse copied list
        return storeList


# Main Program
n = int(input("Enter number of elements: "))
myList = list(map(int, input("Enter elements: ").split()))

obj = ReverseList(myList)
result = obj.reverse_list()

print("storeList =", result)
