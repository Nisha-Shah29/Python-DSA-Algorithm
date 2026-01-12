class Solution:
    def string(self, strS):
        result=strS[-1]
        return result
        
if __name__=="__main__":
    sol=Solution()
    s="Nisha"
    a=sol.string(s)
    print("The last character of string: ", a)