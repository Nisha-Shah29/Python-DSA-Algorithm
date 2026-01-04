class Dictionary:
    def displayKeys(self, num):
        for key in num:
            print(key)

if __name__=="__main__":
    obj=Dictionary()
    data={'a':10, 'b':20, 'c':30}
    obj.displayKeys(data)