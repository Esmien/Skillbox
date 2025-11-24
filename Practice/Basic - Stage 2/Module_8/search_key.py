site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search_key(data, tag):
    if tag in data:
        return data[tag]
    for sub_data in data.values():
        if isinstance(sub_data, dict):
            result = search_key(sub_data, tag)
            if result:
                return result
    return None

print(search_key(site, 'div'))