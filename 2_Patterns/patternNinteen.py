class Pattern:
    def patternNinteen(self, n):
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or j==0 or j==n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternNinteen(num)