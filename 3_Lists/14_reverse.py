class ReverseList:
    def __init__(self, myList):
        self.myList = myList

    def reverse_list(self):
        self.myList.reverse()   # reverses the list in place


# Main Program
n = int(input("Enter number of elements: "))
myList = list(map(int, input("Enter elements: ").split()))

obj = ReverseList(myList)
obj.reverse_list()

print(myList)
