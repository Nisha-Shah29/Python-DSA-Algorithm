class Pattern:
    def patternUpward(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()

    def patternDownward(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end=" ")
            print()

    def patternTen(self, n):
        self.patternUpward(n)
        self.patternDownward(n-1)

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternTen(num)
