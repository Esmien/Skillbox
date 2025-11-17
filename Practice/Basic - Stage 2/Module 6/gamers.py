def get_name_of_player(players_dict: dict,
                       player_team: str,
                       player_status: str) -> list[str]:
    """
    Ищет игроков по заданным критериям - команда и статус
    :param players_dict: словарь словарей со всеми игроками по порядку {player_num: {player_data}}
    :param player_team: название команды str(team)
    :param player_status: искомый статус str(status)
    :return: список игроков, отобранных по заданным критериям [players_names]
    """
    return [
            player['name']
            for player in players_dict.values()
            if player['team'] == player_team and player['status'] == player_status
    ]
def main():
    players_dict = {
        1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
        2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
        3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
        4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
        5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
        6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
        7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
        8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
    }
    queries = [
        ('A', 'Rest'),
        ('B', 'Training'),
        ('C', 'Travel'),
    ]
    status_translation = {
        'Rest': 'отдыхают',
        'Training': 'тренируются',
        'Travel': 'путешествуют'
    }
    for team, status in queries:
        players = get_name_of_player(players_dict, team, status)
        status_ru = status_translation[status]
        print(f'Все члены команды {team}, которые {status_ru}: ')
        print(*players, sep=', ')
        print()

if __name__ == '__main__':
    main()