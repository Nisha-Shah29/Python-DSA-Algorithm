class Dictionary:
    def listOfKeys(self, nums):
        #declaring empty list 
        keyList=[]
        for key,value in nums.items():
            if value>50:
                keyList.append(key)
        return keyList

        
if __name__=="__main__":
    obj=Dictionary()
    data={"pen":10, "book":100, "bag":70}
    result=obj.listOfKeys(data)
    print("List of keys when value is greater 50:", result)