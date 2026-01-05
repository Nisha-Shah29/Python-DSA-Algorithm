class Dictionary:
    def displaySum(self, data):
        sumValue = sum(data.values())
        return sumValue

if __name__=="__main__":
    obj=Dictionary()
    sales={"jan":2000, "feb":3000, "march":2500}
    result=obj.displaySum(sales)
    print("Sum of all values:", result)