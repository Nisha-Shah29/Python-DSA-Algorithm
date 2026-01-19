class CheckSorted:
    def __init__(self, myList):
        self.myList = myList

    def is_sorted(self):
        for i in range(len(self.myList) - 1):
            if self.myList[i] > self.myList[i + 1]:
                return False
        return True


# Main Program
if __name__=="__main__":
    n = int(input("Enter number of elements: "))
    myList = list(map(int, input("Enter elements: ").split()))

    obj = CheckSorted(myList)
    print(obj.is_sorted())
