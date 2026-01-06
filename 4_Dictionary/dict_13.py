class Dictionary:
    def displaySize(self, data):
        return len(data)

if __name__=="__main__":
    obj=Dictionary()
    student={"name":"Nisha", "age":30, "course":"computer"}
    result=obj.displaySize(student)
    print("Length of dictionary is", result)



