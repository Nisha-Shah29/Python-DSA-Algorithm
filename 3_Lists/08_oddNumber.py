class ListOdd:
    def getOddNumber(self, myList):
        for num in myList:
            if num%2!=0:
                print(num, end=" ")

if __name__=="__main__":
    obj=ListOdd()
    myList=[2,5,6,11,20,25]
    obj.getOddNumber(myList)