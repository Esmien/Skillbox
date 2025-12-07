def my_zip(data_1, data_2):
    list_1 = list(data_1)
    list_2 = list(data_2)
    min_len = min(len(list_1), len(list_2))
    return (
        (list_1[i], list_2[i])
        for i in range(min_len)
    )

def main():
    data_1 = {'a': 1, 'b': 2, 'c': 3}
    data_2 = {'d': 4, 'e': 5, 'f': 6}
    result = my_zip(data_1, data_2)
    print(result)
    for item in result:
        print(item)

if __name__ == "__main__":
    main()