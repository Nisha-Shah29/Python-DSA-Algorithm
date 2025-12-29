class ListCountOdd:
    def getOddCount(self, myList):
        count=0
        for num in myList:
            if num%2!=0:
                count=count+1
        return count

if __name__=="__main__":
    obj=ListCountOdd()
    myList=[1,3,5,9,10,12]
    result=obj.getOddCount(myList)
    print("Number of odd numbers in list is:" ,result)