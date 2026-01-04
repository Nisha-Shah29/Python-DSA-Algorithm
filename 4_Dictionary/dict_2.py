class Dictionary:
    def displayValues(self, data):
        for value in data.values():
            print(value)

if __name__=="__main__":
    obj=Dictionary()
    prices={'Apple':100, 'Banana':40, 'orange':60}
    obj.displayValues(prices)