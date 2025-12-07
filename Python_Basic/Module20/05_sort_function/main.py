def tpl_sort(tpl: tuple) -> tuple:
    for item in tpl:
        if not isinstance(item, int):
            return tpl
    sorted_lst = tuple(sorted(tpl))
    return sorted_lst