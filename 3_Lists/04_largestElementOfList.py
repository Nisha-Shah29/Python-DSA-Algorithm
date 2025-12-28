class ListLargest:
    def getLargest(self, myList):
        maximum=myList[0]
        for num in myList:
            if num>maximum:
                maximum=num
        return maximum
        
if __name__=="__main__":
    obj=ListLargest()
    myList=[20,30,50,5,10]
    result=obj.getLargest(myList)
    print("Largest number of list entered is:", result)
    