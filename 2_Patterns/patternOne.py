class Pattern:
    def patternOne(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternOne(num)
