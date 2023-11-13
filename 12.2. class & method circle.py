import math                     #Импорт модуля для работы с числами - pi

                                #Создание класса. Название класса с большой буквы.
class Circle():                 #Спец. метод-инициализация ( определение переменных экземпляра )
    def __init__(self, pi, r):  #self,pi,r-параметры метода
        self.pi = math.pi       #Объявление Переменных экземпляра self.имя_переменнной = значение_переменной 
        self.radius = r

    def area(self):             #Вызов метода из класса и возврат результата
        return self.pi * self.radius * self.radius

circle = Circle(math.pi, 2)     #Создание экземпляра (объекта) класса.
print(circle.area())
