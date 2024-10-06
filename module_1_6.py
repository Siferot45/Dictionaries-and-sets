my_dict = {1:"Петя", 2:"Вася", 3:"Настя", 4:"Мия", 5:"Кирил"}
print(my_dict)
print(my_dict.get(1))
print(my_dict.get(6))
my_dict.update({6:"Юля", 7:"Данил"})
my_value = my_dict.pop(2)
print(my_value)
print(my_dict)

my_set = {1, 6, 3, 2, 5, 8, 5, 5, 4, 4, 6, 1, 1, 7, 5, 5, False, False, True, "string", "string",}
print(my_set)
my_set.add(10)
my_set.discard(1)
print(my_set)