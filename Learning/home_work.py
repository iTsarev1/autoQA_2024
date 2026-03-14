#С объяснениями!!!
# Исходный список строк
n_list = ["devs dev dev dev ls devs ls ls ls jh jh jh jh"]

# Разбиваем строку на отдельные слова
n_list = n_list[0].split()

# Инициализируем переменные для хранения максимального числа повторений и наиболее часто встречающегося элемента
result_num = 0  # Счетчик максимального числа повторений
result_str = []  # Список для хранения элементов с максимальным числом повторений

# Проходим по каждому элементу в списке
for str_1 in n_list:
    # Считаем количество повторений текущего элемента
    result = n_list.count(str_1)
    
    # Если число повторений текущего элемента больше или равно текущему максимальному числу повторений
    if result >= result_num:
        # Если число повторений текущего элемента больше текущего максимального числа повторений
        if result > result_num:
            # Очищаем список, так как нашли новый максимум повторений
                result_str.clear()
        
        # Обновляем текущее максимальное число повторений
        result_num = result
        
        # Если текущий элемент еще не добавлен в список наиболее часто встречающихся элементов
        if str_1 not in result_str:
            # Добавляем текущий элемент в список
            result_str.append(str_1)

# Выводим результат
print("Наиболее часто встречающиеся элементы:", result_str)
print("Число повторений:", result_num)
print("-" * 20)




#Немного сложноватый вариант
n_list = ["devs dev dev dev ls devs ls ls ls jh jh jh jh"]
n_list = n_list[0].split()


result_num = 0
result_str = []

for str_1 in n_list:
     result = n_list.count(str_1)
     if result >= result_num:
          if result > result_num:
               result_str = []
               result_num = result
          if str_1 not in result_str:
            result_str.append(str_1)

print(result_str)
print(result_num)
print("-" * 20)



#Убрал строку 'if result >= result_num:'--> Рез-т не тот
n_list = ["devs dev dev dev ls devs ls ls ls jh jh jh jh"]
n_list = n_list[0].split()


result_num = 0
result_str = []

for str_1 in n_list:
     result = n_list.count(str_1)
     if result > result_num:
          result_str = []
          result_num = result
     if str_1 not in result_str:
          result_str.append(str_1)

print(result_str)
print(result_num)
print("-" * 20)



#Вариант упрощенный.Success
n_list = ["devs dev dev dev ls devs ls ls ls jh jh jh jh"]
n_list = n_list[0].split()

result_num = 0  
result_str = []  

for str_1 in n_list:
    result = n_list.count(str_1)
    if result > result_num:
        result_str = []
        result_num = result
    if result_num == result and str_1 not in result_str:
        result_str.append(str_1)
print(result_str)
print(result_num)




n_list = ["devs dev dev dev ls devs ls ls ls jh jh jh jh"]
n_list = n_list[0].split()

result_num = 0
result_str = []


for str_1 in n_list:
    result = n_list.count(str_1)
    if result > result_num:
          result_str = []
          result_num = result
    if result_num == result and str_1 not in result_str:
          result_str.append(str_1)

print('Самые часто встречающиеся значения:', result_num)
print('Число повторений:', result_str)





n_list = ["devs dev dev dev ls devs ls ls ls jh jh jh jh"]
n_list = n_list[0].split()


result_num = 0
result_str = []



for str_1 in n_list:
        result = n_list.count(str_1)
        if result > result_num:
             result_str = []
             result_num = result
        if result == result_num and str_1 not in result_str:
             result_str.append(str_1)
print(result_num)
print(result_str)

for num in range(10):
    if num % 2 == 0:
        continue
    print(num)



spisok = ["23 23 frre gy yh 2 ук"]
spisok = spisok.


