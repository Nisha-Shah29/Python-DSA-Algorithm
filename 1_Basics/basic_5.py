class Solution:
    def sumOfNum(self, num):
        sumOfFirstAndLast=num[0]+num[-1]
        return sumOfFirstAndLast

if __name__=="__main__":
    sol=Solution()
    nums=[2,3,4,5,6]
    result=sol.sumOfNum(nums)
    print("sum of first and last num is:" ,result)