class Dictionary:
    def numberOfKeys(self, num):
        count=0
        for key in num:
            count=count+1
        return count


if __name__=="__main__":
    obj=Dictionary()
    data={'a':1, 'b':2, 'c':3, 'd':4}
    result=obj.numberOfKeys(data)
    print("Number of keys:", result)


# Method-2 using built function
# class Dictionary:
#     def numberOfKeys(self, num):
#         count = len(num.keys())
#         return count

# if __name__=="__main__":
#     obj=Dictionary()
#     data={'a':1, 'b':2, 'c':3, 'd':4}
#     result=obj.numberOfKeys(data)
#     print("Number of keys:", result)