try:#1.	Ввести строку, вывести на экран только слова, имеющие заданную длину.
    print('Введите строку')
    s = input()  #Вводится строка
    print('Введите число')
    l = int(input())  #Вводится число
    w = s.split()  #Cтрока разделяется на слова
    for i in w:  #Для каждого слова проверяется, является ли его длина равной введенному числу
        if len(i) == l: #Если условие выполняется, то слово выводится на экран
            print(i)
    if l<0:#Если введено отрицательное число, программа выводит сообщение
        print('Введите сначала строку, а потом положительное число!')
except ValueError:#В случае ошибки ввода, вводится соответствующее сообщение
    print('Введите сначала строку, а потом положительное число!')
except NameError:
    print('Введите сначала строку, а потом положительное число!')
## перевет






