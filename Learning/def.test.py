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

#Ввести 2 числа и вывести их сумму
x = int(input("Введите 1 число: "))
y = int(input("Введите 2число: "))

def sum(a,b):
   return(print(a+b))

sum(x, y)

#Вычислить значение функции
def f(a):
   return(print(2*a-2))
f(5)

#Вариант 2
def f(a):
   return(2*a-2)

print(f(5))


