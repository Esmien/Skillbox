expended_time = 0
is_downloaded = False
while True:
    download_size = 123
    download_speed = 27
    downloaded_in_percentage = 0
    if download_speed <= 0 and download_size <= 0:
        print('Размер обновления и скорость соединения не могут быть меньше нуля.')
    else:
        while int(downloaded_in_percentage) < 100:
            expended_time += 1
            downloaded = download_speed * expended_time
            downloaded_in_percentage = int(downloaded / download_size * 100)
            if downloaded_in_percentage >= 100:
                downloaded_in_percentage = 100
                downloaded = download_size
                is_downloaded = True
            print(f'Прошло {expended_time} сек. Скачано {downloaded} из {download_size} - {downloaded_in_percentage}%')
        if is_downloaded:
            break