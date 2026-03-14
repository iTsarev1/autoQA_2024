#APPEND
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print("-" * 20)

#CLEAR
my_list_1 = [1, 4, 3, 7]
my_list_1.clear()
print(my_list_1)
print("-" * 20)

#COPY
original_list = [1, 2, 3, 4, 5]
copy_list = original_list.copy()
copy_list.append(69)
print(copy_list)
print(original_list)
print("-" * 20)

original_list = [1, 2, 3, 4, 5]
copy_list = original_list.copy()
original_list.append(6.6)
print(original_list)
print(copy_list)
print("-" * 20)

#COUNT
my_list_2 = [1, 2, 3, 1, 4, 1, 5]
count_of_ones = my_list_2.count(1)
print(count_of_ones)
print("-" * 20)

#INDEX
my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
index_of_5 = my_list_3[5]
print(index_of_5)
print("-" * 20)

my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
index_of_5 = my_list_3.index(5)
print(index_of_5)
print("-" * 20)

#INSERT
my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_3.insert(2, 'xxx')
print (my_list_3)
print("-" * 20)

#POP
my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_3.pop(5)
print (my_list_3)
print("-" * 20)

#REVERSE
my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_3.reverse()
print (my_list_3)
print("-" * 20)

#SORT
my_list_4 = [7, 45, 2, -1, 0, 65, 9, 8]
my_list_4.sort()
print (my_list_4)
print("-" * 20)

my_list_4 = [7, 45, 2, -1, 0, 65, 9, 8]
my_list_4.sort(reverse = True)
print (my_list_4)
print("-" * 20)

#REMOVE
my_list = [1, 2, 3, 4, 5, 3]
my_list.remove(3)
print (my_list)
print("-" * 20)

my_list = [1, 2, 3, 4, 5, 3]
while 3 in my_list:
    my_list.remove(3)
print (my_list)
print("-" * 20)

my_list = [1, 2, 3, 4, 5, 3]
#
#

my_list = [1, 2, 3, 4, 5, 3]
my_list = my_list[0]

if my_list in [3]:
    print('Hi')
print(my_list) 