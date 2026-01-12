class Solution:
    def string(self, strS):
        if strS:
            result=strS[-1]
        else:
            return None
        return result

if __name__=="__main__":
    sol=Solution()
    s=input("Enter the string: ")
    a=sol.string(s)
    print("The last character of string: ", a)