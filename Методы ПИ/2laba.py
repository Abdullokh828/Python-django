def task1():
    text = input("Введите строку: ")
    words = text.split()  # разделяем по пробелам
    longest = max(words, key=len)
    print("Самое длинное слово:", longest)


def task2():
    text = input("Введите строку (слова разделены ';'): ")
    words = text.split(';')  # разделяем по точке с запятой
    longest = max(words, key=len)
    print("Самое длинное слово:", longest)


def task3():
    text = input("Введите строку: ")
    delimiter = input("Введите разделитель: ")
    words = text.split(delimiter)  # разделяем по введённому символу
    shortest = min(words, key=len)
    print("Самое короткое слово:", shortest)


def task4():
    text = input("Введите строку: ")
    word = input("Введите слово для поиска: ")
    if word in text.split():
        print("Слово найдено!")
    else:
        print("Слово не найдено!")


def task5():
    text = input("Введите предложение: ")
    words = text.split()
    print("Количество слов:", len(words))


# --- Главное меню ---
while True:
    print("\nВыберите задачу:")
    print("1 - Самое длинное слово (разделитель пробел)")
    print("2 - Самое длинное слово (разделитель ';')")
    print("3 - Самое короткое слово (разделитель задаёт пользователь)")
    print("4 - Поиск слова в строке")
    print("5 - Подсчёт количества слов")
    print("0 - Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task4()
    elif choice == "5":
        task5()
    elif choice == "0":
        print("Выход из программы...")
        break
    else:
        print("Ошибка! Нет такой задачи.")
