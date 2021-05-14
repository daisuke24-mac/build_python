class Student:
    def __init__(self,name):
        self.name = name
    def calculateAvg(self,data):
        sum = 0
        for num in data:
            sum += num
        avg = sum/len(data)
        return avg
    def judge(self,avg):
        if(avg>=60):
            result="passed"
        else:
            result="failed"
        return result

a001=Student("sato")
satolist=[34,43,65,32,21]
satoavg=a001.calculateAvg(satolist)
print(satoavg)
satoresult=a001.judge(satoavg)
print(a001.name+" "+satoresult)
a002=Student("yamamoto")
yamamotolist=[77,87,97,67,82]
yamamotoavg=a002.calculateAvg(yamamotolist)
yamamotoresult=a002.judge(yamamotoavg)
print(+yamamotoavg)
print(a002.name+" "+yamamotoresult) # 数値と文字列は分ける
