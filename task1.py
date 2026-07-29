def caching_fibonacci():
    cache: dict[int, int] = {}

    def fibonacci(number: int) -> int:
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number in cache:
            return cache[number]
        else:
            cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
            return cache[number]

    return fibonacci


def main():
    fib = caching_fibonacci()

    test_value = [1, 1, 5, 5, 10, 10, 20, 20]
    for n in test_value:
        print(f"fib({n}) = {fib(n)}")


if __name__ == "__main__":
    main()
