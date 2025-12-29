class ListEvenSum:
    def getEvenSum(self, myList):
        evenSum=0
        for num in myList:
            if num%2==0:
                evenSum=evenSum+num
        return evenSum

if __name__=="__main__":
    obj=ListEvenSum()
    myList=[1,2,4,8,3]
    result=obj.getEvenSum(myList)
    print("Sum of even number in a list is:" , result)