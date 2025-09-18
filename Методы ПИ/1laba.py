x = int (input ("Введите число от 1 до 9: "))

if 1<= x <=3:
    s = input ("Введте строку: ")
    n = int (input ("Введите число повторов строки: "))
    for i in range (n):
        print(s)

elif 4<= x <= 6: 
     m = int (input ("Введите степень: "))
     result = x**m 
     print("Резултать: ", result)

elif 7<= x <= 9:
    for i in range(10):
        x+=1
        print(x)


else:

    print("Ошибка ввода")

    