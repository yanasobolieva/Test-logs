import os


def find_all_files_in_folder(raw_path):
    log_files_list = []
    for log_file in os.scandir(raw_path):
        log_files_list.append(log_file.name)
    return log_files_list


def generate_full_path(raw_path, log_files_list):
    full_logs_path_list = []
    for file_name in log_files_list:
        full_logs_path_list.append(os.path.join(raw_path, file_name))
    return full_logs_path_list


def test_log_files(raw_path, full_logs_path_list):
    for log_file in full_logs_path_list:
        log_records_list = []
        for line in open(log_file, 'rt', encoding='utf-8').readlines():
            log_records_list.append(line)
        if len(log_records_list) > len(set(log_records_list)):
            for record in set(log_records_list):
                match_counter = log_records_list.count(record)
                if match_counter >= 2:
                    f2 = open(os.path.join(raw_path, '{}.duplicates.txt'.format(log_file)), 'a', encoding='utf-8')
                    f2.write(record + '\n')
                    # f2.write('The line index is ' + str(log_records_list.index(record)) + '\n')
                    f2.close()
            print('The file contains not unique lines')
        else:
            print('The file contains only unique lines')


input_path = "D:\Logs"
test_log_files(input_path, generate_full_path(input_path, find_all_files_in_folder(input_path)))
