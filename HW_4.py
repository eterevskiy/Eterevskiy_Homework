import random


def separator():
    print("\n##################################################################\n")
def input_digit():
    while True :
        digit=input('Введите целое число :')
        if digit.isdigit() : return digit
  

# 1. Дано целое число (int). Определить сколько нулей в этом числе.

a = input_digit()
print(f"Целое число: {a}\nКоличество нулей: {a.count('0')}")
separator()

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

a = input_digit()
count1=0
count2=0
# Способ 1
for x in a[::-1] :
    if x=='0' :
        count1+=1
    else :
        break
# Способ 2
a=int(a)
while a % 10 == 0 :
    a//=10
    count2+=1
print(f"Целое число: {a}\nКоличество нулей в конце числа:\n\tСпособ 1: {count1}\n\tСпособ 2: {count2}")
separator()

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1=[random.randint(0,100) for i in range(15)]
print("List 1:",my_list_1)
my_list_2=[random.randint(0,100) for i in range(15)]
print("List 2:",my_list_2)
my_reuslt= my_list_1[::2]+my_list_2[1:len(my_list_2):2]
print("Result:",my_reuslt)
separator()

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list=[random.randint(0,100) for i in range(15)]
print(my_list)
new_list=my_list[1:]+[my_list[0]]
print(new_list)
separator()

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list=[random.randint(0,100) for i in range(15)]
print(my_list)
my_list.append(my_list.pop(0))
print(my_list) 
separator()

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

stroka = "43 больше чем 34 но меньше чем 56"
result=sum( int(x) for x in stroka.split() if x.isdigit())
print(result)
separator()
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
_start= my_str.index(l_limit)+1
_end =len(my_str)-my_str[::-1].index(r_limit)-1
sub_str=my_str[_start:_end]
print(sub_str)
separator()

# or
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# _start= my_str.index(l_limit)+1
# _end=0
# for x in range(len(my_str)-1 , -1 , -1) :
#      if my_str[x] == r_limit :
#          _end=x
#          break
# sub_str=my_str[_start:_end]
# print(sub_str)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str="Дана строка my_str."
if(len(my_str)%2!=0) : my_str+="_"
n=2
new_list=[my_str[i:i+n] for i in range(0, len(my_str), n)]
print(new_list)
separator()

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list=[2,4,1,5,3,9,0,7]
count=0
for idx in range(1,len(my_list)-2) :
    if my_list[idx]>my_list[idx-1]+my_list[idx+1] :
        count+=1
print (count)
separator()