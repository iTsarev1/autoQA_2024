dict_new = {'name':'John', 'age':[{'age': 30, 'name':'jon'},{}]}
for key,value in dict_new.items():
    if type(value)== list:
        result = value[0]
print(result)
print('-'*20)




#Задача: Если рез-т словарь, то положить его в result_dict, 
#а если список, то положить в result_list

dict_new = {'name':'John', 'age':[{'age': 30, 'name':'jon'},{}]}
result_dict = {}
result_list = []

for key, value in dict_new.items():
    if type(value) == list:
        result_list = value
        result_dict = value[0]
print(result_dict, result_list)
print('-'*20)




dict_new = {'name':'John', 'age':[{'age': 30, 'name':'jon'},{}]}

result_dict = {}
result_list = []

for key, value in dict_new.items():
    if type(value) == list:
        result_list = value
        result_dict = value[1]
print(result_list, result_dict)
print('-'*20)


#Хотим также сохранить значение John и положить его в result_str

result_dict = {}
result_list = []
result_str = ''

for key, value in dict_new.items():
    if type(value) == list:
        result_list = value
        result_dict = value[0]
    if type(value) == str:
        result_str = value
print(result_list, result_dict, result_str)