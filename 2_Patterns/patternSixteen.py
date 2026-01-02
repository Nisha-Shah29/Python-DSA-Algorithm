class Pattern:
    def patternSixteen(self, n):
        startChar='A'
        for i in range(n):
            for j in range(i+1):
                print(startChar, end=" ")
            print()
            startChar=chr(ord(startChar)+1)

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternSixteen(num)
