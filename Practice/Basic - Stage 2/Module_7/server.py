server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
for title, data in server_data.items():
    print(f'{title}:')
    for parameter, value in data.items():
        print(f'\t{parameter}: {value}')
