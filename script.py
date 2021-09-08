# print ('HelloWorld')
# print (1+3)
# #aiueo
# i = 3
# w = 4
# print( i + w)

# for i in range(100):
#     print("Hello, World!")

# int a;
# print (a = 144;)

# b = 100
# b -= 10
# print (b)

# a = 10 / 0
# print(a)

# x = 100
# if x == 10:
#     print("10")
# elif x == 20:
#     print(20)
# else:
#     print("分かりません")

# def f(x):
#     return x * 2 
# f(2)
# result = f(2)
# print(result)

# def f(x):
#     return x + 1

# def f(x):
#     return x + 1

# z = f(4)
# if z == 5:
#     print("z is 5")
# else:
#     print("z is not 5")

# def f():
#     return 1 + 1
# result = f()
# print(result)

# x = len("monty")
# print(x)

# y = str(100)
# print(y)

# z = float(100)
# print(z)

# w = float(20.54)
# print(w)

# age = input("Enter your age :")
# int_age = int(age)
# if int_age < 21:
#     print("You are young")
# else:
#     print("You are old")

# def even_odd(x):
#     if x % 2 == 0:
#         print("偶数")
#     else:
#         print("奇数")

# even_odd(2)
# even_odd(3)

# n = input("type a number :")
# n = int(n)
# if n % 2 == 0:
#     print("n is even")
# else:
#     print("n is odd")

# def even_odd():
#     n = input("type a number :")
#     n = int(n)
#     if n % 2 == 0:
#         print("n is even")
#     else:
#         print("n is odd")

# even_odd()
# even_odd()
# even_odd()

# def f(x=2):
#     return x ** x

# print(f())
# print(f(4))

# def add_it(x, y=10):
#     return x + y
# result = add_it(2)
# print(result)

# def f():
#     x = 1
#     y = 2
#     z = 3
#     print(x)
#     print(y)
#     print(z)

# f()

# x = 100
# def f():
#     global x
#     x += 1
#     print(x)

# f()

# try:
#     a = input("type a number:")
#     b = input("type another:")
#     a = int(a)
#     b = int(b)
#     print(a/b)
# except(ZeroDivisionError,ValueError):
#     print("bにゼロは入力しちゃ駄目だよ")

# def add(x,y):
#     """
#     Returns x + y
#     :param x: int.
#     :param y: int.
#     :return: int sum pf x and y.
#     """
#     return x + y

# add(3,7)

# def f(x):
#     return x ** 2
# print(f(4))

# def print_string(string):
#     print(string)

# print_string("Test:1, 2, 3")

# def add_mult(a,b,c,x=100,y=200):
#     return a + b + c + x + y

# result = add_mult(10,15,20)
# print(result)

# def waru1(x):
#     return x / 2

# def waru2(x):
#     return x * 4

# y = waru1(4)
# z = waru2(y)

# print(z)

# def convert(string):
#     try:
#         return float(string)
#     except ValueError:
#         print("Could not convert the string to a float")

# c = convert("55.0")
# print(c)

# fruit = ["apple","orange","group"]
# fruit.append("banana")
# fruit.append("peach")
# print(fruit)

# fruit = ["apple","orange","group"]
# print(fruit[0])

# colors = ["blue","green","yellow"]
# print(colors)
# colors[2] = "red"
# print(colors) 

# colors = ["blue","green","yellow"]
# print(colors)
# item = colors.pop()
# print(item)

# colors = ["blue","green","yellow"]
# x = "green" not in colors
# y = "black" not in colors
# print(x)
# print(y)

# x = len(colors)
# print(x)

# colors = ["blue","green","yellow"]
# guess = input("好きな色を入力してね：")
# if guess in colors:
#     print("あたり")
# else:
#     print("はずれ")

# dys = ("1984","2000","3000")
# print(dys[2])

# songs = {"1":"fun",
#          "2":"blue",
#          "3":"me",
#          "4":"floor",
#          "5":"live"
#          }
# n = input("数字を入力してください　：　")
# if n in songs:
#     song = songs[n]
#     print(song)
# else:
#     print("見つかりません")

# me = {
#     "height": "6",
#     "fav_color": "red",
#     "fav_author": "Orwell"
# }

# answer = input("Type height, fav_color or fav_author")
# if answer in me:
#     result = me[answer]
#     print(result)

# print("hello\"world\"")
# print("line1\nline2\nline3")

# fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
# fox = " ".join(fox)
# fox = fox[0: -2] + "."
# print(fox)
# # print(fox[0: -2])

# name = "Ted"
# for character in name:
#     print(character)

# tv = ["GOT","Narcos","Vice"]
# i=0
# for new in tv:
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new
#     i += 1
# print(tv)

# tv = ["GOT","Narcos","Vice"]
# all_shows = []

# for show in tv:
#     show = show.upper()
#     all_shows.append(show)
    
# print(all_shows)

# for i in range(1,11):
#     print(i)

# x = 10
# while x > 0:
#     # print('{}'.format(x))
#     print(x)
#     x -= 1
# print("Happy NewYear!")

# for i in range(1,100):
#     print(i)
#     break

# for i in  range(1,6):
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# for i in range(1,3):
#     print(i)
#     for letter in ["a","b","c"]:
#         print(letter)

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# added = []
# for i in list1:
#     for j in list2:
#         added.append(i + j)
# print(added)

# shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
# for index, show in enumerate(shows):
#     print(index,show)
#     # print(show)


# numbers = [11,32,33,15,1]

# while True:
#     answer = input("Guess a number or type q to quit. :")
#     if answer == "q":
#         break
#     try:
#         answer = int(answer)
#     except ValueError:
#         print("please type a number or q to quit.")
#     if answer in numbers:
#         print("You guessed correctly!")
#     else:
#         print("You guessed invorrectly!")


list1 = [8,19,148,4]
list2 = [9,1,33,83]
add_list = []

for i in list1:
    for j in list2:
        add_list.append(i * j)

print(add_list)