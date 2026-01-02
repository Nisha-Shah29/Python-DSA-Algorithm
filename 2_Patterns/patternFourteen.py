class Pattern:
    def patternFourteen(self, n):
        for i in range(n):
            startChar='A'
            for j in range(i+1):
                print(startChar, end=" ")
                startChar=chr(ord(startChar)+1)
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternFourteen(num)
