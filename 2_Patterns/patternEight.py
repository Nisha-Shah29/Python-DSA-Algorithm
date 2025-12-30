class Pattern:
    def patternEight(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end=" ")
            for k in range((2*n)-(2*i)-1):
                print("*", end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternEight(num)
