class MyClass:
    #Поле на класа:
    color = 'Червен'
    #Методи на класа:
    def set(txt):
        MyClass.color = txt
    def show():
        print(MyClass.color)
#Извикване на методите на класа:
MyClass.show()
MyClass.set("Зелен")
#Показване стойността на полето на класа:
print(MyClass.color)
#Задаваме нова стойност за полето на класа:
MyClass.color = 'Син'
#извикваме метода на класа:
MyClass.show()
#Създаваме обекти на класа:
A = MyClass()
B = MyClass()
#Проверка на стойността на полето:
print(f'Клас: {MyClass.color}')
print(f'Обект А: {A.color}')
print(f'Обект В: {B.color}')
#Присвояваме стойност на полето:
A.color = 'Бял'
#Проверяваме стойността на полето:
print(f'Клас: {MyClass.color}')
print(f'Обект А: {A.color}')
print(f'Обект В: {B.color}')
#Защо при извикването на Обект А се принтира 'Бял', а не 'Син'? Защото на пръв поглед обекти А и В са еднакви, но всъщност не са- те имат различни места в РАМ паметта.
MyClass.color = 'Оранжев'
print(f'Клас: {MyClass.color}')
print(f'Обект А: {A.color}')
print(f'Обект В: {B.color}')
#Защо при изхода обект А остана 'Бял'? Защото при създаването на обекти А/В на класа MyClass, ние всъщност създаваме референция към самия обект MyClass,
#! Класът се реализира на основата на някакъв обект (в случая А и В), а името на класа съдържа РЕФЕРЕНЦИЯ към самия обект.
print(type(A))
print(type(B))
print(type(MyClass))
print()
#Чрез type()/id() ние разбираме типа на данните (в случая класове) и техните адреси в РАМ паметта. Всички три типа, макар и на пръв поглед еднакви, са различни, ознавайки това от различните им адреси в паметта.
print(id(A))
print(id(B))
print(id(MyClass))
print()

MyClass.color = ("Жълт")
#Проверяваме стойността на полето:
print(f'Клас: {MyClass.color}')
print(f'Обект А: {A.color}')
print(f'Обект В: {B.color}')
print()
#Защо А.колор връща 'син', а класът и обект В връщат 'Жълт'? Защото на обект В, който е референция към класа, не е придадена стойност на променлива color.
del A.color
print(f'Клас: {MyClass.color}')
print(f'Обект А: {A.color}')
print(f'Обект В: {B.color}')
#След изтриване на обект А, търсенето на A.color няма да се осъществява в обект А, а в класа MyClass.
