class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Создаем объект класса Rectangle
rect = Rectangle(5, 10)
rect1 = Rectangle(10, 15)
rect2 = Rectangle(3, 9)

# Вычисляем площадь
print(f"Площадь прямоугольника: {rect.area()}")  # Площадь прямоугольника
print(f"Площадь прямоугольника: {rect1.area()}")
print(f"Площадь прямоугольника: {rect2.area()}")

# Вычисляем периметр
print(f"Периметр прямоугольника: {rect.perimeter()}") #Периметр прямоугольника
print(f"Периметр прямоугольника: {rect1.perimeter()}")
print(f"Периметр прямоугольника: {rect2.perimeter()}")


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


    def multiplication(self):
        return self.a * self.b


    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            raise ValueError("Деление на 0 невозможно")


    def subtraction(self):
        return  self.a - self.b


m = Math(100, 20)

# Вызов методов
print(m.addition())
print(m.multiplication())
print(m.division())
print(m.subtraction())



class Button:
    def __init__(self, text, button_type="Кнопка", locator=""):
        self.text = text
        self.type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке '{self.text}'"

# Создаём список кнопок
buttons = [
    Button("Text Box"),
    Button("Check Box"),
    Button("Radio Button"),
    Button("Web Tables"),
    Button("Buttons"),
    Button("Links"),
    Button("Broken Links - Images"),
    Button("Upload and Download"),
    Button("Properties"),
]

# b. вывод текста для каждой кнопки
for button in buttons:
    print(button.text)

# c. вызываем "Клик" для каждой кнопки
for button in buttons:
    print(button.click())


#Доп*

class Car:
    def __init__(self, color=None, car_type=None, year=None):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведён.")

    def stop_engine(self):
        print("Автомобиль заглушен.")

    def set_year(self, new_year):
        self.year = new_year

    def set_car_type(self, new_type):
        self.car_type = new_type

    def set_color(self, new_color):
        self.color = new_color


# Создаем объект класса Car без указания параметров
my_car = Car()

# Запускаем двигатель
my_car.start_engine()  

# Присваиваем новые значения атрибутам
my_car.set_year(2013)
my_car.set_car_type("hatchback")
my_car.set_color("gray")

# Проверяем текущие значения атрибутов
print(my_car.year)     
print(my_car.car_type) 
print(my_car.color)    

# Останавливаем двигатель
my_car.stop_engine()   
