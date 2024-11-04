def task_1():
    # Создаем 5 разных переменных с произвольным названием.
    a: int = 10
    b: float = 3.14
    c: str = "Hello, World!"
    d: list = [1, 2, 3]
    e: bool = True

    # Выводим тип данных каждой переменной в консоль.
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

    # Добавляем аннотацию возвращаемых данных.
    return (a, b, c, d, e)


#Добавляем вызов функции.
result = task_1()
print("Результат функции:")
print(result)



def task_2():
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3])  # выводим первые три элемента списка

    # Добавляем аннотацию возвращаемых данных.
    return a

# Добавляем вызов функции.
result = task_2()
print("Результат функции:")
print(result)

# Определяем последовательность чисел
print("Эта последовательность называется числами Фибоначчи")



def task_3(num):
    return num ** 2

# Добавляем вызов функции.
result = task_3(5)
print("Результат функции:")
print(result)
