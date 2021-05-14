class Student:
    #初期化メソッド(コンストラクタ)の作成
    #ここで書いたものは全てのクラスに反映される
    def __init__(self) :
        self.gender = ""
    # def __init(self,gender):
    #     self.gender = genderとしても同じ
    # その場合
    # a002 = Student("woman")
    # といった記述ができるようになる
    def avg(self,math,english):
        sum = math+english
        ave = sum/2
        print(ave)

a001 = Student() #インスタンス化(オブジェクト化) 
#a001.avg(80,70)
 
#アトリビュートの作成
a001.name = "sato"
print(a001.name)
#ここで作ったnameというアトリビュートは他のクラスには反映されない
a002 = Student()
#print(a002.name)
#->error

a001.gender = "man"
print(a001.gender)
print(a002.gender)