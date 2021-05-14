#ランダムな0~9までの数字を６つ出力するプログラム
import random

for i in range(6) :
    num=(random.randint(0,9))
    print(num,end="")
print()