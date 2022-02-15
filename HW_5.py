import random 
import requests
from string import ascii_letters
from bs4 import BeautifulSoup

def separator():
    print("\n##################################################################\n")
   
# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
persons=[{"name": "John", "age": 15},
{"name": "Emma", "age": 19},
{"name": "Lucas", "age": 17},
{"name": "Michael", "age": 67},
{"name": "Jack", "age": 45},
{"name": "Isabella", "age": 26}]

def result_form(_list,_key) :
   return [item for item in _list if item==_list[0] or item.get(_key)==_list[0].get(_key)]
    
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.

def young_man(_list,_key) :
   return result_form(sorted(_list,key = lambda item : item[_key]),_key)


# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

def long_name(_list,_key) :
    return result_form(sorted(_list,key = lambda item : len(item[_key]),reverse=True),_key)


#  в) Посчитать среднее количество лет всех людей из списка.

def average_age(_list) :
    return sum(x.get('age') for x in _list)/len(_list)

###############################################################################################

# 2. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз

stroka1_2="Написать функцию которой"
stroka2_2="передается два параметр"

def intersection (string_1,string_2) :
    result=[]
    for i in set(string_1) :
        for j in set(string_2):
            if i==j :
                result+=[j]
    return result

# 3. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

stroka1_3="Написать функцию которой"
stroka2_3="передается два параметр"

def only_once(s1,s2) :
    return [symbol for symbol in intersection(s1,s2) if s1.count(symbol)==s2.count(symbol)==1]

# 4. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
names=["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin",
                "Lucas", "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob"]

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2_%D0%B2%D0%B5%D1%80%D1%85%D0%BD%D0%B5%D0%B3%D0%BE_%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
domains = []
for a in soup.find_all('a' , class_='new'):
    if a.text[0] == '.' :
        domains.append(a.text)

def email_generator(list_name,list_domain) :
    stroka=''.join(random.choice(ascii_letters) for i in range(random.randint(5,7)))
    number=random.randint(100,999)
    return f'{random.choice(names)}.{number}@{stroka}{random.choice(domains)}'

##############################################################################################################
##############################################################################################################
# OUTPUT :

# 1.
#################################################
print("Ask 1 :")
print(f"а) :\n\t{young_man(persons,'age')}")
print(f"б) :\n\t{long_name(persons,'name')}")
print(f"в) :\n\t{average_age(persons)}")
separator()
#################################################
# 2.
#################################################
print("Ask 2 :")
print(intersection(stroka1_2,stroka2_2))
separator()
#################################################
# 3.
#################################################
print("Ask 3 :")
print(only_once(stroka1_3,stroka2_3))
separator()
#################################################
# 4.
#################################################
print("Ask 4 :")
print(email_generator(names,domains))
separator()
#################################################