class Solution:
    def validateAge(self, age):
        if age>=18:
            print("Adult")
        else:
            print("Teen")

if __name__=="__main__":
    sol=Solution()
    a=int(input("Enter the number: "))
    sol.validateAge(a)