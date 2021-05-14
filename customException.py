import random
class Error(Exception) :
    pass

class ValueTooSmalllError(Error) :
    pass

class ValueTooLargeError(Error) :
    pass
#ランダムな1~10までの整数を生成する
number = random.randint(1,10)

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmalllError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmalllError:
        print("too small,try again")
        print()
    except ValueTooLargeError:
        print("too large,try agein")
        print()

print("you guessed it correctly")