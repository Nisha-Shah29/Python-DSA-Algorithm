class Pattern:
    def patternSeventeen(self, n):
        for i in range(n):
            startChar='A'
            for j in range(n-i-1):
                print(" ", end=" ")
            for k in range(i+1):
                print(startChar, end=" ")
                startChar=chr(ord(startChar)+1)
            startChar=chr(ord(startChar)-2)
            for l in range(i):
                print(startChar, end=" ")
                startChar=chr(ord(startChar)-1)
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternSeventeen(num)