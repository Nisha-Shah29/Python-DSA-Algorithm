class Pattern:
    def patternFour(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternFour(num)
