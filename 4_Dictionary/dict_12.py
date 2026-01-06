class Dictionary:
    def printBol(self, data, keySearch):
        for key in data:
            if keySearch==key:
                return True
        return False


if __name__=="__main__":
    obj=Dictionary()
    student={"name":"Nisha", "age":35, "course":"python"}
    keyFind=input("Enter the key to search: ")
    result=obj.printBol(student, keyFind)
    print("Return the bol value if key exist or don't exist:", result)



