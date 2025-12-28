class ListSecondLargest:
    def getSecondLargest(self, myList):
        # Remove duplicates to avoid issues like [5, 5, 5]
        unique_nums = list(set(myList))

        # Check if we have at least two unique numbers
        if len(unique_nums) < 2:
            return None
            
        # Sort and return second largest
        unique_nums.sort()
        return unique_nums[-2]
        
if __name__=="__main__":
    obj=ListSecondLargest()
    myList=[10, 20, 4, 45, 99, 99, 5]
    result=obj.getSecondLargest(myList)
    print("Second largest number of list entered is:", result)
    