class Pattern:
    def patternFive(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternFive(num)
