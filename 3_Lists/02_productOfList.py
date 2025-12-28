class ListProduct:
    def getProduct(self, myList):
        product=1
        for num in myList:
            product=product*num
        return product
        
if __name__=="__main__":
    obj=ListProduct()
    myList=[10,20,30,40,50]
    result=obj.getProduct(myList)
    print("Product of list entered is: ", result)
    