
# # 1) Написать программу, которая считывает целое число и выводит значение,
# #  которое в два раза больше, чем введенное.
a = int(input("Введите целое число :"))

print(f"Вы ввели : {a} результат : {a * 2}")
print("Вы ввели :", a ,"результат :", a*2 ,sep=' ')
print("Вы ввели : {} результат : {}".format(a,a*2))

# #########################################################################
# # 2) Написать программу, которая считывает число с точкой и выводит значение,
# # два раза больше, чем введенное.

a = float(input("Введите число с точкой :"))

print(f"Вы ввели : {a} результат : {a * 2}")
print("Вы ввели :", a ,"результат :", a*2 ,sep=' ')
print("Вы ввели : {} результат : {}".format(a,a*2))

#########################################################################
# 3) Написать программу, которая считывает строку и выводит удвоенную эту строку
a=input("Введите строку :")

print(f"Вы ввели : '{a}' результат : '{(a +' ')*2}' ")
print("Вы ввели : ", a ," результат : ", (a +' ')*2+"'",sep="'")
print("Вы ввели : '%s' результат : '%s'"  %(a , (a +' ')*2))