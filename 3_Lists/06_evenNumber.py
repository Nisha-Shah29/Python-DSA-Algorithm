class ListEvenNumber:
    def getEvenNumber(self, myList):
        for num in myList:
            if num%2==0:
                print(num, end=" ")
       
        
if __name__=="__main__":
    obj=ListEvenNumber()
    myList=[1,2,4,6,9]
    obj.getEvenNumber(myList)
    