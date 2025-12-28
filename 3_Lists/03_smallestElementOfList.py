class ListSmallest:
    def getSmallest(self, myList):
        minimum=myList[0]
        for num in myList:
            if num<minimum:
                minimum=num
        return minimum
        
if __name__=="__main__":
    obj=ListSmallest()
    myList=[10,2,5,7,1]
    result=obj.getSmallest(myList)
    print("Smallest number of list entered is:", result)
    