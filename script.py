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
if score == 100