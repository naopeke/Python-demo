# 文字列の出力
print ('Hello Python')
print ("Hello Python")
print ('3 + 5')

#数字の出力
print(3)
print(3 + 7)
print(7 - 3)

print(3 / 2) #1.5　小数で出力
print(7 % 3) #1 余りが出力

name = 'John'
print(name)  #John
print('name')#name

#変数　アンダーバーでつなげる
apple_count = 3
apple_price = 100
total_price = apple_count * apple_price
print(total_price) #結果：300

#変数の更新
x = 5
print(x) # 5

x =11
print(x) # 11

x = x + 3
print(x) #14

x = x + 10
x += 10

x = x - 10
x -= 10

x = x * 10
x *= 10

x = x / 10
x /= 10

x = x % 10
x %= 10

#文字列の連結
print ('Hello ' + 'Python')

name = 'John'
print('My Name is ' + name)

#データ型の違い
print(5 + 7)     #12
print('5' + '7') #57

#型変換 データ型の異なる文字列型と数値型を連結するとエラーになるため必要
# str：数値型　＝＞　文字列型
price = 100
print('りんごの価格は' + str(price) + '円です')

# int：文字列型　＝＞　数値型
count = '3'
price = 100
total_price = price * int(count)
print(total_price) #300

#if文
score = 100
if score == 100:
    print('よくできました！')
    print('次も頑張りましょう') #必ず同じインデント

if score != 0:
    print('次回はIF文のテストです')

#真偽値
print(score == 100) # True
print(score == 99)  # False

# else
score = 50
if score == 100:
     print('よくできました')
else:
     print('頑張りましょう')

# elif 　いくつでも書ける
score = 70
if score == 100:
     print('よくできました！')
elif score >= 60:
     print('まずまずです')
elif score > 40:
     print('んー')
else:
     print('頑張りましょう')

# and
time = 14
if time > 10 and time <18:
    print('就業時間です')

# or
time = 15
if time == 10 or time == 15:
    print('おやつの時間です')

# not
time = 9
if not time == 18:
     print('退社時刻ではありません')

# andを使わない書き方
time = 16
if 10 < time < 18:
     print('就業時間です')


# お買い物代金の計算（１）
apple_price = 200
count = 5
total_price = apple_price * count
print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')


# お買い物代金の計算（２）
apple_price = 200
input_count = input('購入するりんごの個数を入力してください：')
#変数input_countの値は文字列になっているのでintで数値に型変換
count = int(input_count)
total_price = apple_price * count
print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')


# お買い物代金の計算（３）
apple_price = 200
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# money と total_price の比較結果によって条件を分岐
if money > total_price:
    print('りんごを' + str(count) + '個買いました')
    print('残金は' + str(money - total_price) + '円です')
elif money == total_price:
    print('りんごを' + str(count) + '個買いました')
    print('財布が空になりました')
else: 
    print('お金が足りません')
    print('りんごを買えませんでした')

# リスト
#　文字列のリスト
    ['pasta', 'curry', 'sushi']
# 数値のリスト
    [1, 2, 3, 5, 7, 13, 21]
# 文字列と数値のリスト
    ['apple', 'banana', 200, 300]
# 変数に代入
    foods = ['pasta', 'curry', 'sushi']
    print(foods)

    print('好きな食べ物は' + foods[2] + 'です')

# リストの要素を更新
    foods[1] = 'pizza' #['pasta', 'pizza', 'sushi']

# リストに要素を追加
    foods.append('curry') #['pasta', 'pizza', 'sushi', 'curry']

# for文
    for food in foods:
         print('好きな食べ物は' + food + 'です')

# 辞書:リストとの違いは、個々の要素をインデックス番号ではなくキーと呼ばれる名前を付けて管理する点。キーと値のペアが1つの要素
    fruits = {'apple':'red', 'banana':'yellow', 'grape':'purple'}
    print(fruits)  # banana, apple, grapeというように順序がない Python 3.7以降は順序が保証

# 辞書の要素の取り出し方
    print('appleの色は' + fruits['apple'] + 'です') 

# 辞書の要素の更新
    fruits['apple'] = 'green'
    print('appleの色は' + fruits['apple'] + 'です')

