from collections.abc import Callable, Generator

"""
Завдання 5.2
Створення ф-ції generator_numbers(text: str) -> Generator[float, None, None]
для аналізу тексту та  ідентифікування всіх дійсних чисел.
"""


def generator_numbers(text: str) -> Generator[float, None, None]:
    # Генератор який ділить текст та шукає числа float
    data = text.split()
    for el in data:
        try:
            yield float(el)
        except ValueError:
            pass


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Приймає текст, який аналізуємо та рахує загал. суму
    return sum(func(text))


def main() -> None:
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
