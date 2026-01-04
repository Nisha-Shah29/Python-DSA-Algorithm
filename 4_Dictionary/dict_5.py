class Dictionary:
    def numberOfValues(self, num):
        count=0
        for value in num.values():
            count=count+1
        return count


if __name__=="__main__":
    obj=Dictionary()
    data={'a':1, 'b':2, 'c':3, 'd':4}
    result=obj.numberOfValues(data)
    print("Number of values:", result)


# Method-2 using built function
# class Dictionary:
#     def numberOfValues(self, num):
#         count = len(num.values())
#         return count

# if __name__=="__main__":
#     obj=Dictionary()
#     data={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
#     result=obj.numberOfValues(data)
#     print("Number of values:", result)