class Dictionary:
    def displayKeyValue(self, data):
        for key, value in data.items():
            print(key, value)


if __name__=="__main__":
    obj=Dictionary()
    marks={"math":90, "science":85, "english":88}
    obj.displayKeyValue(marks)