class ListCountEven:
    def getEvenCount(self, myList):
        count=0
        for num in myList:
            if num%2==0:
                count=count+1
        return count

if __name__=="__main__":
    obj=ListCountEven()
    myList=[1,2,3,4,5]
    result=obj.getEvenCount(myList)
    print("Number of even numbers in list is:" ,result)