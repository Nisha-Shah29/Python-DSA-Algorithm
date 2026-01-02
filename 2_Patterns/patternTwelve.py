class Pattern:
    def patternTwelve(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1, end=" ")
            for k in range((2*n)-(2*(i+1))):
                print("  ",end="")
            for l in range(i+1):
                print(i+1-l, end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternTwelve(num)
