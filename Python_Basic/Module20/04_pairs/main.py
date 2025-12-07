import random

def get_pairs(numbers: list) -> list[tuple[int, int]]:
    return [(numbers[i], numbers[i+1])
            for i in range(0, len(numbers) - 1, 2)]

def main():
    numbers = [random.randint(1, 10) for _ in range(10)]
    print(numbers)
    print(get_pairs(numbers))

if __name__ == '__main__':
    main()