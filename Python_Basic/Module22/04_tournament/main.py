INPUT_FILENAME = 'first_tour.txt'
OUTPUT_FILENAME = 'second_tour.txt'

def get_champions(filename):
    """
    Обрабатывает и сортирует данные из файла с результатами тура
    :param filename: имя файла
    :returns список участников, прошедших во второй тур в формате 'N. Surname score'
    """
    champions = {}
    min_score = 0

    with open(filename, 'r') as f:
        for line in f:
            row = line.split()
            if len(row) == 1:
                min_score = int(row[0])
                continue
            surname, name, score = row
            score = int(score)
            name = name[0].upper() + '. '
            if score > min_score:
                champions[(surname, name)] = score

    return dict(sorted(champions.items(), key=lambda item: item[1], reverse=True))

def main():
    champions = get_champions(INPUT_FILENAME)

    with open(OUTPUT_FILENAME, 'w') as f:
        f.write(str(len(champions)) + '\n')
        for index, ((surname, name), score) in enumerate(champions.items(), start=1):
            f.write(f'{index}) {name}{surname} {score}\n')

if __name__ == '__main__':
    main()