class Dictionary:
    def displayMaximum(self, data):
        maximumValue = max(data.values())
        return maximumValue

if __name__=="__main__":
    obj=Dictionary()
    scores={"A":88, "B":92, "C":85}
    result=obj.displayMaximum(scores)
    print("Maximum value:", result)