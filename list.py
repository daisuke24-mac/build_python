#リスト内の特定の文字を削除する時
list = [1,2,3,4,5,2,3,3]

#removeだと条件に合う最初の一つだけが削除される
list.remove(2)
print(list)

#リスト内包表記なら条件に合う全てが削除できる
list = [1,2,3,4,5,2,3,3]
print([i for i in list if i != 2])