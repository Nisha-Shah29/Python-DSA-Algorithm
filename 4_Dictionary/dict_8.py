class Dictionary:
    def displayMaxKey(self, data):
        max_key = max(data, key=data.get)
        return max_key

if __name__=="__main__":
    obj=Dictionary()
    marks={"Ram":85, "Shyam":90, "Mohan":88}
    result=obj.displayMaxKey(marks)
    print("Key of maximum value is:", result)