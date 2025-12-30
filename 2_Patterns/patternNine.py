class Pattern:
    def patternUpward(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end=" ")
            for k in range((2*i)+1):
                print("*", end=" ")
            print()

    def patternDownward(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end=" ")
            for k in range((2*n)-(2*i)-1):
                print("*", end=" ")
            print()

    def patternNine(self, n):
        self.patternUpward(n)
        self.patternDownward(n)

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternNine(num)
