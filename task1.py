"""
Завдання 5.1
Створення функції для обрахунку ряду Фібоначчі, яка
використовує кешування для спрощення обрахунків
"""


def caching_fibonacci():
    # Створення словника для кешу
    cache: dict[int, int] = {0: 0, 1: 1}  # додаємо виняткові значення 0 та 1

    def fibonacci(number: int) -> int:  # Ф-ція Фібоначчі
        if number < 0:  # Для значень менше 0
            return 0
        elif number in cache:  # У випадку якщо було вже обчислення n
            return cache[number]  # де n --> number
        else:  # Якщо у кеші немає обчисленого n
            cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
            return cache[number]

    return fibonacci


def main():
    fib = caching_fibonacci()

    test_value = [1, 1, 5, 5, 10, 10, 20, 20]  # Тестові значення
    for n in test_value:  # Виводимо результат
        print(f"fib({n}) = {fib(n)}")


if __name__ == "__main__":
    main()
