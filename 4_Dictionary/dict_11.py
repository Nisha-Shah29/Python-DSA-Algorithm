#Method-1   Time complexity:O(n)
# class Dictionary:
#     def printValue(self, data):
#         for key,value in data.items():
#             if key=="age":
#                 return value

# if __name__=="__main__":
#     obj=Dictionary()
#     student={"name":"Nisha", "age":25, "course":"python"}
#     result=obj.printValue(student)
#     print("value of mentioned key age is:", result)


#Method-2   Time complexity:O(1)   most recommended method

class Dictionary:
    def printValue(self, data):
        return data["age"]

if __name__=="__main__":
    obj=Dictionary()
    student={"name":"Nisha", "age":25, "course":"python"}
    result=obj.printValue(student)
    print("value of mentioned key age is:", result)


# Method-3    Time compexity: O(1)
# student={"name":"Nisha", "age":25, "course":"python"}
# print("Value of age is:", student["age"])

