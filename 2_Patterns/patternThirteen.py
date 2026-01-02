class Pattern:
    def patternThirteen(self, n):
        sum=0
        for i in range(n):
            for j in range(i+1):
                sum=sum+1
                print(sum, end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternThirteen(num)
