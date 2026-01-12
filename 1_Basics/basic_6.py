class Solution:
    def patternXN(self, x, n):
        for i in range(n):
            print(x, end="")
            if i<n-1:
                print(" ", end="")
        print()
        print("Nisha")
        print("Shah")

if __name__=="__main__":
    sol=Solution()
    sol.patternXN(7,5)