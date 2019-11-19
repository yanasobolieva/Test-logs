import os


def prettify_path(raw_path):
    return r'{}'.format(raw_path)


def find_all_files_in_folder(logs_dir):
    log_files = []
    for log_file in os.scandir(logs_dir):
        log_files.append(log_file.name)
    return log_files


def generate_full_path(parent_path, files_names):
    full_logs_path = []
    for file_name in files_names:
        full_logs_path.append(os.path.join(parent_path, file_name))
    return full_logs_path


def test_log_files(input_path):
    updated_input_path = prettify_path(input_path)
    all_logs = find_all_files_in_folder(updated_input_path)
    full_logs_path = generate_full_path(input_path, all_logs)
    for file in full_logs_path:
        log_records_set = set()
        log_records_list = []
        for line in open(file, 'rt', encoding='utf-8').readlines():
            log_records_set.add(line)
            log_records_list.append(line)
        if len(log_records_list) > len(log_records_set):
            for record in log_records_set:
                match_counter = log_records_list.count(record)
                if match_counter >= 2:
                    f2 = open(os.path.join(input_path, '{}.duplicates.txt'.format(file)), 'a', encoding='utf-8')
                    f2.write(record + '\n')
                    # f2.write('The line index is ' + str(log_records_list.index(record)) + '\n')
                    f2.close()
            print('The file contains not unique lines')
        else:
            print('The file contains only unique lines')


print(test_log_files("D:\Logs"))
