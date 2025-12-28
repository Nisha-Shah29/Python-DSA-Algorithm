class ListSum:
    def getSum(self, myList):
        total=0
        for num in myList:
            total+=num
        return total
        
if __name__=="__main__":
    obj=ListSum()
    myList=[10,20,30,40,50]
    result=obj.getSum(myList)
    print("Sum of list entered is: ", result)
    