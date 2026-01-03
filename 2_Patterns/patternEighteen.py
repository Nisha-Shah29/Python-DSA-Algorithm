class Pattern:
    def patternEighteen(self, n):
        for i in range(n):
            startChar=chr(ord('A')+(n-i-1))
            for j in range(i+1):
                print(startChar, end=" ")
                startChar=chr(ord(startChar)+1)
            print()

if __name__=="__main__":
    obj=Pattern()
    num=int(input("Enter the value of n: "))
    obj.patternEighteen(num)