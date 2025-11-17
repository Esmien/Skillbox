def main():
    small_storage = {
        'гвозди': 5000,
        'шурупы': 3040,
        'саморезы': 2000
    }

    big_storage = {
        'доски': 1000,
        'балки': 150,
        'рейки': 600
    }

    big_storage.update(small_storage)
    item = input('Введите название товара: ').lower()
    amount = big_storage.get(item, 'Товар не найден')
    print(amount)

if __name__ == '__main__':
    main()