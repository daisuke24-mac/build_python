#関数の練習
def function(a):
    #return文
    a += 5
function(3)

#１つの引数を受け取ってそれをそのまま表示する関数
def response(greeting) : 
    print(greeting)
response("hello")

#関数を変数に代入する
hello = response
hello("tanaka")

#２つの引数を足してその合計を返す関数
def add(a,b) : 
    sum = a+b
    return sum
sum = add(31,32)
print(sum)

#２つの引数を足してその合計を表示する関数
def add_result(a,b) : 
    print(add(a,b))
add_result(41,144)

#３つの引数からその平均を返す関数
def average(a,b,c) :
    ave = (a+b+c)/3
    return ave
print(average(421,431,42))

#複数の引数からその平均を返す関数
def average_ad(list) :
     sum = 0
     for i in list :
         sum += i
     ave = sum/i
     return ave
sequence = [2,1,45,124,6,3]
print('{:.1f}'.format(average_ad(sequence)))