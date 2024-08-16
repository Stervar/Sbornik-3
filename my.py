class MyClass:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(f"Hello, my name is {self.name}")

    @staticmethod
    def static_method():
        print("This is a static method")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}")

# Create an instance of the class
obj = MyClass("John")

# Call the instance method
obj.instance_method()  # Output: Hello, my name is John

# Call the static method
MyClass.static_method()  # Output: This is a static method

# Call the class method
MyClass.class_method()  # Output: This is a class method of MyClass


# Модуль 1 (часть 2)




#1



#print("Введите три числа:")

#a = int(input())
#b = int(input())
#c = int(input())

#d = a + b + c

#print(a, "+", b, "+", c, "=", d)





#2





#print() 

#x = int(input('введите зарплата за месяц'))   
#y = int(input('введидь сумма месячного платежа по кредиту в банке'))    
#z = int(input('введидь задолженность за коммунальные услуги.'))

#summa_plat= x - y - z 

#print(x, "-", y, "-",  z,"=" , summa_plat)





# 3






# print("Найдите S")

# d1 = int(input("видите число"))
# d2 = int(input("видите другое число"))

# s = (d1+d2)/2 

# print('(',d1, "+", d2, ")/2=", s)





#4




# print("To be")
# print("or not")
# print("to be")




#5





# print("'Life is what happens \n    when\n       you’are busy making other plans\n                                  John Lennon.\n")

# Модуль 1 (часть 3)
 





#1







# a = int(input("Введите число №1"))

# v = int(input(("Введите число №2")))

# n = int(input(("Введите число №3")))

# print(a,v,n)


# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# print(a*100+b*10+c)







#2






# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# g = int(input("Введите число №4"))


# s = (a * b * c * g) 

# print("Площадь параллелепида равна" ,a, "*",b, "*",c,"*",g,"=",s)







# №3






# a = float(input("Введите количество метров"))

# s = (a * 100)
# print ("Сумма сантиметров в метрах  равна ", s, "сантиметров")

# a = float(input("Введите количество метров"))

# s = (a * 10)
# print ("Сумма сантиметров в метрах  равна ", s, "дацеметров")

# a = float(input("Введите количество метров"))

# s = (a * 1000)
# print ("Сумма сантиметров в метрах  равна ", s, "милимтров")

# a = float(input("Введите количество метров"))

# s = (a *  0.000621)
# print ("Сумма сантиметров в метрах  равна ", s, "миль")







#№4







# a = int(input("размер основания треугольника"))

# h = int(input("размер высоты треугольника"))

# summa_plat= S = (a*h)/2

# print("Площадь  треугольника равен ", S)

# print(a,"*"  , h, "/2 = ", S )






# №5







# (запарестый способ)

# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# g = int(input("Введите число №4"))

# v = print(a*1000+b*100+c*10+g)

# v = input("Повторите результат если хотите перевернуть число")

# v = v[::-1]

# print(v)


# (легкий способ)

# number = input()
# number = number[::-1]
# print(number)






#Модуль 2 Операторы ветвлений (Часть 1)






# №1






# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# operation = input("Выберете один из вариантов решения - (+,*):")

# if operation == "+":
#     print(a + b + c)

# elif operation == "*":
#     print(a * b * c)
# else:
#     print("Вы ввели неверный оператор")



# Почему так нельзя делать?
# y = print(a * b * c) 
  
# y = print("сумма трех чисел равна")


# if print ==  2:  

# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# y=summa_plat= S = a * b * c 
# y=print("сумма трех чисел равна")
# y=print(S)





# №2
 




# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# all = [a, b, c]

# operation = input("Выберете один из вариантов решения чтобы найти последовательность - (a,b,c):")

# if operation == "a":
#       print ('Максимум из 3:', max(all))
# elif operation == "b":
#     print ('Минимум из 3:', min(all))
# elif operation == "c":
#      print('Среднее из 3:', sum(all) / len(all))
# else:
#     print("Вы ввели неверный вариант")




# №3





# a = int(input("Введите количество метров"))

# operation = input("Выберете один из вариантов решения - (мили,дюймы,ярды): ")

# if operation == "мили":
#     print ('Мили:', a * 0.000621371192)

# if operation == "дюймы":
#     print ('Дюймы:', a * 39.3700787)

# if operation == "ярды":
#     print ('Ярды', a * 0.9144)
# else:
#     print("Вы ввели неверный вариант")






#Модуль 2 Операторы ветвлений (Часть 2)





# №1






# operation = input("Введите номер недели (1,2,3,4,5,6,7): ")
# if operation == "1":
#     print("Понедельник")
# if operation == "2":
#     print("Ввторник")
# if operation == "3":
#     print("Среда")
# if operation == "4":
#     print("Четверг")
# if operation == "5":
#     print("Пятница")
# if operation == "6":
#     print("Суббота")
# if operation == "7":
#     print("Восскресенье")
# else:
#     print("Вы ввели неверный вариант")







# №2








# num = int(input("Введите номер месяца (1,2,3,4,5,6,7,8,9,10,11,12): "))
# month = ['Январь','Февраль'///]
# print(month[num-1])
# if operation == "1":
#     print("Январь")
# if operation == "2":
#     print("Февраль")
# if operation == "3":
#     print("Март")
# if operation == "4":
#     print("Апрель")
# if operation == "5":
#     print("Май")
# if operation == "6":
#     print("Июнь")
# if operation == "7":
#     print("Июль")
# if operation == "8":
#     print("Август")
# if operation == "9":
#     print("Сентябрь")   
# if operation == "10":
#     print("Октябрь")
# if operation == "11":
#     print("Ноябрь")
# if operation == "12":
#     print("Декабрь")







#№3








# peration = input("Введите число")

# peration = int(peration)

# if peration < 0:
#     print("«Number is negative»,")
# if peration > 0:
#     print("«Number is positive»,")
# if peration  == 0:
#     print("«Number is equal to zero»")






#№4







# a = input("Введите число №1 :")

# p = input("Введите число №2 :")


# if a == p: print('Эти два числа равны')

# elif a != p: print('Эти два числа не равны')

# if a > p: print('Первое число больше второго')

# if a < p: print('Второе число больше первого')








#Модуль 2 Операторы ветвления (Часть 3)






#№1







# a = int(input("Введите число от 1-100"))

# if  1 <=  a <= 100: 
#     print("Число входит в диапазон от 1 до 100:")
    
# # if a != 1 or a != 100:
# #         print("Ошибка")

# elif not a %3 == 0 :
#     print("Fizz")

# elif not a % 5 == 0:
#     print("Buzz")

# if not a % 3 == 0 and not a % 5 == 0:
#     print("Fizz Buzz")
# else:
#     print(a)
# else :
#  print("Ошибка,введите число в диапазоне [1; 100]")
# почему сдесь не поучаеться вести вторую если..?






#№2






# b = int(input("Введите число от 1-100"))

# a = int(input("Введите в каую степень вы хотите возвести число[0-7]:"))

# if 0 <= a <= 7:
  
#   print(a ** b)

# else:

#     print("Ошибка,введите число в диапазоне [0; 7]")





#3





# a = int(input("Введите стоимость разговора:"))
# b = int(input("Выбирите одного из опреторов [1-2-3-4]:"))

# if b == 1:
#     print(a * 0.95)
#     print("стоимость тарифа в руб")
# if b == 2:
#     print(a * 0.92)
#     print("стоимость тарифа в руб")
# if b == 3:
#     print(a * 0.9) 
#     print("стоимость тарифа в руб")
# if b == 4:
#     print(a * 0.85) 
#     print("стоимость тарифа в руб")






#4 (x/100*10)






# r = int(input("Введите сумму продаж для 1 менеджера [ОТ 500-1000]:"))
# a = int(input("Введите уровень продаж  для 1 менеджера[ОТ 3-8%]:"))

# if print(r/100*a):
#     print("1 менеджер")


# n = int(input("Введите сумму продаж для 2 менеджера [ОТ 500-1000]:"))
# b = int(input("Введите уровень продаж  для 2 менеджера[ОТ 3-8%]:"))

# if print(n/100*b):
#  print("2 менеджер")


# m = int(input("Введите сумму продаж для 3 менеджера [ОТ 500-1000]:"))
# c = int(input("Введите уровень продаж  для 3 менеджера[ОТ 3-8%]:"))


# if  print(m/100*c):
#  print("3 менеджер")



# g = int(input("Какой мененджр лучше всех сделал свою работу?: "))

# if not g == 1:
#     print(r/100*a  + 200)
#     print("1 менеджер получает прибавку 200$")

# elif not g == 2:
#     print(n/100*b + 200)
#     print("2 менеджер получает прибавку 200$")

# elif not  g == 3:
#     print(r/100*a + 200)
#     print("3 менеджер получает прибавку 200$")

# else:
#     print("Такого менеджера нет")






#Модуль 3 Цикл: (Часть 1)









# №1








# a = int(input("Ведите число номер 1(начало):"))

# b = int(input("Ведите число номер 2(конец):"))


# for i in range(a, b):
#     print(i)
#     if i == a:
#         print("Начало")
# if i == b:
#         print("Конец")
#         for i in range(a,b+1): 
#  (i%7==0):
#  print(i)
# else a == b:
#         raise RuntimeError
# print('Числа не могут быть одинаковыми')

# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# for i in range(a, b +1):
#     print(i)
#     if i == a:
#         print("Начало")
#     if i == b:
#         print("Конец")
#     if i % 7 == 0:
#         print(f"Найдена кратная 7: {i}")







# №2







# a = int(input("Ведите число номер 1(начало): "))
# b = int(input("Ведите число номер 2(конец): "))

# for i in range(a-1, b-1,-1 ):
#     print(i)
#     if i == a:
#         print("начало:")
#     if i == b:
#         print("конец:")
        
#     if i % 7 == 0:
#         print(f" Найдена кратная 7: {i}")
#     if i % 5 == 0:
#         print(f"Найдена кратная 5: {i}")








# №3







# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# for i in range(a, b +1):
#     print(i)
#     if i == a:
#         print("Начало")
#     if i == b:
#         print("Конец")
#     if i % 3 == 0:
#         print(f"Fizz: {i}")
#     if i % 5 == 0:
#         print(f"Buzz: {i}")
#     if i % 3 and 5 == 0:
#         print(f"Fizz Buzz: {i}")
#     if not i % 3 and 5 == 0:
#         print(f"Cамо число{i}")


# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# for i in range(a, b +1):
#     print(i)
#     if i == a:
#         print("Начало")
#     if i == b:
#         print("Конец")
#     if i % 3 == 0:
#         print(f"Fizz: {i}")
#     if i % 5 == 0:
#         print(f"Buzz: {i}")
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"Fizz Buzz: {i}")
#     if not i % 3 and not i % 5:
#         print(f" не делиться не на 3 не на 5{i}")









#Модуль 3 Цикл: (Часть 2)







# №1







# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# sred_arvmet = 0
# nine_sum = 0

# for i in range(a, b +1):

#     print(i)
#     if i == a:

#         print("Начало")
#     if i == b:

#         print("Конец")
#     if i % 9 == 0:

#         print(f"кратно:{i}")

#     if i % 2 == 0:
#      nine_sum = 0
#      sred_arvmet += 1
#      print(f"четное: {i}")   

#     else: not i % 2 == 0
#     nine_sum  += i
#     sred_arvmet += 1
#     print(f"нечётное: {i}")    

#     print(f"Среднеарифметическое нечетных чисел:{sred_arvmet/nine_sum }")





# №2






# length = int(input("Введите длину линии: "))
# symbol = input("Введите символ для заполнения линии: ")

# for i in range(length):
#     print(symbol)





# №3





# a = int(input("Ведите число больше [0]:"))
# if a < 0 :
#     print("«Number is positive»")
# if 0 > a: 
#     print("«Number is negative»")
# else:
#     print("Number is equal to zero")

# if a == 7:
#     print("Good bye!")
        



#№4





# a = int(input("Ведите число 1:"))
# b = int(input("Ведите число 2:"))
# c = int(input("Ведите число 3:"))
# 19

# if a > b and a > c:
#  print("Макимально число[A]:", a)

# elif b > a and b > c:
#  print("Макимально число[B]:", b)


# elif c > a and c > b:
#  print("Макимально число[С]:", c)






# Модуль 3 Циклы.(Часть 3)





# # №1




# x = int(input("Ведите чётное число [1]:"))

# y = int(input("Ведите чётное число [2]:"))

# результат = pow(x,y)

# print(результат)








# №2
# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.







# count = 0 
# for i in range(100, 1000): 
#     num = str(i) 
#     if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]: 
#         count += 1 
# print(count)








# №3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.








# count = 0
# for i in range(100, 10000):
#     num = str(i)
#     if num[0] != num[1] and num[0] != num[2] and num[0] != num[
#         3] and num[1] != num[2] and num[1] != num[3] and num[2]
#         != num[3]:
#         count += 1
# print(count)







# №4
# Пользователь вводит любое целое число. Необхо-
# димо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.








# a = int(input("Ведите любое целое число:"))

# ???????









# Модуль 3 Циклы.(Часть 4)








# №1
# Показать на экран все простые числа в диапазоне,
# указанном пользователем. Число называется простым,
# если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.









# a = int(input("Ведите число которое будет являться начлом диапозонна: "))

# b = int(input("Ведите число которое будет являться концом диапозонна: "))

# for i in range(a,b +1):

#     is_prime = True
    

#     for j in range(2, i):

#         if i % j == 0:

#             is_prime = False
           
#             break

#     if is_prime:

#         print(f"{i}-простое число:")







# №2
# Показать на экране таблицу умножения для всех чисел
# от 1 до 10 Например:






# 1 * 1 = 1 1 * 2 = 2 ….. 1 * 10 = 10
# .........................................................................
# 10 * 1 = 10 10 * 2 = 20 …. 10 * 10 = 100


# for x in range(1,11):

#  for y in range(1,11):
#   print(f"{x} * {y} = {x*y}")
#   print()






# №3
# Показать на экран таблицу умножения в диапазоне,
# указанном пользователем. Например, если пользователь
# указал 3 и 5, таблица может выглядеть так






# 3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
# .....................................................................................
# 5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50

# a = int(input("Ведите число которое будет являться начлом диапозонна: "))
# b = int(input("Ведите число которое будет являться концом диапозонна: "))
# for x in range(a,b +1):
#     for y in range(1,11):
#         print(f"{x} * {y} = {x*y}")






# Модуль 3 Циклы.(Часть 5)





# №1
 







# while True:
#     variant = input('Введите вариант от "а" до "к"')
#     length = int(input('Ведите нечётно число'))
#     string = ''
#     for y in range(length):
#         for x in range(length):
#             match variant:
#                 case 'а':
#                     if y <= x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'б':
#                     if y >= x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'в':
#                     if y == x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'г':
#                     if y + x == length - 1:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'д':
#                     if y == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'е':
#                     if y == x or y == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'ж':
#                     if y == x or y == length - 1 - x or y + x == length - 1:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'з':
#                     if y == x or y == length - 1 - x or y + x == length - 1 or y + x == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'и':
#                     if y == x or y == length - 1 - x or y + x == length - 1 or y + x == length - 1 - x or y == length - 1 - x or y + x == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'к':
#                     if y == x or y == length - 1 - x or y + x == length - 1 or y + x == length - 1 - x or y == length - 1 - x or y + x == length - 1 - x or y + x == length - 1 or y + x == length:
#                         string += "*"
#                     else:
#                         string += " "
#                 case _:
#                     pass
#             string += "\n"
#         print(string)








# Модуль 4 Строки. Списки.(Часть 1)







#№1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палин-
# дром - слово или текст,которое читаеться одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.

# def palindrom():

#     string = input("Введите строку: ")

#     string = string.lower()

#     string = string.replace(" ", "")

#     if string == string[::-1]: ## Проверяет, является ли строка такой же, если изменить ее местами,если не находит слово которое не меняеться  то  выводит принт.

#         print("Строка является палиндромом")

#     else:

#         print("Строка не является палиндромом")

# palindrom()








#№2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.







# def palindrom():

#     string = input("Введите строку: ")

    # string = string.lower() ##Получаем вводимые пользователем данные и преобразуем их в нижний регистр

#     string = string.replace(" ", "") ## Убираем пробелы из строки

#     string = string.split()

#     print(string)

#     for i in string:

#         if i in string: ## Проверить, не появляется ли какой-либо символ в строке более одного разадля i в строке:

#             print(i.upper())


# palindrom()






# №3
# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат.





# def palindrom():

# string = input("Введите строку: ")

# string = string.lower()##-Метод - lower() ##используется для преобразования строки в нижний регистр.

# string = string.replace(" ", "")##-Метод - replace() ##используется для удаления пробелов из строки.

# string = string.split(".")##-Метод split() ##используется для разделения строки на список подстрок с использованием символа "." в качестве разделителя.

# print(string)##-Функция - print() ##используется для печати списка подстрок и его длины.

# print(len(string))##-Функция - len()## используется для получения длины списка подстрок.






# Модуль 4 Строки. Списки.(Часть 2)






#№1 
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35 Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/







# def palindrom():

#     string = input("Введите арифметическое выражение: ") ##Предлагает пользователю ввести арифметическое выражение, например "2 + 3" или "4 * 5".

#     string = string.split() ##string = строка.split(): Разбивает входную строку на список слов, используя пробел в качестве разделителя. Например, "2 + 3" станет ["2", "+", "3"].

#     print(string) ##выводит список слов на консоль.

#     print(string[0]+string[2]) ##выводит объединение первого и третьего элементов списка. В приведенном выше примере это означало бы вывод "23".

# palindrom()







# №2
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.






# import random

# def palindrom():

#     list = [random.randint(-100, 100) for i in range(21)] ##

#     print(list)

#     print(max(list)) ##выводит максимальный элемент списка.

#     print(min(list)) ##выводит минимальный элемент списка.

#     print(list.count(0)) ##выводит количество нулей в списке.
    
#     countOtr = 0
#     for n in list:
#         if n < 0:
#             countOtr += 1
#     print(countOtr) ##выводит количество отрицательных элементов в списке
    
#     countPol = 0
#     for n in list:
#         if n > 0:
#             countPol += 1
#     print(countPol) ##выводит количество положительных элементов в списке

# palindrom()







# Модуль 4 Строки. Списки.(Часть 3)





# №1 
# Два списка целых заполняются случайными числами.
# Необходимо:
# Сформировать третий список, содержащий элементы
# обоих списков;
# Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# Сформировать третий список, содержащий элементы
# общие для двух списков;
# Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков






## Два списка целых заполняются случайными числами.
## Необходимо:

# import random
# def task1():
#      print
# list1 = [random.randint(-100, 100) for _ in range(10)]

# list2 = [random.randint(-100, 100) for _ in range(10)]

# print("List 1:", list1)
# print("List 2:", list2)

# # Сформировать третий список, содержащий элементы
# # обоих списков;

# list3 = list1 + list2
# print("List 3:", list3)

# # формировать третий список, содержащий элементы
# # обоих списков без повторений;

# list4 = list(set(list1 + list2))
# print("List 4:", list4)

# # Сформировать третий список, содержащий элементы
# # общие для двух списков;

# list5 = list(set(list1) & set(list2))
# print("List 5:", list5)

# # Сформировать третий список, содержащий только
# # уникальные элементы каждого из списков;

# list6 = list(set(list1) ^ set(list2))
# print("List 6:", list6)
 
# # минимальное и максимальное значение каждого из
# # списков

# list7 = [min(list1), max(list1), min(list2), max(list2)]
# print("List 7:", list7)
# task1()







# Модуль 5 Функции. Функции.(Часть 1)








# Задание 1
## Напишите функцию, которая отображает на экран
## форматированный текст, указанный ниже:
## “Don't compare yourself with anyone in this world…
## if you do so, you are insulting yourself.”
##                                           Bill Gates






# print("“Don't compare yourself with anyone in this world…")
# print ("if you do so, you are insulting yourself.”")
# print("                                           Bill Gates")






# Задание 2
## Напишите функцию, которая принимает два числа
## в качестве параметра и отображает все четные числа
## между ними






# def print_even_numbers(a, b):
#     for i in range(a, b+1):
#         if i % 2 == 0:
#             print(i)
# print_even_numbers(1, 10)








# Задание 3
## Напишите функцию, которая отображает пустой или
## заполненный квадрат из некоторого символа. Функция
## принимает в качестве параметров: длину стороны ква-
## драта, символ и переменную логического типа
## если она равна True, квадрат заполненный
## если False, квадрат пустой







## (True или False), указывающую, является ли квадрат
##  пустым или заполненным

# def print_square(size, symbol, is_empty):
#     if is_empty:
#         for i in range(size):
#             if i == 0 or i == size - 1:
#                 print(symbol * size)
#             else:
#                 print(symbol + " " * (size - 2) + symbol)
#     else:
#         for i in range(size):
#             print(symbol * size)
# print_square(5, '*', True)







## Задание 4
## Напишите функцию, которая возвращает минимальное
## из пяти чисел Числа передаются в качестве параметров









# import random 
# import math

# def min_of_five(a, b, c, d, e):
#     return min(a, b, c, d, e)

# print(min_of_five(1, 2, 3, 4, 5))

# print(min_of_five(random.randint(1,5), random.randint(1,5)
                  
# , random.randint(1,5), random.randint(1,5), random.randint
# (1,5)))

# print(min_of_five(math.pi, math.e, math.sqrt(2), math.sqrt(3)
# , math.sqrt(5)))



## Этот код определяет функцию min_of_five, которая принимает пять аргументов и возвращает минимальное значение из них. Затем функция вызывается три раза с разными наборами аргументов:

## С числами 1, 2, 3, 4 и 5.
## С пятью случайными целыми числами от 1 до 5.
## С пятью математическими константами: π, e, √2, √3 и √5.
## Вот краткое описание того, как работает код:

## Первый вызов:


## Печать кода копирования(min_of_five(1, 2, 3, 4, 5))
## Функция min_of_five вызывается с аргументами 1, 2, 3, 4 и 5. Функция min возвращает наименьшее значение из этих аргументов, равное 1. Результатом будет 1.

## Второй вызов:


## Печать кода копирования(min_of_five(random.randint(1,5), random.randint(1,5),
## random.randint(1,5), random.randint(1,5), random.randint(1,5)))
## Функция min_of_five вызывается с пятью случайными целыми числами от 1 до 5. Функция random.randint генерирует случайное целое число от 1 до 5 для каждого аргумента. Функция min возвращает наименьшее значение из этих случайных целых чисел


# import random
# import math

# def min_of_five(args):
#     return min(args)

# print(min_of_five([1, 2, 3, 4, 5]))

# print(min_of_five([random.randint(1,5) for _ in range(5)]))

# print(min_of_five([math.pi, math.e, math.sqrt(2), math.sqrt(3), math.sqrt(5)]))







## Задание 5
## Напишите функцию, которая возвращает произве-
## дение чисел в указанном диапазоне. Границы диапазона
## передаются в качестве параметров. Если границы диапа-
## зона перепутаны (наппример, 5- верхняя граница,25-)
## нижняя граница), их нужно поменять местами






# import math
# def product_of_range(a, b):
#     if a > b:
#         a, b = b, a
#     product = 1
#     for i in range(a, b + 1):
#         product *= i
#     return product
# print(product_of_range(5, 25))
# print(product_of_range(25, 5))






## Задание 6
## Напишите функцию, которая считает количество
## цифр в числе. Число передаётся в качестве параметра. Из
## функции нужно вернуть полученное количество цифр.
## Например, если передали 3456, количество цифр будет 4






# def count_digits(n):
#     return len(str(abs(n)))
# print(count_digits(3456))
# print(count_digits(-3456))







## Задание 7
## Напишите функцию, которая проверяет является ли
## число палиндромом. Число передаётся в качестве пара-
## метра. Если число палиндром нужно вернуть из функции
## true, иначе false.
## «Палиндром» — это число, у которого первая часть
## цифр равна второй перевернутой части цифр. Например,
## 123321 — палиндром (первая часть 123, вторая 321, которая
## после переворота становится 123), 546645 — палиндром,
## а 421987 — не палиндром.





# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# print(is_palindrome(123321)) # True
# print(is_palindrome(546645)) # True
# print(is_palindrome(421987)) # False





## Модуль 5 Функции. Функции.(Часть 2)







## Задание 1
## Напишите функцию, вычисляющую произведение
## элементов списка целых. Список передаётся в качестве па-
## раметра. Полученный результат возвращается из функции







# def product_of_list(lst):

#     product = 1

#     for i in lst:

#         product *= i

#     return product

# print(product_of_list([1, 2, 3, 4, 5]))


## 1. def product_of_list(lst):: Эта строка определяет функцию с именем product_of_list, которая принимает единственный аргумент lst, представляющий собой список чисел.

## 2. product = 1: В этой строке переменная product инициализируется значением 1. Эта переменная будет использоваться для хранения результатов всех элементов в списке.

## 3. for i в lst:: Эта строка запускает цикл for, который будет выполнять итерацию по каждому элементу i в списке lst.

## 4. product *= i: Внутри цикла эта строка умножает текущее значение product на текущий элемент i. Это делается с помощью оператора *=, который является сокращением от product = продукт * i.

## 5. возвращает product: После того, как цикл завершает итерацию по всем элементам в списке, эта строка возвращает конечное значение product, которое является произведением всех элементов в списке.



## Теперь давайте посмотрим, как эта функция работает с примером входных данных [1, 2, 3, 4, 5]:

## Итерация 1: product = 1 i = 1 product *= 1 => product = 1

## Итерация 2: product = 1 i = 2 product *= 2 => продукт = 2







## Задание 2
## Напишите функцию для нахождения минимума в
## списке целых. Список передаётся в качестве параметра.
## Полученный результат возвращается из функции






# def find_min(lst):

#     return min(lst)

# numbers = [4, 2, 9, 1, 7, 3]

# min_value = find_min(numbers)

# print(min_value)  # Output: 1







## Задание 3
## Напишите функцию, определяющую количество про-
## стых чисел в списке целых. Список передаётся в качестве
## параметра. Полученный результат возвращается из функции







# def count_even_numbers(lst):

#     count = 0

#     for num in lst:

#         if num % 2 == 0:

#             count += 1

#     return count

# numbers = [1, 2, 3, 4, 5, 6]

# even_count = count_even_numbers(numbers)

# print(even_count)  # Output: 3







## Задание 4
## Напишите функцию, удаляющую из списка целых
## некоторое заданное число. Из функции нужно вернуть
## количество удаленных элементов







# def remove_number(lst, num):

#     count = 0

#     for i in range(len(lst) - 1, -1, -1):

#         if lst[i] == num:

#             lst.pop(i)

#             count += 1

#             return count
        
#         return count
    
#     numbers = [1, 2, 2, 3, 2, 4,]

#     removed_count = remove_number(numbers, 2)

#     print(removed_count)  # Output: 3






## Задание 5
## Напишите функцию, которая получает два списка в
## качестве параметра и возвращает список, содержащий
## элементы обоих списков






# def merge_lists(list1, list2):

#     return list1 + list2

# list1 = [1, 2, 3]

# list2 = [4, 5, 6]

# print(merge_lists(list1, list2))  # Output: [1, 2,]







## Задание 6
## Напишите функцию, высчитывающую степень каждого
## элемента списка целых. Значение для степени передаётся
## в качестве параметра, список тоже передаётся в качестве
## параметра. Функция возвращает новый список, содержа-
## щий полученные результаты





# def merge_lists(lst):

#     return [i**2 for i in lst]

# def power_list(lst, power):
         
#          return [i**power for i in lst]

# list1 = [1, 2, 3, 4, 5]

# print(power_list(list1, 2))  # Output: [1, 4, 9]





## Модуль 5 Функции. Функции.(Часть 3)





## Задание 1
## Написать рекурсивную функцию нахождения наи-
## большего общего делителя двух целых чисел





# def gcd(a, b):

#     if b == 0:

#         return a
    
#     else:

#         return gcd(b, a % b) 
    
# print(gcd(12, 15))  # Output: 3











# Задание 2
# Написать игру «Быки и коровы». Программа «за-
# гадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа
# сообщает, сколько цифр числа угадано (быки) и сколько
# цифр угадано и стоит на нужном месте (коровы). После
# отгадывания числа на экран необходимо вывести коли-
# чество сделанных пользователем попыток. В программе
# необходимо использовать рекурсию







# import random

# def game():

#     number = str(random.randint(1000, 9999))  # загадываем число

#     attempts = 0

#     while True:

#         guess = input("Введите четырёхзначное число: ")

#         if len(guess) != 4 or not guess.isdigit():

#             print("Некорректный ввод. Введите четырёхзначное число")

#             continue

#         attempts += 1

#         bulls = 0

#         cows = 0

#         for i in range(4):

#             if guess[i] == number[i]:

#                 bulls += 1

#             elif guess[i] in number:
             
#              cows += 1

#             print(f"Быки: {bulls}, Коровы: {cows}")

#             if bulls == 4:
             
#              print(f"Вы угадали! Количество попыток: {attempts}")
#             break
        
# game() # запуск игры

        

## Вот пошаговое объяснение того, как работает код:

## 1. Импорт модуля random

## Код начинается с импорта модуля random, который используется для генерации случайного числа.

## 2. Определение функции game()

## Определена функция game(), которая будет содержать логику игры.

## 3. Генерация случайного числа

## Переменной number задается случайное четырехзначное число с помощью random.randint(1000, 9999). Это число будет секретным номером, который пользователь должен угадать.

## 4. Инициализация переменной attempts

## Переменной attempts присваивается значение 0, которое будет отслеживать количество попыток пользователя угадать число.

## 5. Вход в игровой цикл

## Код переходит в бесконечный цикл, используя while True:. Этот цикл будет продолжаться до тех пор, пока пользователь правильно не угадает число.

## 6. Получение пользовательского ввода

## Пользователю предлагается ввести четырехзначное число с помощью ввода("Введите значение: "). Введенные данные сохраняются в переменной guess.

## 7. Проверка правильности ввода пользователем

## Код чепроверьте правильность введенных пользователем данных, проверив, составляет ли длина введенных данных 4 символа и все ли символы являются цифрами, используя len(угадайте) != 4 или не угадывайте.isdigit(). Если вводимые данные неверны, выводится сообщение об ошибке, и цикл продолжается.

## 8. Увеличение переменной attempts

## Если вводимые данные верны, переменная attempts увеличивается на 1.

## 9. Инициализация переменных bulls и cows

## Переменным bulls и cows присваивается значение 0. Эти переменные будут использоваться для отслеживания количества правильных цифр в правильном положении (bulls) и количества правильных цифр в неправильном положении (cows).

## 10. Сравнение догадки с секретным номером

## Код повторяет каждую цифру предположения и сравнивает ее с соответствующей цифрой секретного номера, используя значение для i в диапазоне(4):. Если цифра совпадает в точности, это увеличивает значение переменной bulls. Если в секретном номере присутствует цифра, но она находится в неправильном положении, значение переменной cows увеличивается.

## 11. Вывод результата на печать

## Код выводит количество быков и коров с помощью print(f"Быки: {быки}, Коровы: {коровы}").

## 12. Проверяем, выиграл ли пользователь

## Если количество буллов равно 4, это означает, что пользователь правильно угадал число, и игра выиграна. Код выводит поздравительное сообщение с количеством попыток, сделанных с помощью print("Спасибо! Количество попыток: {attempts}").

## 13. Выход из цикла

## Если пользователь выиграл, код выходит из цикла с помощью break.

## 14. Запуск игры

## Наконец, для запуска игры вызывается функция game().








## Задание 4
## Написать игру «Пятнашки».









# def game():
    
#     import random

# # Заготовки для отображения поля
# up = """+-----+-----+-----+-----+
# |     |     |     |     |"""
# mid = """|     |     |     |     |
# +-----+-----+-----+-----+
# |     |     |     |     |"""
# bot = """|     |     |     |     |
# +-----+-----+-----+-----+"""

# def get_new_random():
#     line = list(range(16))
#     return line

# def print_board(new_game):
#     print(up)
#     for i in range(0, 16):
#         if new_game[i]<10:
#             if new_game[i] == 0:
#                 print('| ', end = '')
#             else:
#                 print('| '+str(new_game[i])+' ', end = '')
#         else:
#             num = str(new_game[i])
#             print('| '+num[0]+' '+num[1]+' ', end = '')
#         if i == 3 or i == 7 or i == 11:
#             print('|')
#             print(mid) 
#     print('|')
#     print(bot)

# def ansver():
#     while True:
#         text = input('Введите число от 1 до 15:')
#         if text.isdigit() == False:
#             print('Вводите только целые числа!')
#         elif 15<int(text) or int(text)<0:
#             print('Нет такого числа на игровом поле!')
#         else:
#             return int(text)

# def possible_moves(new_game):
#     moves = []
#     ind = new_game.index(0)
#     if ind == 0:
#         moves.append(new_game[1])
#         moves.append(new_game[4])
#     elif ind == 1:
#         moves.append(new_game[0])
#         moves.append(new_game[2])
#         moves.append(new_game[5])
#     elif ind == 2:
#         moves.append(new_game[1])
#         moves.append(new_game[3])
#         moves.append(new_game[6])
#     elif ind == 3:
#         moves.append(new_game[2])
#         moves.append(new_game[7])
#     elif ind == 4:
#         moves.append(new_game[0])
#         moves.append(new_game[5])
#         moves.append(new_game[8])
#     elif ind == 5:
#         moves.append(new_game[1])
#         moves.append(new_game[4])
#         moves.append(new_game[6])
#         moves.append(new_game[9])
#     elif ind == 6:
#         moves.append(new_game[2])
#         moves.append(new_game[5])
#         moves.append(new_game[7])
#         moves.append(new_game[10])
#     elif ind == 7:
#         moves.append(new_game[3])
#         moves.append(new_game[6])
#         moves.append(new_game[11])
#     elif ind == 8:
#         moves.append(new_game[4])
#         moves.append(new_game[9])
#         moves.append(new_game[12])
#     elif ind == 9:
#         moves.append(new_game[5])
#         moves.append(new_game[8])
#         moves.append(new_game[10])
#         moves.append(new_game[13])
#     elif ind == 10:
#         moves.append(new_game[6])
#         moves.append(new_game[9])
#         moves.append(new_game[11])
#         moves.append(new_game[14])
#     elif ind == 11:
#         moves.append(new_game[7])
#         moves.append(new_game[10])
#         moves.append(new_game[15])
#     elif ind == 12:
#         moves.append(new_game[8])
#         moves.append(new_game[13])
#     elif ind == 13:
#         moves.append(new_game[9])
#         moves.append(new_game[12])
#         moves.append(new_game[14])
#     elif ind == 14:
#         moves.append(new_game[10])
#         moves.append(new_game[13])
#         moves.append(new_game[15])
#     else:
#         moves.append(new_game[11])
#         moves.append(new_game[14])
#     return moves

# # Основной код игры
# win = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# new_game = get_new_random()
# print_board(new_game)

# while True:
#     moves = possible_moves(new_game)
#     move_num = ansver()
#     if move_num in moves:
#         ind_move = new_game.index(move_num)
#         ind_0 = new_game.index(0)
#         new_game[ind_0] = move_num
#         new_game[ind_move] = 0
#         print_board(new_game)
#     else:
#         print('Это число нельзя переместить!')
#     if new_game == win:
#         print('Поздравляю! Вы победили!')
#         break







## Модуль 7 Сортировка и поиск. Сортировка и поиск(Часть 1)






## Задание 1
## Необходимо отсортировать первые две трети списка
## в порядке возрастания, если среднее арифметическое
## всех элементов больше нуля; иначе — лишь первую треть.
## Остальную часть списка не сортировать, а расположить
## в обратном порядке.







# def sort_list(lst):
#     n = len(lst)
#     avg = sum(lst) / n
#     if avg > 0:
#         lst[:2*n//3] = sorted(lst[:2*n//3])
#     else:
#         lst[:n//3] = sorted(lst[:n//3])
#         lst[n//3:] = lst[n//3:][::-1]
#     return lst

# lst = [1, 2, 3, 4, 5, 6]
# print(sort_list(lst)) # [1, 2, 3, 6,]
# print = 








## Задание 2
## Написать программу «успеваемость». Пользователь
## вводит 10 оценок студента. Оценки от 1 до 12 Реализовать
## меню для пользователя:
## ■ Вывод оценок (вывод содержимого списка);
## ■ Пересдача экзамена (пользователь вводит номер эле-
## мента списка и новую оценку);
## ■ Выходит ли стипендия (стипендия выходит, если
## средний бал не ниже 10.7);
## ■ Вывод отсортированного списка оценок: по возрас-
## танию или убыванию







# def sort_list(lst):

#     n = len(lst)

#     avg = sum(lst) / n

#     if avg > 10.7:

#         return True

#     else:

#       return false

# lst = [1, 2, 3, 4, 5, 6]
# print(sorted(lst))
# print(sorted(lst)[::-1])
# print(sort_list(lst)) # [1, 2, 3, 6,]








# Задание 3
## Написать программу, реализующую сортировку списка
## методом усовершенствованной сортировки пузырьковым
## методом. Усовершенствование состоит в том, чтобы ана-
## лизировать количество перестановок на каждом шагу, если
## это количество равно нулю, то продолжать сортировку
## нет смысла — список отсортирован







# lst = [1, 2, 3, 4, 5, 6]

# def sort_list(lst):

#     n = len(lst)

#     for i in range(n - 1):

#         count = 0

#         for j in range(n - i - 1):

#             if lst[j] > lst[j + 1]:

#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

#                 count += 1

#         if count == 0:

#             break

#     return lst







## Модуль 7 Сортировка и поиск.
## Тема: Сортировка и поиск. Часть 2






## Задание 1








## Написать программу «справочник». Создать два списка
## целых. Один список хранит идентификационные коды,
## второй — телефонные номера. Реализовать меню для
## пользователя:
## Отсортировать по идентификационным кодам;
## Отсортировать по номерам телефона;
## Вывести список пользователей с кодами и телефонами;
## Выход


# lst1 = ['123', '456', '789', '012', '345', '678']
# lst2 = ['+79394593', '+724904480294', '+724940934566', '+7435352525', '+734536346', '+74636326226']

# def insertion_sort(a1:list, a2:list):
#     if (len(a1)!=len(a2)):
#         raise ValueError('len not equals')
#     n = len(a1)
#     for i in range(1, n):
#         x = a1[i]
#         j = i
#         z = a2[i]
#         while j > 0 and a1[j - 1] > x:
#             a1[j] = a1[j - 1]
#             a2[j] = a2[j - 1]
#             j -= 1

#         a1[j] = x
#         a2[j] = z

# insertion_sort(lst1,lst2)
# print(lst1)    
# print(lst2)    
# insertion_sort(lst2,lst1)
# print(lst1)    
# print(lst2)    







# Задание 2
## Написать программу «успеваемость». Пользователь
## вводит 10 оценок студента. Оценки от 1 до 12 Реализовать
## меню для пользователя:
## ■ Вывод оценок (вывод содержимого списка);
## ■ Пересдача экзамена (пользователь вводит номер эле-
## мента списка и новую оценку);
## ■ Выходит ли стипендия (стипендия выходит, если
## средний бал не ниже 10.7);
## ■ Вывод отсортированного списка оценок: по возрас-
## танию или убыванию.
## ■ Выход.









            ## Инициализируйте пустой список для хранения оценок
# grades = []

# ## Предложите пользователю ввести 10 оценок
# for i in range(10):
#     while True:
#         grade = int(input(f"Введите оценку {i+1} (1-12): "))
#         if 1 <= grade <= 12:
#             grades.append(grade)
#             break
#         else:
#             print("Неверная оценка. Пожалуйста, попробуйте снова.")

# ## Определите функцию для вычисления среднего балла
# def calculate_average():
#     return sum(grades) / len(grades)

# ## Определите функцию для проверки того, имеет ли студент право на получение стипендии
# def is_scholarship_eligible():
#     return calculate_average() >= 10.7

# ## Определите функцию для сортировки оценок в порядке возрастания или убывания
# def sort_grades(order):
#     if order == "asc":
#         return sorted(grades)
#     elif order == "desc":
#         return sorted(grades, reverse=True)
#     else:
#         print("Недействительный заказ. Пожалуйста, попробуйте снова.")

# ## Цикл работы главного меню
# while True:
#     print("\nАкадемическое меню выступлений:")
#     print("1. Просмотр оценок")
#     print("2. Пересдать экзамен")
#     print("3. Проверьте право на получение стипендии")
#     print("4. Сортировка оценок")
#     print("5. Выход")
#     choice = input("Введите свой выбор: ")

#     if choice == "1":
#         print("Оценки:", grades)
#     elif choice == "2":
#         index = int(input("Введите номер экзамена для пересдачи (1-10): ")) - 1
#         if 0 <= index < 10:
#             new_grade = int(input("Переход в новый класс (1-12): "))
#             grades[index] = new_grade
#             print("Оценка успешно обновлена!")
#         else:
#             print("Неверный номер экзамена. Пожалуйста, попробуйте снова.")
#     elif choice == "3":
#         if is_scholarship_eligible():
#             print("Студент имеет право на получение стипендии!")
#         else:
#             print("Студент не имеет права на получение стипендии.")
#     elif choice == "4":
#         order = input("Введите порядок сортировки (asc/desc): ")
#         sorted_grades = sort_grades(order)
#         print("Отсортированные сорта:", sorted_grades)
#     elif choice == "5":
#         print("До свидания!")
#         break
#     else:
#         print("Неверный выбор. Пожалуйста, попробуйте снова.")









## Модуль 7 Сортировка и поиск.
## Тема: Сортировка и поиск. Часть 3








## Задание 1
## Есть четыре списка целых. Необходимо их объединить
## в пятом списке. Полученный результат в зависимости от
## выбора пользователя отсортировать по убыванию или
## возрастанию. Найти значение, введенное пользователем,
## с использованием линейного поиска.
## Вывести результат на экран.

## Определите четыре списка целых чисел
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3 = [9, 10, 11, 12]
# list4 = [13, 14, 15, 16]

# ## Объедините четыре списка в один
# combined_list = list1 + list2 + list3 + list4

# ## Попросите пользователя выбрать порядок сортировки
# print("Выберите порядок сортировки:")
# print("1. Восходящий")
# print("2. Нисходящий")
# choice = int(input("Введите свой выбор: "))

# ## Отсортируйте объединенный список на основе выбора пользователя
# if choice == 1:
#     combined_list.sort()
#     print("Отсортированный список в порядке возрастания:", combined_list)
# elif choice == 2:
#     combined_list.sort(reverse=True)
#     print("Отсортированный список в порядке убывания:", combined_list)
# else:
#     print("Неверный выбор. Выходящий.")

# ## Попросите пользователя ввести значение для поиска
# search_value = int(input("Введите значение для поиска: "))

# ## Выполнять линейный поиск
# found = False
# for i, value in enumerate(combined_list):
#     if value == search_value:
#         found = True
#         print(f"Ценность {search_value} найдено по индексу {i}")
#         break

# if not found:
#     print(f"Ценность {search_value} не найден в списке")








## Задание 2
## Есть четыре списка целых. Необходимо объединить
## в пятом списке только те элементы, которые уникальны
## для каждого списка. Полученный результат в зависимости
## от выбора пользователя отсортировать по убыванию или
## возрастанию. Найти значение, введенное пользователем,
## с использованием бинарного поиска






# def unique_elements(list1, list2, list3, list4):
#     ## Объедините все списки в один
#     combined_list = list1 + list2 + list3 + list4
    
#     ## Найдите уникальные элементы в объединенном списке
#     unique_list = [x for x in combined_list if combined_list.count(x) == 1]
    
#     return unique_list

# def sort_list(unique_list, order):
#     if order == 'asc':
#         return sorted(unique_list)
#     elif order == 'desc':
#         return sorted(unique_list, reverse=True)
#     else:
#         return "Неверный заказ. Пожалуйста, выберите 'asc' или 'desc'."

# def binary_search(sorted_list, target):
#     low = 0
#     high = len(sorted_list) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
#         if sorted_list[mid] == target:
#             return mid
#         elif sorted_list[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
    
#     return -1

# ## Пример использования
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# list3 = [5, 6, 7, 8]
# list4 = [7, 8, 9, 10]

# unique_list = unique_elements(list1, list2, list3, list4)
# print("Уникальные элементы:", unique_list)

# order = input("Введите 'asc' для возрастания или 'desc' для убывания: ")
# sorted_list = sort_list(unique_list, order)
# print("Отсортированный список:", sorted_list)

# target = int(input("Введите номер для поиска: "))
# index = binary_search(sorted_list, target)

# if index != -1:
#     print("Элемент, найденный по индексу", index)
# else:
#     print("Элемент не найден")

## Модуль 8 Кортежи, множества, словари
## Тема: Кортежи, множества, словари. Часть 1






## Задание 1
## Есть три кортежа целых чисел необходимо найти
## элементы, которые есть во всех кортежах






# # t1 = (1, 2, 3, 4, 5)
# t2 = (4, 5, 6, 7, 8)
# t3 = (4, 5, 9, 10, 11)

# s1 = set(t1)
# s2 = set(t2)
# s3 = set(t3)

# common_elements = s1 & s2 & s3

# print(common_elements)  # {4, 5}






## Задание 2
## Есть три кортежа целых чисел необходимо найти
## элементы, которые уникальны для каждого списка.






# t1 = (1, 2, 3, 4, 5)
# t2 = (4, 5, 6, 7, 8)
# t3 = (4, 5, 9, 10, 11)

# s1 = set(t1)
# s2 = set(t2)
# s3 = set(t3)

# unique_in_t1 = s1 - s2 - s3
# unique_in_t2 = s2 - s1 - s3
# unique_in_t3 = s3 - s1 - s2

# print("Уникальные элементы в t1:", unique_in_t1)  # {1, 2, 3}
# print("Уникальные элементы в t2:", unique_in_t2)  # {6, 7, 8}
# print("Уникальные элементы в t3:", unique_in_t3)  # {9, 10, 11}





## Задание 3
## Есть три кортежа целых чисел необходимо найти эле-
## менты, которые есть в каждом из кортежей и находятся
## в каждом из кортежей на той же позиции.





# t1 = (1, 2, 3, 4, 5)
# t2 = (1, 2, 3, 6, 7)
# t3 = (1, 2, 3, 8, 9)

# common_elements = [x for x, y, z in zip(t1, t2, t3) if x == y == z]

# print(common_elements)  # [1, 2, 3]






## Модуль 8 Кортежи, множества, словари
## Тема: Кортежи, множества, словари. Часть 2






## Задание 1
## Создайте программу, хранящую информацию о вели-
## ких баскетболистах. Нужно хранить ФИО баскетболиста и
## его рост. Требуется реализовать возможность добавления,
## удаления, поиска, замены данных. Используйте словарь
## для хранения информации.







# Создаем пустой словарь для хранения информации о баскетболистах
# basketball_players = {}

# def add_player():
#     # Добавляем нового баскетболиста
#     name = input("Введите ФИО баскетболиста: ")
#     height = int(input("Введите рост баскетболиста (в см): "))
#     basketball_players[name] = height
#     print(f"Баскетболист {name} добавлен в список!")

# def delete_player():
#     # Удаляем баскетболиста из списка
#     name = input("Введите ФИО баскетболиста для удаления: ")
#     if name in basketball_players:
#         del basketball_players[name]
#         print(f"Баскетболист {name} удален из списка!")
#     else:
#         print(f"Баскетболист {name} не найден в списке!")

# def search_player():
#     # Ищем баскетболиста по ФИО
#     name = input("Введите ФИО баскетболиста для поиска: ")
#     if name in basketball_players:
#         print(f"Баскетболист {name} найден! Его рост: {basketball_players[name]} см")
#     else:
#         print(f"Баскетболист {name} не найден в списке!")

# def replace_player():
#     # Заменяем информацию о баскетболисте
#     name = input("Введите ФИО баскетболиста для замены: ")
#     if name in basketball_players:
#         new_height = int(input("Введите новый рост баскетболиста (в см): "))
#         basketball_players[name] = new_height
#         print(f"Информация о баскетболисте {name} обновлена!")
#     else:
#         print(f"Баскетболист {name} не найден в списке!")

# def print_players():
#     # Выводим список всех баскетболистов
#     print("Список баскетболистов:")
#     for name, height in basketball_players.items():
#         print(f"{name} - {height} см")

# while True:
#     print("Меню:")
#     print("1. Добавить баскетболиста")
#     print("2. Удалить баскетболиста")
#     print("3. Найти баскетболиста")
#     print("4. Заменить информацию о баскетболисте")
#     print("5. Вывести список баскетболистов")
#     print("6. Выход")
#     choice = int(input("Выберите пункт меню: "))
#     if choice == 1:
#         add_player()
#     elif choice == 2:
#         delete_player()
#     elif choice == 3:
#         search_player()
#     elif choice == 4:
#         replace_player()
#     elif choice == 5:
#         print_players()
#     elif choice == 6:
#         break
#     else:
#         print("Неверный выбор!")







## Задание 2
## Создайте программу «Англо-русский словарь».
## Нужно хранить слово на английском языке и его перевод
## на французский. Требуется реализовать возможность до-
## бавления, удаления, поиска, замены данных. Используйте
## словарь для хранения информации.






# dictionary_wor = {}

# def add_word():
#     # Добавляем новое слово
#     name = input("Введите слово на русском: ")
#     height = input("Введите слово на английском: ")
#     dictionary_wor[name] = height
#     print(f"Слово {name} добавлено в список!")

# def delete_word():
#     # Удаляем слово из списка
#     name = input("Введите слово для удаления: ")
#     if name in dictionary_wor:
#         del dictionary_wor[name]
#         print(f"Слово {name} удалено из списка!")
#     else:
#         print(f"Слово {name} не найдено в списке!")

# def search_word():
#     # Ищем слово на русском
#     name = input("Введите слово для поиска: ")
#     if name in dictionary_wor:
#         print(f"Слово {name} найдено! Это слово по-английски: {dictionary_wor[name]} ")
#     else:
#         print(f"Слово {name} не найдено в списке!")

# def replace_word():
#     # Заменяем информацию о слове
#     name = input("Введите слово на русском для замены: ")
#     if name in dictionary_wor:
#         new_height = input("Введите новое слово на английском: ")
#         dictionary_wor[name] = new_height
#         print(f"Информация о слове {name} обновлена!")
#     else:
#         print(f"Слово {name} не найдено в списке!")

# def print_word():
#     # Выводим список всех слов
#     print("Список слов:")
#     for name, height in dictionary_wor.items():
#         print(f"{name} - {height} ")

# while True:
#     print("Меню:")
#     print("1. Добавить слово")
#     print("2. Удалить слово")
#     print("3. Найти слово")
#     print("4. Заменить информацию о слове")
#     print("5. Вывести список слов")
#     print("6. Выход")
#     choice = int(input("Выберите пункт меню: "))

#     if choice == 1:
#         add_word()
#     elif choice == 2:
#         delete_word()
#     elif choice == 3:
#         search_word()
#     elif choice == 4:
#         replace_word()
#     elif choice == 5:
#         print_word()
#     elif choice == 6:
#         break
#     else:
#         print("Неверный выбор!")






## Задание 3
##  Создайте программу «Фирма». Нужно хранить ин-
##  формацию о человеке: ФИО, телефон, рабочий email,
##  название должности, номер кабинета, skype. Требуется
##  реализовать возможность добавления, удаления, поис-
##  ка, замены данных. Используйте словарь для хранения
##  информации.







# Firm_human = {}

# Firm_human = {}

# def add_human():
#     # Добавляем нового сотрудника
#     name = input("Введите ФИО сотрудника: ")
#     phone = input("Введите телефон сотрудника: ")
#     email = input("Введите email сотрудника: ")
#     position = input("Введите должность сотрудника: ")
#     cabinet = input("Введите номер кабинета сотрудника: ")
#     skype = input("Введите skype сотрудника: ")
#     Firm_human[name] = {
#         "телефон": phone,
#         "email": email,
#         "должность": position,
#         "кабинет": cabinet,
#         "skype": skype
#     }
#     print(f"Сотрудник {name} добавлен в список!")

# def delete_human():
#     # Удаляем сотрудника из списка
#     name = input("Введите ФИО сотрудника для удаления: ")
#     if name in Firm_human:
#         del Firm_human[name]
#         print(f"Сотрудник {name} удален из списка!")
#     else:
#         print(f"Сотрудник {name} не найден в списке!")

# def search_human():
#     # Ищем сотрудника по ФИО
#     name = input("Введите ФИО сотрудника для поиска: ")
#     if name in Firm_human:
#         print(f"Сотрудник {name} найден!")
#         print(f"Телефон: {Firm_human[name]['телефон']}")
#         print(f"Email: {Firm_human[name]['email']}")
#         print(f"Должность: {Firm_human[name]['должность']}")
#         print(f"Кабинет: {Firm_human[name]['кабинет']}")
#         print(f"Skype: {Firm_human[name]['skype']}")
#     else:
#         print(f"Сотрудник {name} не найден в списке!")

# def replace_human():
#     # Заменяем информацию о сотруднике
#     name = input("Введите ФИО сотрудника для замены: ")
#     if name in Firm_human:
#         phone = input("Введите новый телефон сотрудника: ")
#         email = input("Введите новый email сотрудника: ")
#         position = input("Введите новую должность сотрудника: ")
#         cabinet = input("Введите новый номер кабинета сотрудника: ")
#         skype = input("Введите новый skype сотрудника: ")
#         Firm_human[name] = {
#             "телефон": phone,
#             "email": email,
#             "должность": position,
#             "кабинет": cabinet,
#             "skype": skype
#         }
#         print(f"Информация о сотруднике {name} обновлена!")
#     else:
#         print(f"Сотрудник {name} не найден в списке!")

# def print_human():
#     # Выводим список всех сотрудников
#     print("Список сотрудников:")
#     for name, info in Firm_human.items():
#         print(f"{name}:")
#         print(f"Телефон: {info['телефон']}")
#         print(f"Email: {info['email']}")
#         print(f"Должность: {info['должность']}")
#         print(f"Кабинет: {info['кабинет']}")
#         print(f"Skype: {info['skype']}")
#         print()

# while True:
#     print("Меню:")
#     print("1. Добавить сотрудника")
#     print("2. Удалить сотрудника")
#     print("3. Найти сотрудника")
#     print("4. Заменить информацию о сотруднике")
#     print("5. Вывести список сотрудников")
#     print("6. Выход")
#     choice = int(input("Выберите пункт меню: "))

#     if choice == 1:
#         add_human()
#     elif choice == 2:
#         delete_human()
#     elif choice == 3:
#         search_human()
#     elif choice == 4:
#         replace_human()
#     elif choice == 5:
#         print_human()
#     elif choice == 6:
#         break
#     else:
#         print("Неверный выбор!")






## Задание 4
## Создайте программу «Книжная коллекция». Нужно
## хранить информацию о книгах: автор, название книги,
## жанр, год выпуска, количество страниц, издательство.
## Требуется реализовать возможность добавления, удале-
## ния, поиска, замены данных. Используйте словарь для
## хранения информации.







# book_collection = {}

# def add_book():
#     # Добавляем новую книгу
#     title = input("Введите название книги: ")
#     author = input("Введите автора книги: ")
#     genre = input("Введите жанр книги: ")
#     year = input("Введите год выпуска книги: ")
#     pages = input("Введите количество страниц книги: ")
#     publisher = input("Введите издательство книги: ")
#     book_collection[title] = {
#         "author": author,
#         "genre": genre,
#         "year": year,
#         "pages": pages,
#         "publisher": publisher
#     }
#     print(f"Книга {title} добавлена в коллекцию!")

# def delete_book():
#     # Удаляем книгу из коллекции
#     title = input("Введите название книги для удаления: ")
#     if title in book_collection:
#         del book_collection[title]
#         print(f"Книга {title} удалена из коллекции!")
#     else:
#         print(f"Книга {title} не найдена в коллекции!")

# def search_book():
#     # Ищем книгу по названию
#     title = input("Введите название книги для поиска: ")
#     if title in book_collection:
#         print(f"Книга {title} найдена!")
#         print(f"Автор: {book_collection[title]['author']}")
#         print(f"Жанр: {book_collection[title]['genre']}")
#         print(f"Год выпуска: {book_collection[title]['year']}")
#         print(f"Количество страниц: {book_collection[title]['pages']}")
#         print(f"Издательство: {book_collection[title]['publisher']}")
#     else:
#         print(f"Книга {title} не найдена в коллекции!")

# def replace_book():
#     # Заменяем информацию о книге
#     title = input("Введите название книги для замены: ")
#     if title in book_collection:
#         author = input("Введите нового автора книги: ")
#         genre = input("Введите новый жанр книги: ")
#         year = input("Введите новый год выпуска книги: ")
#         pages = input("Введите новое количество страниц книги: ")
#         publisher = input("Введите новое издательство книги: ")
#         book_collection[title] = {
#             "author": author,
#             "genre": genre,
#             "year": year,
#             "pages": pages,
#             "publisher": publisher
#         }
#         print(f"Информация о книге {title} обновлена!")
#     else:
#         print(f"Книга {title} не найдена в коллекции!")

# def print_books():
#     # Выводим список всех книг
#     print("Список книг:")
#     for title, book in book_collection.items():
#         print(f"{title}:")
#         print(f"Автор: {book['author']}")
#         print(f"Жанр: {book['genre']}")
#         print(f"Год выпуска: {book['year']}")
#         print(f"Количество страниц: {book['pages']}")
#         print(f"Издательство: {book['publisher']}")
#         print()

# while True:
#     print("Меню:")
#     print("1. Добавить книгу")
#     print("2. Удалить книгу")
#     print("3. Найти книгу")
#     print("4. Заменить информацию о книге")
#     print("5. Вывести список книг")
#     print("6. Выход")
#     choice = int(input("Выберите пункт меню: "))

#     if choice == 1:
#         add_book()
#     elif choice == 2:
#         delete_book()
#     elif choice == 3:
#         search_book()
#     elif choice == 4:
#         replace_book()
#     elif choice == 5:
#         print_books()
#     elif choice == 6:
#         break
#     else:
#         print("Неверный выбор!")

 #Модуль 5 Файлы.Файлы.(Часть 1)






## Задание 1
## Дано два текстовых файла. Выяснить, совпадают ли
## их строки. Если нет, то вывести несовпадающую строку
## из каждого файла.




# import os

# def compare_files(file1_name, file2_name):
#     """
#     Сравнивает строки двух текстовых файлов.

#     Args:
#         file1_name (str): Имя первого файла.
#         file2_name (str): Имя второго файла.

#     Returns:
#         None
#     """
#     try:
#         with open(file1_name, 'r', encoding='utf-8') as file1, open(file2_name, 'r', encoding='utf-8') as file2:
#             file1_lines = file1.readlines()
#             file2_lines = file2.readlines()

#             # Сравниваем количество строк в файлах
#             if len(file1_lines) != len(file2_lines):
#                 print("Файлы имеют разное количество строк.")
#                 print(f"Файл {file1_name} имеет {len(file1_lines)} строк.")
#                 print(f"Файл {file2_name} имеет {len(file2_lines)} строк.")
#                 return

#             # Сравниваем строки
#             not_match = False
#             for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
#                 if line1.strip() != line2.strip():
#                     not_match = True
#                     print(f"Несовпадающие строки в строке {i}:")
#                     print(f"Файл {file1_name}: {line1.strip()}")
#                     print(f"Файл {file2_name}: {line2.strip()}")
#                     print()

#             if not not_match:
#                 print("Все строки совпадают.")

#     except FileNotFoundError:
#         print("Один из файлов не найден. Пожалуйста, проверьте путь к файлам.")

# def main():
#     while True:
#         print("Меню:")
#         print("1. Сравнить файлы")
#         print("2. Выход")
#         choice = input("Выберите действие: ")

#         if choice == "1":
#             file1_name = input("Введите полный путь к первому файлу: ")
#             file2_name = input("Введите полный путь к второму файлу: ")

#             # Проверяем, существуют ли файлы
#             if not os.path.exists(file1_name):
#                 print(f"Файл {file1_name} не найден.")
#                 continue
#             if not os.path.exists(file2_name):
#                 print(f"Файл {file2_name} не найден.")
#                 continue

#             compare_files(file1_name, file2_name)
#         elif choice == "2":
#             print("Выход из программы.")
#             break
#         else:
#             print("Неправильный выбор. Пожалуйста, выберите действие из меню.")

# if __name__ == "__main__":
#     main()







##     Дан текстовый файл. Необходимо создать новый файл
## и записать в него следующую статистику по исходному
## файлу:
## ■ Количество символов;
## ■ Количество строк;
## ■ Количество гласных букв;
## ■ Количество согласных букв;
## ■ Количество цифр.





# def count_chars(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         text = file.read()
#         char_count = len(text)
#         line_count = len(text.splitlines())
#         vowel_count = sum(1 for char in text.lower() if char in 'aeiouy')
#         consonant_count = sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiouy')
#         digit_count = sum(1 for char in text if char.isdigit())

#     with open('stats.txt', 'w', encoding='utf-8') as stats_file:
#         stats_file.write(f'Количество символов: {char_count}\n')
#         stats_file.write(f'Количество строк: {line_count}\n')
#         stats_file.write(f'Количество гласных букв: {vowel_count}\n')
#         stats_file.write(f'Количество согласных букв: {consonant_count}\n')
#         stats_file.write(f'Количество цифр: {digit_count}\n')

# def main():
#     file_name = input("Введите имя файла для анализа: ")
#     count_chars(file_name)
#     print("Статистика записана в файл stats.txt.")

# if __name__ == "__main__":
#     main()






## Задание 3
## Дан текстовый файл. Удалить из него последнюю
## строку. Результат записать в другой файл.






# def remove_last_line(input_file_name, output_file_name):
#     with open(input_file_name, 'r', encoding='utf-8') as input_file:
#         lines = input_file.readlines()
#         lines = lines[:-1]  # удалить последнюю строку

#     with open(output_file_name, 'w', encoding='utf-8') as output_file:
#         output_file.writelines(lines)

# def main():
#     input_file_name = input("Введите имя файла для редактирования: ")
#     output_file_name = input("Введите имя файла для результата: ")
#     remove_last_line(input_file_name, output_file_name)
#     print("Результат записан в файл", output_file_name)

# if __name__ == "__main__":
#     main()







## Задание 4
## Дан текстовый файл. Найти длину самой длинной
## строки.






# def find_longest_line_length(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#         longest_line_length = max(len(line.strip()) for line in lines)

#     print(f"Длина самой длинной строки: {longest_line_length}")

# def main():
#     file_name = input("Введите имя файла для анализа: ")
#     find_longest_line_length(file_name)

# if __name__ == "__main__":
#     main()







# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.






# def count_word_occurrences(file_name, word):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         text = file.read().lower()
#         word = word.lower()
#         occurrences = text.count(word)

#     print(f"Слово '{word}' встречается {occurrences} раз(а)")

# def main():
#     file_name = input("Введите имя файла для анализа: ")
#     word = input("Введите слово для поиска: ")
#     count_word_occurrences(file_name, word)

# if __name__ == "__main__":
#     main()






## Задание 6
## Дан текстовый файл. Найти и заменить в нем задан-
## ное слово. Что искать и на что заменять определяется
## пользователем.







## №1



# def replace_word(file_name, old_word, new_word):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         text = file.read().lower()
#         old_word = old_word.lower()
#         new_word = new_word.lower()
#         text = text.replace(old_word, new_word)
#         with open(file_name, 'w', encoding='utf-8') as file:
#             file.write(text)
#     print(f"Слово '{old_word}' заменено на '{new_word}'")
# def main():
#     file_name = input("Введите имя файла для редактирования: ")
#     old_word = input("Введите слово для замены: ")
#     new_word = input("Введите новое слово: ")
#     replace_word(file_name, old_word, new_word)
# if __name__ == "__main__":
#     main()







## №2



# def replace_word_in_file(file_name, old_word, new_word):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         text = file.read()

#     new_text = text.replace(old_word, new_word)

#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(new_text)

#     print(f"Слово '{old_word}' заменено на '{new_word}' в файле {file_name}")

# def main():
#     file_name = input("Введите имя файла для редактирования: ")
#     old_word = input("Введите слово для замены: ")
#     new_word = input("Введите новое слово: ")
#     replace_word_in_file(file_name, old_word, new_word)

# if __name__ == "__main__":
#     main()







## Модуль 5 Файлы.
## Тема: Файлы. Часть 2







## Задание 1
## Напишите информационную систему «Сотрудники».
## Программа должна обеспечивать ввод данных, редакти-
## рование данных сотрудника, удаление сотрудника, поиск
## сотрудника по фамилии, вывод информации обо всех
## сотрудниках, указанного возраста, или фамилия которых
## начинается на указанную букву. Организуйте возможность
## сохранения найденной информации в файл. Также весь
## список сотрудников сохраняется в файл (при выходе из
## программы — автоматически, в процессе исполнения
## программы — по команде пользователя). При старте
## программы происходит загрузка списка сотрудников из
## указанного пользователем файла.






# class Employee:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.surname} {self.name}, {self.age} лет"

# class EmployeeSystem:
#     def __init__(self, file_name):
#         self.employees = self.load_employees_from_file(file_name)

#     def load_employees_from_file(self, file_name):
#         try:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 employees = []
#                 for line in file:
#                     surname, name, age = line.strip().split(',')
#                     employees.append(Employee(surname, name, int(age)))
#                 return employees
#         except FileNotFoundError:
#             return []

#     def save_employees_to_file(self, file_name):
#         with open(file_name, 'w', encoding='utf-8') as file:
#             for employee in self.employees:
#                 file.write(f"{employee.surname},{employee.name},{employee.age}\n")

#     def add_employee(self, surname, name, age):
#         self.employees.append(Employee(surname, name, age))

#     def edit_employee(self, surname, name, age):
#         for employee in self.employees:
#             if employee.surname == surname:
#                 employee.name = name
#                 employee.age = age
#                 return
#         print("Сотрудник не найден")

#     def delete_employee(self, surname):
#         for employee in self.employees:
#             if employee.surname == surname:
#                 self.employees.remove(employee)
#                 return
#         print("Сотрудник не найден")

#     def find_employees_by_surname(self, surname):
#         return [employee for employee in self.employees if employee.surname.startswith(surname)]

#     def find_employees_by_age(self, age):
#         return [employee for employee in self.employees if employee.age == age]

#     def print_employees(self, employees):
#         for employee in employees:
#             print(employee)

# def main():
#     file_name = input("Введите имя файла для загрузки списка сотрудников: ")
#     system = EmployeeSystem(file_name)

#     while True:
#         print("Меню:")
#         print("1. Добавить сотрудника")
#         print("2. Редактировать сотрудника")
#         print("3. Удалить сотрудника")
#         print("4. Найти сотрудника по фамилии")
#         print("5. Найти сотрудника по возрасту")
#         print("6. Вывести информацию обо всех сотрудниках")
#         print("7. Сохранить список сотрудников в файл")
#         print("8. Выход")

#         choice = input("Введите номер пункта меню: ")

#         if choice == "1":
#             surname = input("Введите фамилию: ")
#             name = input("Введите имя: ")
#             age = int(input("Введите возраст: "))
#             system.add_employee(surname, name, age)
#         elif choice == "2":
#             surname = input("Введите фамилию: ")
#             name = input("Введите имя: ")
#             age = int(input("Введите возраст: "))
#             system.edit_employee(surname, name, age)
#         elif choice == "3":
#             surname = input("Введите фамилию: ")
#             system.delete_employee(surname)
#         elif choice == "4":
#             surname = input("Введите фамилию: ")
#             employees = system.find_employees_by_surname(surname)
#             system.print_employees(employees)
#         elif choice == "5":
#             age = int(input("Введите возраст: "))
#             employees = system.find_employees_by_age(age)
#             system.print_employees(employees)
#         elif choice == "6":
#             system.print_employees(system.employees)
#         elif choice == "7":
#             file_name = input("Введите имя файла для сохранения списка сотрудников: ")
#             system.save_employees_to_file(file_name)
#         elif choice == "8":
#             system.save_employees_to_file(file_name)
#             break
#         else:
#             print("Неверный выбор")

# if __name__ == "__main__":
#     main()






##     Шаг 1: Определение класса Employee

## Код определяет класс Employee с тремя атрибутами: фамилией, именем и возрастом. Метод __init__ инициализирует эти атрибуты при создании экземпляра класса. Метод __str__ возвращает строковое представление сотрудника в формате "Фамилия, имя, возраст, годы".

## Шаг 2: Определение класса EmployeeSystem

## В коде определяется класс EmployeeSystem, который управляет списком сотрудников. Метод __init__ инициализирует список сотрудников, загружая их из файла, указанного параметром file_name. Метод load_employees_from_file считывает файл и создает экземпляр класса Employee для каждой строки в файле.

## Шаг 3: Определение методов для класса EmployeeSystem

## В коде определено несколько методов для класса EmployeeSystem:

## add_employee: добавляет нового сотрудника в список
## edit_employee: редактирует существующего сотрудника в списке
## delete_employee: удаляет сотрудника из списка
## find_employees_by_surname: находит сотрудников по фамилии
## find_employees_by_age: находит сотрудников по возрасту
## print_employees: печатает список сотрудников
## save_employees_to_file: сохраняет список сотрудников в файл
## Шаг 4: Определение основной функции

## Код определяет основную функцию, которая запускает программу. Функция:

## Просит пользователя ввести имя файла для загрузки списка сотрудников
## Создает экземпляр класса EmployeeSystem с указанным именем файла
## Переходит в цикл, в котором пользователю повторно предлагается выбрать действие из меню
## Шаг 5: Цикл меню

## В цикле меню пользователю повторно предлагается выбрать действие из следующего меню:

## Добавить сотрудника
## Отредактировать сотрудника
## Удалить сотрудника
## Поиск сотрудников по фамилии
## Поиск сотрудников по возрасту
## Вывести всех сотрудников
## Сохранить сотрудников в файл
## Выход
## В зависимости от выбора пользователя программа выполняет соответствующее действие, используя методы, определенные в классе EmployeeSystem.

## Шаг 6: Сохранение сотрудников в файл

## Когда пользователь выбирает сохранение сотрудников в файл, программа запрашивает имя сотрудника.выберите файл для сохранения, а затем вызовите метод save_employees_to_file, чтобы сохранить список сотрудников в указанном файле.

## Шаг 7: Выход из программы

## Когда пользователь решает выйти из программы, программа сохраняет список сотрудников в файл, указанный в переменной file_name, а затем завершает цикл.

## Это общий обзор того, что делает код на высоком уровне! Дайте мне знать, если у вас возникнут какие-либо конкретные вопросы по поводу любого из этих шагов.







# Модуль 10. Обьектно-ориентированное программирование
#        Тема: Множественное наследование.
# Полиморфизм. Реализация магических методов. Часть 6








## Задание 1
## Создать базовый класс Фигура с методом для подсчета
## площади. Создать производные классы: прямоугольник,
## круг, прямоугольный треугольник, трапеция со своими
## методами для подсчета площади.





# import math

# ## Базовый класс Фигура
# class Figure:
#     def __init__(self):
#         pass

#     def area(self):
#         pass

# ## Производный класс Прямоугольник
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# ## Производный класс Круг
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# ##Производный класс Прямоугольный треугольник
# class RightTriangle(Figure):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# ## Производный класс Трапеция
# class Trapezoid(Figure):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height

#     def area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height

# ## Пример использования
# rectangle = Rectangle(4, 5)
# print(f"Площадь прямоугольника: {rectangle.area()}")

# circle = Circle(3)
# print(f"Площадь круга: {circle.area()}")

# right_triangle = RightTriangle(3, 4)
# print(f"Площадь прямоугольного треугольника: {right_triangle.area()}")

# trapezoid = Trapezoid(3, 5, 4)
# print(f"Площадь трапеции: {trapezoid.area()}")







# ## Задание 2
# ## Для классов из задания 1 нужно переопределить маги-
# ## ческие методы int(возвращает площадь) и str (возвращает
# ## информацию о фигуре).
# import math






# # Базовый класс Фигура
# class Figure:
#     def __init__(self):
#         pass

#     def area(self):
#         pass

#     def __int__(self):
#         return int(self.area())

#     def __str__(self):
#         pass

# ## Производный класс Прямоугольник
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def __str__(self):
#         return f"Прямоугольник: ширина = {self.width}, высота = {self.height}, площадь = {self.area()}"

# ## Производный класс Круг
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def __str__(self):
#         return f"Круг: радиус = {self.radius}, площадь = {self.area()}"

# ## Производный класс Прямоугольный треугольник
# class RightTriangle(Figure):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

#     def __str__(self):
#         return f"Прямоугольный треугольник: основание = {self.base}, высота = {self.height}, площадь = {self.area()}"

# ## Производный класс Трапеция
# class Trapezoid(Figure):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height

#     def area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height

#     def __str__(self):
#         return f"Трапеция: основания = {self.base1} и {self.base2}, высота = {self.height}, площадь = {self.area()}"

# ## Пример использования
# rectangle = Rectangle(4, 5)
# print(int(rectangle))  ## Выводит площадь прямоугольника
# print(rectangle)  # Выводит информацию о прямоугольнике

# circle = Circle(3)
# print(int(circle))  ## Выводит площадь круга
# print(circle)  ## Выводит информацию о круге

# right_triangle = RightTriangle(3, 4)
# print(int(right_triangle))  ## Выводит площадь прямоугольного треугольника
# print(right_triangle)  ## Выводит информацию о прямоугольном треугольнике

# trapezoid = Trapezoid(3, 5, 4)
# print(int(trapezoid))  ## Выводит площадь трапеции
# print(trapezoid)  ## Выводит информацию о трапеции







# ## Задание 3
# ## Создайте базовый класс Shape для рисования плоских
# ## фигур.
# ## Определите методы:
# ## ■ Show() — вывод на экран информации о фигуре;
# ## ■ Save() — сохранение фигуры в файл;
# ## ■ Load() — считывание фигуры из файла.
# ## Определите производные классы:
# ## ■ Square — квадрат, который характеризуется коорди-
# ## натами левого верхнего угла и длиной стороны;
# ## ■ Rectangle — прямоугольник с заданными координа-
# ## тами верхнего левого угла и размерами;
# ## ■ Circle — окружность с заданными координатами цен-
# ## тра и радиусом;
# ## ■ Ellipse — эллипс с заданными координатами верхнего
# ## угла описанного вокруг него прямоугольника со сто-
# ## ронами, параллельными осям координат, и размерами
# ## этого прямоугольника.
# ## Создайте список фигур, сохраните фигуры в файл,
# ## загрузите в другой список и отобразите информацию о
# ## каждой из фигур.

# import json

# ## Базовый класс Shape
# class Shape:
#     def __init__(self):
#         pass

#     def show(self):
#         pass

#     def save(self, filename):
#         with open(filename, 'a') as file:
#             json.dump(self.__dict__, file)
#             file.write('\n')

#     @classmethod
#     def load(cls, filename):
#         shapes = []
#         with open(filename, 'r') as file:
#             for line in file:
#                 shape_dict = json.loads(line)
#                 shape = cls()
#                 shape.__dict__.update(shape_dict)
#                 shapes.append(shape)
#         return shapes

# ## Производный класс Square
# class Square(Shape):
#     def __init__(self, x, y, side):
#         self.x = x
#         self.y = y
#         self.side = side

#     def show(self):
#         print(f"Квадрат: ({self.x}, {self.y}), сторона = {self.side}")

# ## Производный класс Rectangle
# class Rectangle(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#     def show(self):
#         print(f"Прямоугольник: ({self.x}, {self.y}), ширина = {self.width}, высота = {self.height}")

# ## Производный класс Circle
# class Circle(Shape):
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius

#     def show(self):
#         print(f"Окружность: ({self.x}, {self.y}), радиус = {self.radius}")

# ## Производный класс Ellipse
# class Ellipse(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#     def show(self):
#         print(f"Эллипс: ({self.x}, {self.y}), ширина = {self.width}, высота = {self.height}")

# ## Создание списка фигур
# shapes = [
#     Square(1, 2, 3),
#     Rectangle(4, 5, 6, 7),
#     Circle(8, 9, 10),
#     Ellipse(11, 12, 13, 14)
# ]

# ## Сохранение фигур в файл
# for shape in shapes:
#     shape.save('shapes.txt')

# ## Загрузка фигур из файла
# loaded_shapes = []
# with open('shapes.txt', 'r') as file:
#     for line in file:
#         shape_dict = json.loads(line)
#         if 'side' in shape_dict:
#             shape = Square(0, 0, 0)
#         elif 'width' in shape_dict and 'height' in shape_dict:
#             if 'radius' not in shape_dict:
#                 shape = Rectangle(0, 0, 0, 0)
#             else:
#                 shape = Ellipse(0, 0, 0, 0)
#         else:
#             shape = Circle(0, 0, 0)
#         shape.__dict__.update(shape_dict)
#         loaded_shapes.append(shape)

# ## Отображение информации о каждой фигуре
# for shape in loaded_shapes:
#     shape.show()






## Модуль 10. Обьектно-ориентированное программирование
##            Тема:наследование.







#  Задание 1
#  Создайте класс Device, который содержит информа-
#  цию об устройстве.
#  С помощью механизма наследования, реализуйте класс
# CoffeeMachine (содержит информацию о кофемашине),
#  класс Blender (содержит информацию о блендере), класс
#  MeatGrinder (содержит информацию о мясорубке).
#  Каждый из классов должен содержать необходимые
#  для работы методы.







# #№1
# class Device:
#     def __init__(self, name, power, voltage):
#         """
#         Инициализация устройства

#         :param name: Название устройства
#         :param power: Мощность устройства
#         :param voltage: Напряжение устройства
#         """
#         self.name = name
#         self.power = power
#         self.voltage = voltage

#     def get_info(self):
#         """
#         Получение информации об устройстве

#         :return: Информация об устройстве
#         """
#         return f"Устройство: {self.name}, Мощность: {self.power} Вт, Напряжение: {self.voltage} В"

#     def turn_on(self):
#         """
#         Включение устройства
#         """
#         print(f"{self.name} включен")

#     def turn_off(self):
#         """
#         Выключение устройства
#         """
#         print(f"{self.name} выключен")

# device = Device("Philips", 300, 220)
# print(device.get_info())
# device.turn_on()
# device.turn_off()



# #№2
# class CoffeeMachine(Device):
#     def __init__(self, name, power, voltage, coffee_types):
#         """
#         Инициализация кофемашины

#         :param name: Название кофемашины
#         :param power: Мощность кофемашины
#         :param voltage: Напряжение кофемашины
#         :param coffee_types: Типы кофе, которые может приготовить кофемашина
#         """
#         super().__init__(name, power, voltage)
#         self.coffee_types = coffee_types

#     def make_coffee(self, coffee_type):
#         """
#         Приготовление кофе

#         :param coffee_type: Тип кофе
#         """
#         if coffee_type in self.coffee_types:
#             print(f"Приготовлен {coffee_type} кофе")
#         else:
#             print("Кофемашина не может приготовить такой тип кофе")

#     def get_coffee_types(self):
#         """
#         Получение списка доступных типов кофе

#         :return: Список доступных типов кофе
#         """
#         return self.coffee_types

# coffee_machine = CoffeeMachine("Philips", 1200, 220, ["Эспрессо", "Капучино", "Латте"])
# print(coffee_machine.get_info())
# coffee_machine.turn_on()
# coffee_machine.make_coffee




# #№3
# class Blender(Device):
#     def __init__(self, name, power, voltage, speed_modes):
#         """
#         Инициализация блендера

#         :param name: Название блендера
#         :param power: Мощность блендера
#         :param voltage: Напряжение блендера
#         :param speed_modes: Режимы скорости блендера
#         """
#         super().__init__(name, power, voltage)
#         self.speed_modes = speed_modes

#     def blend(self, speed_mode):
#         """
#         Взбивание

#         :param speed_mode: Режим скорости
#         """
#         if speed_mode in self.speed_modes:
#             print(f"Взбивание на скорости {speed_mode}")
#         else:
#             print("Блендер не имеет такого режима скорости")

#     def get_speed_modes(self):
#         """
#         Получение списка доступных режимов скорости

#         :return: Список доступных режимов скорости
#         """
#         return self.speed_modes

# blender = Blender("Bosch", 500, 220, ["Low", "Medium", "High"])
# print(blender.get_info())
# blender.turn_on()
# blender.blend("Medium")




# #№4
# class MeatGrinder(Device):
#     def __init__(self, name, power, voltage, grinding_modes):
#         """
#         Инициализация мясорубки

#         :param name: Название мясорубки
#         :param power: Мощность мясорубки
#         :param voltage: Напряжение мясорубки
#         :param grinding_modes: Режимы измельчения мясорубки
#         """
#         super().__init__(name, power, voltage)
#         self.grinding_modes = grinding_modes

#     def grind(self, grinding_mode):
#         """
#         Измельчение

#         :param grinding_mode: Режим измельчения
#         """
#         if grinding_mode in self.grinding_modes:
#             print(f"Измельчение на режиме {grinding_mode}")
#         else:
#             print("Мясорубка не имеет такого режима измельчения")

#     def get_grinding_modes(self):
#         """
#         Получение списка доступных режимов измельчения

#         :return: Список доступных режимов измельчения
#         """
#         return self.grinding_modes

# meat_grinder = MeatGrinder("Moulinex", 800, 220, ["Fine", "Medium", "Coarse"])
# print(meat_grinder.get_info())
# meat_grinder.turn_on()
# print(meat_grinder.get_grinding_modes())
# meat_grinder.grind("Medium")






# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.






# #№1
# # ship.py
# class Ship:
#     def __init__(self, name, length, width, draft):
#         """
#         Инициализация корабля.

#         :param name: Название корабля
#         :param length: Длина корабля
#         :param width: Ширина корабля
#         :param draft: Осадка корабля
#         """
#         self.name = name
#         self.length = length
#         self.width = width
#         self.draft = draft

#     def get_info(self):
#         """
#         Возвращает информацию о корабле.

#         :return: Строка с информацией о корабле
#         """
#         return f"Корабль '{self.name}': длина - {self.length} м, ширина - {self.width} м, осадка - {self.draft} м"

#     def __str__(self):
#         return self.get_info()
    
# ship = Ship("Корабль", 100, 10, 5)
# print(ship)  # Выводит: Корабль 'Корабль': длина - 100 м, ширина - 10 м, осадка - 5 м







# #№2
# # frigate.py

# class Frigate(Ship):
#     def __init__(self, name, length, width, draft, speed):
#         """
#         Инициализация фрегата.

#         :param name: Название фрегата
#         :param length: Длина фрегата
#         :param width: Ширина фрегата
#         :param draft: Осадка фрегата
#         :param speed: Скорость фрегата
#         """
#         super().__init__(name, length, width, draft)
#         self.speed = speed

#     def get_info(self):
#         """
#         Возвращает информацию о фрегате.

#         :return: Строка с информацией о фрегате
#         """
#         return f"{super().get_info()}, скорость - {self.speed} узлов"

#     def __str__(self):
#         return self.get_info()
    
# frigate = Frigate("Фрегат", 100, 10, 5, 20)
# print(frigate)  # Выводит: Корабль 'Фрегат': длина - 100 м, ширина - 10 м, осадка - 5 м, скорость - 20 узлов
# # destroyer.py







# #№3
# # Destroyer.py

# class Destroyer(Ship):
#     def __init__(self, name, length, width, draft, torpedo_tubes):
#         """
#         Инициализация эсминца.

#         :param name: Название эсминца
#         :param length: Длина эсминца
#         :param width: Ширина эсминца
#         :param draft: Осадка эсминца
#         :param torpedo_tubes: Количество торпедных аппаратов
#         """
#         super().__init__(name, length, width, draft)
#         self.torpedo_tubes = torpedo_tubes

#     def get_info(self):
#         """
#         Возвращает информацию об эсминце.

#         :return: Строка с информацией об эсминце
#         """
#         return f"{super().get_info()}, торпедные аппараты - {self.torpedo_tubes} шт."

#     def __str__(self):
#         return self.get_info()
    
# destroyer = Destroyer("Эсминец", 100, 10, 5, 4)
# print(destroyer)  # Выводит: Корабль 'Эсминец': длина - 100 м, ширина - 10 м, осадка - 5 м, торпедные аппараты - 4 шт.






# #№4
# # cruiser.py

# class Cruiser(Ship):
#     def __init__(self, name, length, width, draft, main_caliber):
#         """
#         Инициализация крейсера.

#         :param name: Название крейсера
#         :param length: Длина крейсера
#         :param width: Ширина крейсера
#         :param draft: Осадка крейсера
#         :param main_caliber: Калибр главной артиллерии
#         """
#         super().__init__(name, length, width, draft)
#         self.main_caliber = main_caliber

#     def get_info(self):
#         """
#         Возвращает информацию о крейсере.

#         :return: Строка с информацией о крейсере
#         """
#         return f"{super().get_info()}, главный калибр - {self.main_caliber}"

# cruiser = Cruiser("Крейсер", 150, 15, 6, "203 мм")
# print(cruiser.get_info())  # Выводит: Корабль 'Крейсер': длина - 150 м, ширина - 15 м, осадка - 6 м, главный калибр - 203 мм





# #№5
# # main.py

# frigate = Frigate("Фрегат", 100, 10, 5, 20)
# destroyer = Destroyer("Эсминец", 120, 12, 6, 4)
# cruiser = Cruiser("Крейсер", 150, 15, 7, 152)

# print(frigate.get_info())
# print(destroyer.get_info())
# print(cruiser.get_info())





## Задание 3
## Запрограммируйте класс Money (объект класса опе-
## рирует одной валютой) для работы с деньгами.
## В классе должны быть предусмотрены поле для хра-
## нения целой части денег (доллары, евро, гривны и т.д.) и
## поле для хранения копеек (центы, евроценты, копейки
## и т.д.).
## Реализовать методы для вывода суммы на экран, за-
## дания значений для частей.





##№1

# class Money:
#     def __init__(self, currency, dollars=0, cents=0):
#         """
#         Инициализация объекта Money.

#         :param currency: Валюта (строка)
#         :param dollars: Целая часть денег (доллары, евро, гривны и т.д.)
#         :param cents: Дробная часть денег (центы, евроценты, копейки и т.д.)
#         """
#         self.currency = currency
#         self.dollars = dollars
#         self.cents = cents

#     def set_dollars(self, dollars):
#         """
#         Установка целой части денег.

#         :param dollars: Целая часть денег
#         """
#         self.dollars = dollars

#     def set_cents(self, cents):
#         """
#         Установка дробной части денег.

#         :param cents: Дробная часть денег
#         """
#         self.cents = cents

#     def get_amount(self):
#         """
#         Возвращает сумму денег в виде строки.

#         :return: Сумма денег в виде строки
#         """
#         return f"{self.dollars}.{self.cents:02} {self.currency}"

#     def __str__(self):
#         return self.get_amount()

# # Пример использования класса Money
# money = Money("USD", 10, 50)
# print(money)  # Выводит: 10.50 USD

# money.set_dollars(20)
# money.set_cents(25)
# print(money)  # Выводит: 20.25 USD







##№2

# class Money:
#     def __init__(self, currency, dollars=0, cents=0):
#         """
#         Инициализация объекта Money.

#         :param currency: Валюта (строка)
#         :param dollars: Целая часть денег (доллары, евро, гривны и т.д.)
#         :param cents: Дробная часть денег (центы, евроценты, копейки и т.д.)
#         """
#         self.currency = currency
#         self.dollars = dollars
#         self.cents = cents

#     def set_dollars(self, dollars):
#         """
#         Установка целой части денег.

#         :param dollars: Целая часть денег
#         """
#         self.dollars = dollars

#     def set_cents(self, cents):
#         """
#         Установка дробной части денег.

#         :param cents: Дробная часть денег
#         """
#         self.cents = cents

#     def get_amount(self):
#         """
#         Возвращает сумму денег в виде строки.

#         :return: Сумма денег в виде строки
#         """
#         return f"{self.dollars}.{self.cents:02} {self.currency}"

#     def __str__(self):
#         return self.get_amount()

# def main():
#     print("Добро пожаловать в меню Money!")
#     currency = input("Введите валюту (например, USD, EUR, UAH): ")
#     money = Money(currency)

#     while True:
#         print("\nМеню:")
#         print("1. Установить сумму денег")
#         print("2. Вывести сумму денег")
#         print("3. Выход")

#         choice = input("Введите номер пункта меню: ")

#         if choice == "1":
#             dollars = int(input("Введите целую часть денег: "))
#             cents = int(input("Введите дробную часть денег: "))
#             money.set_dollars(dollars)
#             money.set_cents(cents)
#         elif choice == "2":
#             print(money)
#         elif choice == "3":
#             print("До свидания!")
#             break
#         else:
#             print("Неверный номер пункта меню. Пожалуйста, попробуйте еще раз.")

# if __name__ == "__main__":
#     main()






## №3

# class Money:
#     def __init__(self, currency, dollars=0, cents=0):
#         """
#         Инициализация объекта Money.

#         :param currency: Валюта (строка)
#         :param dollars: Целая часть денег (доллары, евро, гривны и т.д.)
#         :param cents: Дробная часть денег (центы, евроценты, копейки и т.д.)
#         """
#         self.currency = currency
#         self.dollars = dollars
#         self.cents = cents

#     def set_dollars(self, dollars):
#         """
#         Установка целой части денег.

#         :param dollars: Целая часть денег
#         """
#         self.dollars = dollars

#     def set_cents(self, cents):
#         """
#         Установка дробной части денег.

#         :param cents: Дробная часть денег
#         """
#         self.cents = cents

#     def get_amount(self):
#         """
#         Возвращает сумму денег в виде строки.

#         :return: Сумма денег в виде строки
#         """
#         return f"{self.dollars}.{self.cents:02} {self.currency}"

#     def __str__(self):
#         return self.get_amount()

# class Bank:
#     def __init__(self):
#         self.exchange_rates = {
#             "USD": 1.0,
#             "EUR": 0.88,
#             "UAH": 26.5
#         }
#         self.interest_rates = {
#             "USD": 0.05,
#             "EUR": 0.03,
#             "UAH": 0.10
#         }

#     def convert(self, money, new_currency):
#         """
#         Переводит деньги из одной валюты в другую.

#         :param money: Объект Money
#         :param new_currency: Новая валюта
#         :return: Объект Money с новой валютой
#         """
#         new_amount = money.dollars * self.exchange_rates[money.currency] / self.exchange_rates[new_currency]
#         return Money(new_currency, int(new_amount), int((new_amount - int(new_amount)) * 100))

#     def deposit(self, money, years):
#         """
#         Положить деньги под процент.

#         :param money: Объект Money
#         :param years: Количество лет
#         :return: Объект Money с новой суммой
#         """
#         interest_rate = self.interest_rates[money.currency]
#         new_amount = money.dollars * (1 + interest_rate) ** years
#         return Money(money.currency, int(new_amount), int((new_amount - int(new_amount)) * 100))

# def main():
#     print("Добро пожаловать в меню Money!")
#     bank = Bank()
#     currency = input("Введите валюту (например, USD, EUR, UAH): ")
#     money = Money(currency)

#     while True:
#         print("\nМеню:")
#         print("1. Установить сумму денег")
#         print("2. Вывести сумму денег")
#         print("3. Перевести деньги в другую валюту")
#         print("4. Положить деньги под процент")
#         print("5. Выход")

#         choice = input("Введите номер пункта меню: ")

#         if choice == "1":
#             dollars = int(input("Введите целую часть денег: "))
#             cents = int(input("Введите дробную часть денег: "))
#             money.set_dollars(dollars)
#             money.set_cents(cents)
#         elif choice == "2":
#             print(money)
#         elif choice == "3":
#             new_currency = input("Введите новую валюту (например, USD, EUR, UAH): ")
#             new_money = bank.convert(money, new_currency)
#             print(new_money)
#         elif choice == "4":
#             years = int(input("Введите количество лет: "))
#             new_money = bank.deposit(money, years)
#             print(new_money)
#         elif choice == "5":
#             print("До свидания!")
#             break
#         else:
#             print("Неверный номер пункта меню. Пожалуйста, попробуйте еще раз.")

# if __name__ == "__main__":
#     main()





## Модуль 10.Обьектно-ориентированное программирование 
## Тема:Перезагрузка операторов.Часть 5







# [Обозночение]

# Комплексное число - это математическое понятие, которое расширяет понятие обычного числа, добавляя к нему.imaginary часть. Комплексное число обычно записывается в виде:

# a + bi

# где:

# a - real part (действительная часть)
# b - imaginary part (мнимая часть)
# i - imaginary unit (мнимая единица), которая равна квадратному корню из -1 (i = √(-1))
                                                                            
# Комплексные числа используются в различных областях математики и физики, таких как алгебра, геометрия, анализ, электротехника, физика и другие.

# В частности, комплексные числа полезны для решения уравнений, которые не имеют решений в области вещественных чисел. Например, уравнение x^2 + 1 = 0 не имеет решений в области вещественных чисел, но имеет два комплексных решения: x = i и x = -i.

# Комплексные числа также используются для описания периодических процессов, таких как колебания и волны, а также для моделирования электрических цепей и других физических систем.                                                                            







## Задание 1
## Создайте класс Circle (окружность). Для данного
## класса реализуйте ряд перегруженных операторов:
## ■ Проверка на равенство радиусов двух окружностей
## (операция = =);
## ■ Сравнения длин двух окружностей (операции >, <,
## <=,>=);
## ■ Пропорциональное изменение размеров окружности,
## путем изменения ее радиуса (операции + - += -=).





# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __le__(self, other):
#         return self.radius <= other.radius

#     def __gt__(self, other):
#         return self.radius > other.radius

#     def __ge__(self, other):
#         return self.radius >= other.radius

#     def __add__(self, other):
#         return Circle(self.radius + other.radius)

#     def __sub__(self, other):
#         return Circle(self.radius - other.radius)

#     def __iadd__(self, other):
#         self.radius += other.radius
#         return self




## Это определение класса Python для класса Circle. Вот описание того, что происходит:

## Инициализация

## Метод __init__ является конструктором класса. Он принимает единственный аргумент radius и устанавливает его в качестве переменной экземпляра self.radius.

## Методы сравнения

## В классе определено несколько методов сравнения:

## __eq__: проверяет, равны ли две окружности (т. е. имеют ли они одинаковый радиус).
## __lt__: проверяет, меньше ли одна окружность другой (т. е. имеет ли она меньший радиус)
## __le__: проверяет, меньше или равна ли одна окружность другой
## __gt__: проверяет, больше ли одна окружность другой
## __ge__: проверяет, больше или равна ли одна окружность другой.
## Эти методы позволяют сравнивать объекты Circle с помощью стандартных операторов сравнения (==, <, <=, >, >=).

## Арифметические методы

## В классе определены два арифметических метода:

## __add__: складывает две окружности путем сложения их радиусов и возвращает новый объект Circle с полученным радиусом.
## __sub__: вычитает одну окружность из другой путем вычитания их радиусов и возвращает новый объект Circle с полученным радиусом
## __iadd__: увеличивает радиус текущей окружности путем добавления радиуса другой окружности (сложение на месте).
## Эти методы позволяют выполнять арифметические операции над объектами Circle с помощью стандартных операторов (+, -, +=).

## Примечание

## Отступы в исходном коде сделаны неправильно. Методы должны быть определены на уровне класса, а не внутри метода __init__. Вот исправленный код:






## Задание 2
## Создайте класс Complex (комплексное число). Более
## подробно ознакомиться с комплексными числами можно
## по ссылке.
## Создайте перегруженные операторы для реализации
## арифметических операций для по работе с комплексными
## числами (операции +, -, *, /).






# class Complex:
#     def __init__(self, real=0, imag=0):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

#     def __truediv__(self, other):
#         denominator = other.real ** 2 + other.imag ** 2
#         return Complex((self.real * other.real + self.imag * other.imag) / denominator,
#                         (self.imag * other.real - self.real * other.imag) / denominator)

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"

# c1 = Complex(3, 4)  # represents 3 + 4i
# c2 = Complex(1, 2)  # represents 1 + 2i

# c3 = c1 + c2  # c3 = Complex(4, 6)  # represents 4 + 6i
# c4 = c1 - c2  # c4 = Complex(2, 2)  # represents 2 + 2i
# c5 = c1 * c2  # c5 = Complex(-5, 10)  # represents -5 + 10i
# c6 = c1 / c2  # c6 = Complex(2.2, -0.4)  # represents 2.2 - 0.4i

# print(c1)  # Output: 3 + 4i
# print(c2)  # Output: 1 + 2i
# print(c3)  # Output: 4 + 6i
# print(c4)  # Output: 2 + 2i
# print(c5)  # Output: -5 + 10i
# print(c6)  # Output: 2.2 - 0.4i








## c1 = 3 + 4i, где a = 3, b = 4
## c2 = 1 + 2i, где a = 1, b = 2
## c3 = 4 + 6i, где a = 4, b = 6
## c4 = 2 + 2i, где a = 2, b = 2
## c5 = -5 + 10i, где a = -5, b = 10
## c6 = 2.2 - 0.4i, где a = 2.2, b = -0.4




## Определение класса

## В коде определен класс Complex, который представляет комплексные числа. Комплексное число - это число, которое можно выразить в виде a + bi, где a - действительная часть, а b - мнимая часть.

## Метод __init__

## Метод __init__ - это специальный метод в Python, который вызывается при создании объекта. В данном случае он инициализирует объект Complex с двумя атрибутами: real и imag. Эти атрибуты представляют действительную и мнимую части комплексного числа, соответственно. Метод __init__ принимает два необязательных аргумента, real и imag, которые по умолчанию равны 0, если не указаны.

## Метод __add__

## Метод __add__ - это специальный метод в Python, который вызывается при использовании оператора +. В данном случае он складывает два комплексных числа. В качестве аргумента метод принимает другой объект Complex, other. Он возвращает новый объект Complex, который представляет собой сумму двух комплексных чисел.

## Вот что происходит при вызове метода c1 + c2:

## c1 и c2 - оба комплексные объекты.
## Метод __add__ вызывается на c1 с c2 в качестве аргумента.
## Метод возвращает новый объект Complex с вещественной частью c1.real + c2.real и образной частью c1.imag + c2.imag.
## Метод __sub__

## Метод __sub__ похож на метод __add__, но вместо сложения он вычитает два комплексных числа.

## Метод __mul__

## Метод __mul__ перемножает два комплексных числа. Он возвращает новый объект Complex с вещественной частью c1.real * c2.real - c1.imag * c2.imag и вещественной частью c1.real * c2.imag + c1.imag * c2.real.

## Метод __truediv__

## Метод __truediv__ делит два комплексных числа. Он возвращает новый объект Complex с вещественной частью (c1.real * c2.real + c1.imag * c2.imag) / знаменатель и вещественной частью (c1.imag * c2.real - c1.real * c2.imag) / знаменатель, где знаменатель равен c2.real ** 2 + c2.imag ** 2.

## Метод __str__

## Метод __str__ возвращает строковое представление комплексного числа. В данном случае он возвращает строку в виде a + bi, где a - действительная часть, а b - мнимая часть.

## Создание комплексных объектов

## Код создает шесть комплексных объектов: c1, c2, c3, c4, c5 и c6.

## c1 представляет комплексное число 3 + 4i.
## c2 представляет комплексное число 1 + 2i.
## c3 представляет собой сумму c1 и c2, которая равна 4 + 6i.
## c4 представляет собой разность c1 и c2, которая равна 2 + 2i.
## c5 представляет собой произведение c1 и c2, которое равно -5 + 10i.
## c6 представляет собой коэффициент c1 и c2, который равен 2,2 - 0,4i.
## Печать сложных объектов

## Код печатает каждый сложный объект с помощью функции print. Для преобразования каждого сложного объекта в строку неявно вызывается метод __str__.







## Задание 3
## Вам необходимо создать класс Airplane (самолет).
## С помощью перегрузги операторов реализовать:
## ■ Проверка на равенство типов самолетов (операция
## = =);
## ■ Увеличение и уменьшение пассажиров в салоне са-
## молета (операции + - += -=);
## ■ Сравнение двух самолетов по максимально возмож-
## ному количеству пассажиров на борту (операции >
## < <= >=).


# class Airplane:
#     def __init__(self, max_passengers):
#         self.max_passengers = max_passengers
#         self.passengers = 0

#     def __eq__(self, other):
#         return self.max_passengers == other.max_passengers

#     def __add__(self, other):
#         if isinstance(other, Airplane):
#             if self.max_passengers >= other.passengers:
#                 self.passengers += other.passengers
#                 return self
#             else:
#                 return "Error: самолет не может вместить всех пассажиров"
#         elif isinstance(other, int):
#             if self.passengers + other <= self.max_passengers:
#                 self.passengers += other
#                 return self
#             else:
#                 return "Error: превышен лимит пассажиров"
#         else:
#             return "Error: неверный тип операнда"

#     def __sub__(self, other):
#         if isinstance(other, Airplane):
#             if self.passengers >= other.passengers:
#                 self.passengers -= other.passengers
#                 return self
#             else:
#                 return "Error: недостаточно пассажиров для удаления"
#         elif isinstance(other, int):
#             if self.passengers >= other:
#                 self.passengers -= other
#                 return self
#             else:
#                 return "Error: недостаточно пассажиров для удаления"
#         else:
#             return "Error: неверный тип операнда"

#     def __iadd__(self, other):
#         return self.__add__(other)

#     def __isub__(self, other):
#         return self.__sub__(other)

#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers

#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers

#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers

#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers

#     def __str__(self):
#         return f"Airplane(max_passengers={self.max_passengers}, passengers={self.passengers})"
    
# plane1 = Airplane(100)
# plane2 = Airplane(50)

# print(plane1 == plane2)  # False

# plane1 + 20  # добавляем 20 пассажиров
# print(plane1)  # Airplane(max_passengers=100, passengers=20)

# plane1 - 10  # удаляем 10 пассажиров
# print(plane1)  # Airplane(max_passengers=100, passengers=10)

# print(plane1 > plane2)  # True
# print(plane1 < plane2)  # False          






## Определение класса

## В коде определен класс под названием Airplane. У этого класса есть несколько методов, которые позволяют нам выполнять операции над объектами этого класса.

## Метод __init__

## Метод __init__ - это специальный метод в Python, который вызывается при создании объекта. Он инициализирует атрибуты объекта. В данном случае метод __init__ принимает один аргумент max_passengers, который является максимальным количеством пассажиров, которое может вместить самолет. Он также инициализирует атрибут passengers значением 0 - это текущее количество пассажиров в самолете.

## Метод __eq__

## Метод __eq__ - это специальный метод в Python, который вызывается при использовании оператора ==. Он проверяет, равны ли два объекта. В данном случае метод __eq__ проверяет, равен ли атрибут max_passengers у двух объектов Airplane.

## Метод __add__

## Метод __add__ - это специальный метод в Python, который вызывается при использовании оператора +. Он складывает два объекта вместе. В данном случае метод __add__ может принимать два типа аргументов:

## Другой объект Airplane: Проверяется, может ли текущий самолет вместить всех пассажиров из другого самолета. Если может, то он добавляет пассажиров из другого самолета в текущий самолет. Если нет, то возвращается сообщение об ошибке.
## Integer: Проверяет, не превысит ли добавление целого числа к текущему количеству пассажиров максимальную вместимость самолета. Если нет, то добавляет целое число к текущему числу пассажиров. Если да, то возвращается сообщение об ошибке.
## Метод __sub__

## Метод __sub__ похож на метод __add__, но он вычитает, а не прибавляет. Он также может принимать два типа аргументов:

## Другой объект Airplane: Проверяется, достаточно ли пассажиров в текущем самолете, чтобы удалить всех пассажиров из другого самолета. Если да, то он удаляет пассажиров из другого самолета из текущего самолета. Если нет, то возвращается сообщение об ошибке.
## Целое число: Проверяет, не приведет ли вычитание целого числа из текущего количества пассажиров к отрицательному числу. Если нет, то вычитает целое число из текущего количества пассажиров. Если да, то возвращается сообщение об ошибке.
## Методы __iadd__ и __isub__

## Эти методы похожи на методы __add__ и __sub__, но они изменяют объект на месте, а не возвращают новый объект.

## Методы сравнения

## Методы __gt__, __lt__, __ge__ и __le__ - это специальные методы в Python, которые вызываются при использовании операторов сравнения (например, >, <, >=, <=). Они сравнивают атрибут max_passengers двух объектов Airplane.

## Метод __str__

## Метод __str__ - это специальный метод в Python, который вызывается при использовании функции str(). Он возвращает строковое представление объекта.

## Пример использования

## Код создает два объекта Airplane, plane1 и plane2, с максимальной вместимостью 100 и 50 пассажиров соответственно.

## Затем он проверяет, равен ли самолет1 самолету2, используя оператор ==, который вызывает метод __eq__. Поскольку максимальные вместимости разные, он возвращает False.

## Затем он добавляет 20 пассажиров к самолету1 с помощью оператора +, который вызывает метод __add__. Поскольку текущее количество пассажиров (0) плюс 20 меньше или равно максимальной вместимости (100), он добавляет 20 пассажиров в самолет1.

## Затем он вычитает 10 пассажиров из самолета1 с помощью оператора -, который вызывает метод __sub__. Поскольку текущее количество пассажиров (20) минус 10 больше или равно 0, он вычитает 10 пассажиров из самолета1.

## Наконец, он сравнивает самолет1 и самолет2 с помощью операторов > и <, которые вызывают методы __gt__ и __lt__ соответственно. Поскольку максимальная вместимость самолета1 больше, чем у самолета2, он возвращает True для оператора > и False для оператора <.





## Задание 4
## Создать класс Flat (квартира). Реализовать перегру-
## женные операторы:
## ■ Проверка на равенство площадей квартир (операция
## ==);
## ■ Проверка на неравенство площадей квартир (опера-
## ция !=);
## ■ Сравнение двух квартир по цене (операции > < <= >=).





# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price

#     def __eq__(self, other):
#         if not isinstance(other, Flat):
#             raise TypeError("Нельзя сравнивать с объектом другого класса")
#         return self.area == other.area

#     def __ne__(self, other):
#         if not isinstance(other, Flat):
#             raise TypeError("Нельзя сравнивать с объектом другого класса")
#         return self.area != other.area

#     def __gt__(self, other):
#         if not isinstance(other, Flat):
#             raise TypeError("Нельзя сравнивать с объектом другого класса")
#         return self.price > other.price

#     def __lt__(self, other):
#         if not isinstance(other, Flat):
#             raise TypeError("Нельзя сравнивать с объектом другого класса")
#         return self.price < other.price

#     def __ge__(self, other):
#         if not isinstance(other, Flat):
#             raise TypeError("Нельзя сравнивать с объектом другого класса")
#         return self.price >= other.price

#     def __le__(self, other):
#         if not isinstance(other, Flat):
#             raise TypeError("Нельзя сравнивать с объектом другого класса")
#         return self.price <= other.price

#     def __str__(self):
#         return f"Flat(area={self.area}, price={self.price})"

# flat1 = Flat(100, 1000)
# flat2 = Flat(100, 2000)
# print(flat1)  # Flat(area=100, price=1000)
# print(flat2)  # Flat(area=100, price=2000)
# print(flat1 == flat2)  # True
# print(flat1 != flat2)  # False
# print(flat1 > flat2)  # False
# print(flat1 < flat2)  # True







## Определение класса

## В коде определен класс Flat со следующими атрибутами:

## площадь: целое число, представляющее площадь квартиры
## цена: целое число, представляющее цену квартиры.
## Класс имеет несколько специальных методов (также известных как «магические методы» или «методы Дандера»), которые используются для переопределения поведения по умолчанию встроенных операторов Python.

## Метод __init__

## Метод __init__ - это специальный метод, который вызывается при создании объекта. Он инициализирует атрибуты объекта заданными значениями. В данном случае он устанавливает атрибуты area и price объекта Flat.

## Методы __eq__ и __ne__

## Метод __eq__ используется для переопределения оператора ==, который проверяет равенство между двумя объектами. В данном случае он проверяет, равен ли атрибут area двух объектов Flat.

## Метод __ne__ используется для переопределения оператора !=, который проверяет неравенство между двумя объектами. Он просто возвращает значение, противоположное методу __eq__.

## Методы __gt__, __lt__, __ge__ и __le__

## Эти методы используются для переопределения операторов сравнения:

## __gt__: Оператор >, проверяет, больше ли атрибут цены текущего объекта, чем атрибут цены другого объекта.
## __lt__: < оператор, проверяет, меньше ли атрибут цены текущего объекта, чем атрибут цены другого объекта.
## __ge__: >= оператор, проверяет, больше или равен ли атрибут цены текущего объекта атрибуту цены другого объекта.
## __le__: <= оператор, проверяет, меньше или равен ли атрибут цены текущего объекта атрибуту цены другого объекта.
## Метод __str__

## Метод __str__ используется для переопределения функции str(), которая возвращает строковое представление объекта. В данном случае возвращается строка в формате Flat(area=<area>, price=<price>).

## Создание и сравнение объектов

## Код создает два объекта Flat, flat1 и flat2, с разными ценами, но одинаковой площадью.

## Затем код печатает строковое представление каждого объекта с помощью функции print().

## Наконец, код сравнивает два объекта с помощью переопределенных операторов сравнения:

## flat1 == flat2 проверяет, равны ли атрибуты площади, что является истиной.
## flat1 != flat2 проверяет, не равны ли атрибуты области, что является False.
## flat1 > flat2 проверяет, что атрибут цены flat1 больше атрибута цены flat2, что является Ложью.
## flat1 < flat2 проверяет, что ценовой атрибут flat1 меньше ценового атрибута flat2, что является Истиной.







## Модуль 10 Объектно-ориентированное
## программирование
## Тема: Классы. Объекты. Часть 1






##  Задание 1
##  Реализуйте класс «Автомобиль». Необходимо хранить
##  в полях класса: название модели, год выпуска, произво-
##  дителя, объем двигателя, цвет машины, цену. Реализуйте
##  методы класса для ввода данных, вывода данных, реа-
##  лизуйте доступ к отдельным полям через методы класса.







# class Car:
#     def __init__(self, model=None, year=None, manufacturer=None, engine_volume=None, color=None, price=None):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_volume = engine_volume
#         self.color = color
#         self.price = price

#     def input_data(self):
#         self.model = input("Введите модель: ")
#         self.year = int(input("Введите год выпуска: "))
#         self.manufacturer = input("Введите производителя: ")
#         self.engine_volume = float(input("Введите объем двигателя: "))
#         self.color = input("Введите цвет: ")
#         self.price = float(input("Введите цену: "))

#     def output_data(self):
#         print(f"Модель: {self.model}")
#         print(f"Год выпуска: {self.year}")
#         print(f"Производитель: {self.manufacturer}")
#         print(f"Объем двигателя: {self.engine_volume}")
#         print(f"Цвет: {self.color}")
#         print(f"Цена: {self.price}")

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         return self.year

#     def get_manufacturer(self):
#         return self.manufacturer

#     def get_engine_volume(self):
#         return self.engine_volume

#     def get_color(self):
#         return self.color

#     def get_price(self):
#         return self.price

# # Создаем объект Car и вводим данные
# my_car = Car()
# my_car.input_data()
# my_car.output_data()
# print(my_car.get_model())







# # Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.






# class Book:
#     def __init__(self, title=None, year=None, publisher=None, genre=None, author=None, price=None):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price

#     def input_data(self):
#         self.title = input("Введите название книги: ")
#         self.year = int(input("Введите год выпуска: "))
#         self.publisher = input("Введите издателя: ")
#         self.genre = input("Введите жанр: ")
#         self.author = input("Введите автора: ")
#         self.price = float(input("Введите цену: "))

#     def output_data(self):
#         print(f"Название книги: {self.title}")
#         print(f"Год выпуска: {self.year}")
#         print(f"Издатель: {self.publisher}")
#         print(f"Жанр: {self.genre}")
#         print(f"Автор: {self.author}")
#         print(f"Цена: {self.price}")

#     def get_title(self):
#         return self.title

#     def get_year(self):
#         return self.year

#     def get_publisher(self):
#         return self.publisher

#     def get_genre(self):
#         return self.genre

#     def get_author(self):
#         return self.author

#     def get_price(self):
#         return self.price

# # Создаем объект Book и вводим данные
# my_book = Book()
# my_book.input_data()
# my_book.output_data()
# print(my_book.get_title())







# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.





# class Stadium:
#     def __init__(self, name=None, opening_date=None, country=None, city=None, capacity=None):
#         self.name = name
#         self.opening_date = opening_date
#         self.country = country
#         self.city = city
#         self.capacity = capacity

#     def input_data(self):
#         self.name = input("Введите название стадиона: ")
#         self.opening_date = input("Введите дату открытия (в формате дд.мм.гггг): ")
#         self.country = input("Введите страну: ")
#         self.city = input("Введите город: ")
#         self.capacity = int(input("Введите вместимость: "))

#     def output_data(self):
#         print(f"Название стадиона: {self.name}")
#         print(f"Дата открытия: {self.opening_date}")
#         print(f"Страна: {self.country}")
#         print(f"Город: {self.city}")
#         print(f"Вместимость: {self.capacity}")

#     def get_name(self):
#         return self.name

#     def get_opening_date(self):
#         return self.opening_date

#     def get_country(self):
#         return self.country

#     def get_city(self):
#         return self.city

#     def get_capacity(self):
#         return self.capacity

# # Создаем объект Stadium и вводим данные
# my_stadium = Stadium()
# my_stadium.input_data()
# my_stadium.output_data()
# print(my_stadium.get_name())





## Модуль 10 Объектно-ориентированное
## программирование
## Тема: Классы. Объекты. Конструкторы.
## Перегрузка методов. Часть 2





# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# конструктор, а также необходимые перегруженные методы.


# class Car:
#     def __init__(self, model=None, year=None, manufacturer=None, engine_volume=None, color=None, price=None):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_volume = engine_volume
#         self.color = color
#         self.price = price

#     def __str__(self):
#         return f"Модель: {self.model}, Год выпуска: {self.year}, Производитель: {self.manufacturer}, Объем двигателя: {self.engine_volume}, Цвет: {self.color}, Цена: {self.price}"

#     def __repr__(self):
#         return f"Car('{self.model}', {self.year}, '{self.manufacturer}', {self.engine_volume}, '{self.color}', {self.price})"

#     def __eq__(self, other):
#         return self.model == other.model and self.year == other.year and self.manufacturer == other.manufacturer

#     def input_data(self):
#         self.model = input("Введите модель: ")
#         self.year = int(input("Введите год выпуска: "))
#         self.manufacturer = input("Введите производителя: ")
#         self.engine_volume = float(input("Введите объем двигателя: "))
#         self.color = input("Введите цвет: ")
#         self.price = float(input("Введите цену: "))

#     def output_data(self):
#         print(f"Модель: {self.model}")
#         print(f"Год выпуска: {self.year}")
#         print(f"Производитель: {self.manufacturer}")
#         print(f"Объем двигателя: {self.engine_volume}")
#         print(f"Цвет: {self.color}")
#         print(f"Цена: {self.price}")

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         return self.year

#     def get_manufacturer(self):
#         return self.manufacturer

#     def get_engine_volume(self):
#         return self.engine_volume

#     def get_color(self):
#         return self.color

#     def get_price(self):
#         return self.price

# # Создаем объект Car и вводим данные
# my_car = Car()
# my_car.input_data()
# print(my_car)  # Используем перегруженный метод __str__
# print(repr(my_car))  # Используем перегруженный метод __repr__

# # Создаем другой объект Car
# my_car2 = Car("Toyota", 2020, "Toyota Motor Corporation", 2.0, "Silver", 25000)
# print(my_car2)

# # Сравниваем два объекта Car
# print(my_car == my_car2)  # Используем перегруженный метод __eq__







# Задание 2
# К уже реализованному классу «Книга» добавьте кон-
# структор, а также необходимые перегруженные методы.






# class Book:
#     def __init__(self, title=None, author=None, year=None, publisher=None, pages=None, price=None):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.publisher = publisher
#         self.pages = pages
#         self.price = price

#     def __str__(self):
#         return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}, Издательство: {self.publisher}, Количество страниц: {self.pages}, Цена: {self.price}"

#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.year}, '{self.publisher}', {self.pages}, {self.price})"

#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author and self.year == other.year

#     def input_data(self):
#         self.title = input("Введите название книги: ")
#         self.author = input("Введите автора: ")
#         self.year = int(input("Введите год издания: "))
#         self.publisher = input("Введите издательство: ")
#         self.pages = int(input("Введите количество страниц: "))
#         self.price = float(input("Введите цену: "))

#     def output_data(self):
#         print(f"Название: {self.title}")
#         print(f"Автор: {self.author}")
#         print(f"Год издания: {self.year}")
#         print(f"Издательство: {self.publisher}")
#         print(f"Количество страниц: {self.pages}")
#         print(f"Цена: {self.price}")

#     def get_title(self):
#         return self.title

#     def get_author(self):
#         return self.author

#     def get_year(self):
#         return self.year

#     def get_publisher(self):
#         return self.publisher

#     def get_pages(self):
#         return self.pages

#     def get_price(self):
#         return self.price

# # Создаем объект Book и вводим данные
# my_book = Book()
# my_book.input_data()
# print(my_book)  # Используем перегруженный метод __str__
# print(repr(my_book))  # Используем перегруженный метод __repr__

# # Создаем другой объект Book
# my_book2 = Book("Python для начинающих", "Джон Смит", 2020, "ООО 'Издательство'", 300, 1500)
# print(my_book2)

# # Сравниваем два объекта Book
# print(my_book == my_book2)  # Используем перегруженный метод __eq__







## Задание 3
## К уже реализованному классу «Стадион» добавьте
## конструктор, а также необходимые перегруженные методы.





# class Stadium:
#     def __init__(self, name=None, location=None, capacity=None, opened_year=None, description=None):
#         self.name = name
#         self.location = location
#         self.capacity = capacity
#         self.opened_year = opened_year
#         self.description = description

#     def __str__(self):
#         return f"Название: {self.name}, Местоположение: {self.location}, Вместимость: {self.capacity}, Год открытия: {self.opened_year}, Описание: {self.description}"

#     def __repr__(self):
#         return f"Stadium('{self.name}', '{self.location}', {self.capacity}, {self.opened_year}, '{self.description}')"

#     def __eq__(self, other):
#         return self.name == other.name and self.location == other.location

#     def input_data(self):
#         self.name = input("Введите название стадиона: ")
#         self.location = input("Введите местоположение стадиона: ")
#         self.capacity = int(input("Введите вместимость стадиона: "))
#         self.opened_year = int(input("Введите год открытия стадиона: "))
#         self.description = input("Введите описание стадиона: ")

#     def output_data(self):
#         print(f"Название: {self.name}")
#         print(f"Местоположение: {self.location}")
#         print(f"Вместимость: {self.capacity}")
#         print(f"Год открытия: {self.opened_year}")
#         print(f"Описание: {self.description}")

#     def get_name(self):
#         return self.name

#     def get_location(self):
#         return self.location

#     def get_capacity(self):
#         return self.capacity

#     def get_opened_year(self):
#         return self.opened_year

#     def get_description(self):
#         return self.description

# # Создаем объект Stadium и вводим данные
# my_stadium = Stadium()
# my_stadium.input_data()
# print(my_stadium)  # Используем перегруженный метод __str__
# print(repr(my_stadium))  # Используем перегруженный метод __repr__

# # Создаем другой объект Stadium
# my_stadium2 = Stadium("Лужники", "Москва", 81000, 1956, "Один из крупнейших стадионов России")
# print(my_stadium2)

# # Сравниваем два объекта Stadium
# print(my_stadium == my_stadium2)  # Используем перегруженный метод __eq__






## Модуль 10 Объектно-ориентированное
## программирование
## Тема: Статические методы





## Задание 1
## К уже реализованному классу «Дробь» добавьте ста-
## тический метод, который при вызове возвращает коли-
## чество созданных объектов класса «Дробь».

