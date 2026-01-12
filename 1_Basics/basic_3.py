class Solution:
    def validateResult(self, marks):
        if marks>=90:
            print("Grade A")
        elif marks>=70:
            print("Grade B")
        elif marks>=50:
            print("Grade C")
        elif marks>=35:
            print("Grade D")
        else:
            print("Fail")

if __name__=="__main__":
    sol=Solution()
    num=int(input("Enter the marks: "))
    sol.validateResult(num)