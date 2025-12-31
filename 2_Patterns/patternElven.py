class Pattern:
    def patternElven(self, n):
        for i in range(n):
            if i%2==0:
                start=1
            else:
                start=0
            for j in range(i+1):
                print(start, end=" ")
                start=1-start
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternElven(num)
