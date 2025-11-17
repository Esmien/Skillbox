#Нихуя не работает, доделать!!!!
def check_filename(filename):
    if not filename:
        return False
    broken_syms = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
    valid_extensions = ('.txt', '.docx')
    if not filename.endswith(valid_extensions):
        return False
    if filename.startswith(broken_syms):
        return False
    return True
def find_longest_filename(filename):
    if not filename:
        return 0
    return max(len(f) for f in filename)

def find_valid_files(filenames_list):
    if not filenames_list:
        return []
    files = filenames_list[0].split()
    valid_files = [f for f in files if check_filename(f)]
    return valid_files

def check_ip(ip_string):
    sector = ip_string.split('.')
    if len(sector) != 4:
        return False
    else:
        for part in sector:
            try:
                if int(part) < 0 or int(part) > 255:
                    return False
            except ValueError:
                return False
    return True

def check_right(data):
    completed_data = []
    max_length = 0
    for row in data:
        if check_ip(row[0]):
            valid_files = find_valid_files(row[1])
            if valid_files:
                current_max = find_longest_filename(valid_files)
                max_length = max(max_length, current_max)
    for row in data:
        if check_ip(row[0]):
            valid_files = find_valid_files(row[1])
            if valid_files and find_longest_filename(valid_files) == max_length:
                completed_data.append([row[0], [' '.join(valid_files)]])
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
    print(check_right(data))
    for row in result:
        print(row)

if __name__ == '__main__':
    main()