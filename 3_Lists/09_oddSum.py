class ListOddSum:
    def getOddSum(self, myList):
        oddSum=0
        for num in myList:
            if num%2!=0:
                oddSum=oddSum+num
        return oddSum

if __name__=="__main__":
    obj=ListOddSum()
    myList=[2,5,6,11,20,25]
    result=obj.getOddSum(myList)
    print("Sum of odd number in a list is:" ,result)