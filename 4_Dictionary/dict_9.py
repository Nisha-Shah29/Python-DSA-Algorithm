class Dictionary:
    def countEvenOdd(self, data):
        evenCount=0
        oddCount=0
        for num in data.values():
            if num%2==0:
                evenCount=evenCount+1
            else:
                oddCount=oddCount+1
                
        print("No of even values:", evenCount)
        print("No of odd values:", oddCount)
        
if __name__=="__main__":
    obj=Dictionary()
    nums={"a":1, "b":2, "c":3, "d":4, "e":5}
    obj.countEvenOdd(nums)
