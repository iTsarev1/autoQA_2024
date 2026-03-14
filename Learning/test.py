a = 1
b = 3
c = a + b - 3
print(c)

a = "Hello"
b = ", World"
c = a + b
print(c)
print(a)

a = 1.5
b = 3.2
c = a + b
print(c)

txt = [1,2,3,4,5,4]
for i in txt:
    if i == 4:
      print(i)

str_1 = "f34r23r343rr438gd5"
print(list(str_1))

str_1 = "f34r23r343rr438gd5"
for i in str_1:
   if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
     print(int(i))

c = "l6l3n3v4v56v7"
print (list(c))

ls = [1,2,3,4,5]
print(ls[::-1])

ls = [1,2,3,4,5]
print(ls[1:-1:])

ls = [1,2,3,4,5]
print(ls[::-2])

ls = [1,2,3,4,5]
print(ls[4::1])

ls = [1,2,3,4,5]
print(ls[4:1:-1])

ls = [1,2,3,4,5]
print(ls[-2:2:-1])


dict_new = {"name": "Jonh", "age": 30}
print(dict_new.items())


dict_new = {"name": "Jonh", "age": ({"age": 30, "name": "jon"}, {})}

for key, value in dict_new.items():
   print(type(value))
   if type(value) == tuple:
    print("1")

dict_new = {"name": "Jonh", "age": [{"age": 30, "name": "jon"}, {}]}
result_dict = {}
result_list = []
result_str = ""
for key, value in dict_new.items():
   if type(value) == list:
      result_list = value
      result_dict = value[0]
   if type(value) == str:
      result_str = value
print(result_list, result_dict, result_str)

numbers = [1,2,3,4,5]
average = sum(numbers) / len(numbers)
print(average)

# Итерация по элементам списка
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "apple":
     print(i)

count = 0
while count != 5:
   print("Hi")
   count += 1

# Прерывание цикла, когда count достигает 3
count = 1
while True:
    print(count)
    if count == 3:
        break
    count += 1

# Печать только нечетных чисел меньше 10
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print("-" * 20)  # Добавляет разделительную линию между числами

def hello():
   print("Привет, Мир!!!")

hello()
hello()
hello()

def say_hello(username, age):
   print(f"Hello, {username}!")
   print(f"Your age is {age}!")
   print("-" * 20)

say_hello("Valera", 20)
say_hello("Anna", 39)

def numbers_sum(num1=1, num2=2):
   print(f"{num1} + {num2} = {num1 + num2}")

numbers_sum(num1=1, num2=9)
numbers_sum(num1=-8, num2=907)
numbers_sum(num1=1/5, num2=54)

def numbers_sum(num1=1, num2=2):
   print(num1 + num2)

numbers_sum(num1=1, num2=9)
numbers_sum(num1=-8, num2=907)
numbers_sum(num1=1/5, num2=54)

ls = [1,2,3,4,5]
print(ls[::-1])


x = 40
print(id(x))

x = 45
print(id(x))

my_list = [1, 2, 3, 4]
print(id(my_list))

my_list = [1, 2, 3, 48]
print(id(my_list))


#Выводит размер одежды
obkhvat = int(input('Введите обхват груди в см: '))

if 86 <= obkhvat <= 92:
   print('S')
if 94 <= obkhvat <= 100:
   print('M')
if 102 <= obkhvat <= 108:
   print('L')
if 110 <= obkhvat:
   print('XL')
else:
   print('Нет в наличии')




def hello(x):
   if x != '':
      print(f'Hello {x}')
   else: 
      print('Hello world')

hello('')
hello('Ilya')