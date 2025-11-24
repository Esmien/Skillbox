def check_filename(filename: str) -> bool:
    """Проверяет имя файла на валидность"""
    if not filename:
        return False
    broken_syms = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
    valid_extensions = ('.txt', '.docx')
    if not filename.endswith(valid_extensions):
        return False
    if filename.startswith(broken_syms):
        return False
    return True

# def find_longest_filename(data):
#     max_length = 0
#     if not data:
#         return 0
#     for row in data:
#         filenames = row[1]
#         current_length = max(len(f) for f in filenames)
#         if current_length > max_length:
#             max_length = current_length
#     return max_length

def find_valid_files(filenames_list: str) -> list[str]:
    """Проверяет имена файлов на валидность"""
    if not filenames_list:
        return []
    files = filenames_list.split()
    valid_files = [f for f in files if check_filename(f)]
    if len(valid_files) == 3:
        return valid_files
    return []

def check_ip(ip_string: str) -> bool:
    """Проверяет IP на соответствие формату"""
    sector = ip_string.split('.')
    if len(sector) != 4:
        return False
    else:
        for part in sector:
            try:
                if not 0 <= int(part) <= 255:
                    return False
            except ValueError:
                return False
    return True

def check_right(data: list) -> list:
    """Проверяет данные в структуре на полное соответствие критериям"""
    completed_data = []
    for row in data:
        ip = row[0]
        filenames = row[1]
        # curr_len = max(len(f) for f in filenames) - не понадобилось
        if (find_valid_files(filenames[0]) and
                check_ip(ip)):
            completed_data.append(row)
    return completed_data
def main():
    data = [
        ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
        ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
        ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
        ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
        ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
        ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
        ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
    ]
    result = check_right(data)
    print('[')
    for row in result:
        print("   ",row)
    print(']')

if __name__ == '__main__':
    main()