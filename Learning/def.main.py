#Добавить числа и вывести суммму
def add_numbers(x,y):
    return(print(x + y))
add_numbers(1, 3)

#NO return
def add_numbers(x,y):
    print(x + y)
add_numbers(1, 3)

#Добавить числа и вывести суммму
def add_numbers(x,y):
    return(print(x + y))
z = add_numbers(1, 3)

a = 45 
b = 5
def f():
    global a
    a = a + 2
    print(a)
f()

c = a + b
print(c)

def double(x):
    return(print(x*2))
double(5)

#сортировка списка в порядке возрастания
numbers = [5, 2, 8, 1, 6]
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

sorted_numbers = sort_list(numbers)
print("Отсортированный список:", sorted_numbers)

