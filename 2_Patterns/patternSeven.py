class Pattern:
    def patternSeven(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end=" ")
            for k in range((2*i)+1):
                print("*", end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternSeven(num)
