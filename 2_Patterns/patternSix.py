class Pattern:
    def patternSix(self, n):
        for i in range(n):
            for j in range(n-i):
                print(j+1, end=" ")
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternSix(num)
