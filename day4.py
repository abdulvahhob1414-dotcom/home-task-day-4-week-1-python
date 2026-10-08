
# 1. Добавление элемента
# Дан список:
numbers = [10, 20, 30, 40]
# Добавь число 50 в конец списка с помощью append().
numbers.append(50)
print(numbers)

# 2. Добавление нескольких элементов
# Дан список:
languages = ["Python", "C++"]
zabon =["Java", "Go", "Rust"]
# Добавь "Java", "Go" и "Rust" с помощью extend().
languages.extend(zabon)
print(languages)

# 3. Вставка элемента
# Дан список:
students = ["Ali", "Muhammad", "John"]
# Вставь "Hakim" на позицию с индексом 1 с помощью insert().
students.insert(1,"Hakim")
print(students)

# 4. Удаление последнего элемента
# Дан список:
numbers = [10, 20, 30, 40, 50]
rakam=numbers.pop(-1)
print(rakam)
# Удали последний элемент с помощью pop() и выведи удалённое значение.

# 5. Удаление конкретного элемента
# Дан список:
fruits = ["apple", "banana", "orange", "banana"]
# Удали первое "banana" с помощью remove().
fruits.remove('banana')
print(fruits)

# 6. Подсчёт элементов
# Дан список:
numbers = [1, 2, 3, 2, 4, 2, 5, 2]
z=numbers.count(2)
print(z)
# С помощью count() узнай, сколько раз встречается число 2.

# 7. Поиск позиции
# Дан список:
students = ["Ali", "John", "Muhammad", "Said"]
print(students.index(2))
# С помощью index() найди индекс "Muhammad".

# 8. Копирование списка
# Дан список:
numbers = [1, 2, 3, 4, 5]
numbers2=numbers.copy()
print(numbers2)
# Создай его независимую копию с помощью copy(). Измени копию и докажи, что оригинальный список не изменился.


# 9. Очистка списка
# Дан список:
cart = ["phone", "laptop", "mouse", "keyboard"]
cart.clear()
print(cart)
# Полностью очисти корзину с помощью clear().

# 10. Разворот списка
# Дан список:
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
# Разверни его в обратном порядке с помощью reverse().

# 11. Сортировка чисел
# Дан список:
numbers = [45, 12, 78, 3, 29, 10]
numbers.sort()
print(numbers)
# Отсортируй список по возрастанию с помощью sort().

# 12. Сортировка по убыванию
# Дан список:
# # Отсортируй его по убыванию, используя sort().
numbers = [15, 4, 89, 32, 7, 21]
numbers.reverse()
numbers.sort()
print(numbers)

# 13. Работа с двумя списками
# Даны:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list1.append(7)
# Добавь все элементы list2 в list1 с помощью extend().
# Затем добавь число 7 с помощью append().

# 14. Управление очередью
# Дан список:
queue = ["Ali", "John", "Muhammad", "Said"]
queue.pop(0)
queue.append('Rustam')
queue.insert(0,'Karim')
print(queue)
# Удали первого человека с помощью pop().
# Добавь "Rustam" в конец.
# Добавь "Karim" в начало списка с помощью insert().
# Выведи итоговый список.

# 15. Работа с оценками
# Дан список оценок:
grades = [75, 90, 60, 90, 85, 70, 90]
print(grades.count(90))
print(grades.index(85))
grades.append(95)
grades.remove(60)
grades.sort()
grades.reverse()
print(grades)
# Выполни следующие действия:
# Узнай, сколько раз встречается 90 с помощью count().
# Найди индекс первой оценки 85 с помощью index().
# Добавь оценку 95 через append().
# Удали одну оценку 60 через remove().
# Отсортируй оценки по возрастанию через sort().
# Разверни список через reverse().
# Выведи итоговый список.


# 16. Список покупок
shopping = ["bread", "milk", "eggs", "cheese"]
ls2=["juice", "water"]
shopping.append('butter')
shopping.extend(ls2)
shopping.insert(1,'meat')
shopping.remove("eggs")
shopping.sort()
print(shopping)
# Добавь "butter" через append().
# Добавь "juice" и "water" через extend().
# Вставь "meat" на индекс 1 через insert().
# Удали "eggs" через remove().
# Отсортируй список через sort().

# 17. Баллы студентов
scores = [85, 70, 95, 60, 85, 75]
print(scores.count(85))
print(scores.index(95))
scores.append(100)
scores.remove(60)
scores.sort()
print(scores)
# Узнай количество 85 через count().
# Найди индекс 95 через index().
# Добавь 100 через append().
# Удали 60 через remove().
# Отсортируй список по возрастанию.

# 18. Имена студентов
students = ["Ali", "John", "Said", "Ali", "Karim"]
print(students.count("Ali"))
print(students.index("Said"))
students.append("Muhammad")
students.insert(2,"Rustam")
students.remove("Ali")
print(students)
# Узнай количество "Ali".
# Найди индекс "Said".
# Добавь "Muhammad" в конец.
# Вставь "Rustam" на индекс 2.
# Удали первое "Ali".

# 19. Очередь клиентов
queue = ["Client1", "Client2", "Client3", "Client4"]
queue2=["Client6", "Client7"]
queue.pop(0)
queue.append("Client5")
queue.extend(queue2)
queue.insert(0,"VIP")
queue.remove("Client3")
print(queue)
# Удали первого клиента через pop().
# Добавь "Client5" через append().
# Добавь "Client6" и "Client7" через extend().
# Вставь "VIP" в начало.
# Удали "Client3".

# 20. Цены товаров
prices = [120, 450, 300, 150, 450, 200]
print(prices.count(450))
print(prices.index(300))
prices.append(500)
prices.pop(0)
prices.sort()
print(prices)
# Узнай количество цены 450.
# Найди индекс цены 300.
# Добавь 500.
# Удали 120.
# Отсортируй цены по возрастанию.

# 21. Языки программирования
languages = ["Python", "C++", "Java"]
languages.append("Go")
languages2=["Rust", "JavaScript"]
languages.extend(languages2)
languages.insert(1,"C")
languages.remove("Java")
languages.reverse()
print(languages)
# Добавь "Go" в конец.
# Добавь "Rust" и "JavaScript" через extend().
# Вставь "C" на индекс 1.
# Удали "Java".
# Разверни список через reverse().

# 22. Копия списка
numbers = [10, 20, 30, 40, 50]
numbers2=numbers.copy()
numbers2.append(60)
numbers2.pop(1)
numbers2.sort()
print(numbers)
print(numbers2)
# Создай копию через copy().
# Добавь 60 в копию.
# Удали 20 из копии.
# Отсортируй копию.
# Выведи оригинал и копию и сравни их.

# 23. Корзина интернет-магазина
cart = ["phone", "mouse", "keyboard"]
cart2=["headphones", "webcam"]
cart.append("monitor")
cart.extend(cart2)
cart.insert(0,"laptop")
cart.remove("mouse")
cart.pop(-1)
print(cart)
# Добавь "monitor".
# Добавь "headphones" и "webcam".
# Вставь "laptop" на индекс 0.
# Удали "mouse".
# Удали последний товар через pop().


# 24. Номера
numbers = [5, 10, 15, 10, 20, 10]
print(numbers.count(10))
print(numbers.index(20))
numbers.append(25)
numbers.pop(1)
numbers.sort()
numbers.reverse()
print(numbers)
# Посчитай количество 10.
# Найди индекс первого 20.
# Добавь 25.
# Удали одно число 10.
# Отсортируй список по убыванию.

# 25. Игроки
players = ["Messi", "Ronaldo", "Neymar", "Mbappe"]
players.append("Haaland")
players.insert(2,"Salah")
players.remove("Neymar")
print(players.index("Ronaldo"))
players.reverse()
print(players)
# Добавь "Haaland".
# Вставь "Salah" на индекс 2.
# Удали "Neymar".
# Найди индекс "Ronaldo".
# Разверни список.

# 26. Задачи Todo
tasks = ["study", "work", "sleep"]
tasks.append("exercise")
tasks2=["read", "code"]
tasks.extend(tasks2)
tasks.insert(1,"eat")
tasks.remove("sleep")
tasks.sort()
print(tasks)
# Добавь "exercise".
# Добавь "read" и "code".
# Вставь "eat" на индекс 1.
# Удали "sleep".
# Отсортируй список.

# 27. Температура
temperatures = [25, 30, 28, 25, 32, 25]
print(temperatures.count(25))
print(temperatures.index(32))
temperatures.append(35)
temperatures.pop(2)
temperatures.sort()
print(temperatures)
# Посчитай количество 25.
# Найди индекс 32.
# Добавь 35.
# Удали одну 28.
# Отсортируй список по возрастанию.

# 28. Города
cities = ["Dushanbe", "Khujand", "Bokhtar"]
cities2=["Tursunzoda", "Istaravshan"]
cities.append("Kulob")
cities.extend(cities2)
cities.insert(1,"Hisor")
cities.remove("Bokhtar")
cities.reverse()
print(cities)
# Добавь "Kulob".
# Добавь "Tursunzoda" и "Istaravshan".
# Вставь "Hisor" на индекс 1.
# Удали "Bokhtar".
# Разверни список.

# 29. Работники
employees = ["Ali", "Said", "John", "Karim"]
employees.append("Rustam")
employees.insert(2,"Muhammad")
print(employees.index("John"))
employees.remove("Said")
employees2=employees.copy()
print(employees)
print(employees2)
# Добавь "Rustam".
# Вставь "Muhammad" на индекс 2.
# Найди индекс "John".
# Удали "Said".
# Создай копию списка через copy().

# 30. Числа и копия
numbers = [9, 3, 7, 3, 5, 3]
numbers2=numbers.copy()
print(numbers.count(3))
numbers2.append(10)
numbers2.pop(1)
numbers2.sort()
print(numbers)
print(numbers2)
# Создай копию списка.
# Посчитай количество 3 в оригинале.
# Добавь 10 в копию.
# Удали одну 3 из копии.
# Отсортируй копию.

# 31. Музыка
songs = ["Song A", "Song B", "Song C", "Song A"]
print(songs.count("Song A"))
print(songs.index("Song C"))
songs.append("Song D")
songs.insert(1,"Song E")
songs.remove("Song A")
print(songs)
# Посчитай количество "Song A".
# Найди индекс "Song C".
# Добавь "Song D".
# Вставь "Song E" на индекс 1.
# Удали одну "Song A".

# 32. Очередь заказов
orders = [101, 102, 103, 104]
orders.pop(0)
orders.append(105)
orders2=[106,107]
orders.extend(orders2)
orders.insert(0,100)
orders.sort()
print(orders)
# Удали первый заказ через pop().
# Добавь заказ 105.
# Добавь заказы 106 и 107.
# Вставь заказ 100 в начало.
# Отсортируй список.

# 33. Рейтинг
rating = [5, 4, 3, 5, 2, 5, 4]
print(rating.count(5))
print(rating.index(2))
rating.append(1)
rating.remove(3)
rating.reverse()
rating.sort()
# Посчитай количество 5.
# Найди индекс 2.
# Добавь 1.
# Удали одну оценку 3.
# Отсортируй список по убыванию.

# 34. Инвентарь
inventory = ["laptop", "phone", "tablet"]
inventory2=["mouse", "keyboard"]
inventory.append("monitor")
inventory.extend(inventory2)
inventory.insert(2,"printer")
inventory.remove("tablet")
inventory.pop(-1)
print(inventory)
# Добавь "monitor".
# Добавь "mouse" и "keyboard".
# Вставь "printer" на индекс 2.
# Удали "tablet".
# Удали последний элемент через pop().

# 35. Полная очистка
data = [10, 20, 30, 40, 50]
data2=data.copy()
data2.append(60)
data2.remove(30)
data2.reverse()
data.clear()
print(data2)
# Создай копию через copy().
# Добавь 60 в копию.
# Удали 30 из копии.
# Разверни копию.
# Полностью очисти оригинальный список через clear().