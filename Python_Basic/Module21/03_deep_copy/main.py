# Я решил использовать именно этот подход, потому что так удобнее работать с несколькими "сайтами",
# храня список объектов с независимыми состояниями, также куда удобнее расширять в случае необходимости,
# и вообще, ООП - наш лучший друг, тут все четко, красиво и понятно,
# хоть для этой задачи на первый взгляд и смотрится избыточно

# Помимо изученного материала используются замыкания - когда внутренняя функция(метод) работает с данными внешней
# По тз все условия выполнены - вывод соответствует задаче, используется рекурсия и deepcopy
from utils import num_validator
import copy, json

class Site:
    def __init__(self, template: dict):
        self.template = copy.deepcopy(template)
        self.tags = ('title', 'h2')
    def create_new_site(self, product: str) -> dict:
        """
        Меняет заголовки(наполнение) сайта под требуемый продукт
        :param product: наименование продаваемого товара(продукта)
        :return: готовая структура сайта
        """

        def replace_in_dict(structure: dict) -> None:
            """
            Меняет шаблон сайта под требуемый продукт,
            рекурсивно находя нужные(заданные вручную) теги в HTML-структуре и
            меняя их значения используя замыкание
            :param structure: HTML-структура для изменения
            :return: None
            """
            for key, value in structure.items():
                if key in self.tags:
                    text = value.split()
                    if key == 'title':
                        text[1] = product
                    elif key == 'h2':
                        text[-1] = product
                    structure[key] = ' '.join(text)
                elif isinstance(value, dict):
                    replace_in_dict(value)

        replace_in_dict(self.template)
        return self.template

def nice_print(list_of_obj: list) -> None:
    """
    Выводит на экран HTML-структуру в формате, заданном в ТЗ
    :param list_of_obj: список отдельных объектов-структур сайтов
    :return: None
    """
    list_of_sites = []
    for site in list_of_obj:
        product = input('Введите название продукта для нового сайта: ')
        list_of_sites.append(site.create_new_site(product))
        for website in list_of_sites:
            text = website["html"]["head"]["title"].split()
            title = text[1]
            print(f'Сайт для {title}: ')
            print('site =', json.dumps(website, ensure_ascii=False, indent=8), '\n')

def main():

    site_template = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iphone',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }

    count_sites = num_validator('Сколько сайтов: ', 1)
    list_of_obj = [Site(site_template) for _ in range(count_sites)]
    nice_print(list_of_obj)

if __name__ == '__main__':
    main()