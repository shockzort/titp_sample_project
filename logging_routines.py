import os
from datetime import datetime

datetime_string = None


def make_log_path(appendix):
    global datetime_string

    if datetime_string is None:
        datetime_string = datetime.now().strftime("%b-%d-%Y %H-%M-%S")

    log_full_path = os.getcwd() + '\\log\\' + appendix + '\\'

    if not os.path.exists(log_full_path):
        os.makedirs(log_full_path)

    return log_full_path


def make_log_file(file_name, logging_column_names):
    log_full_path = make_log_path('csv')

    full_log_name = log_full_path + file_name + ' ' + str(datetime_string) + '.csv'

    log_file = open(full_log_name, "w")

    if os.stat(full_log_name).st_size == 0:
        log_file.write('Time,' + logging_column_names + '\n')

    return log_file, str(datetime_string)


def write_to_log_file(file_handle, logging_data):
    now = datetime.now().strftime("%H-%M-%S.%f")

    data_string = str(now)

    for i in range(len(logging_data)):
        data_string += ','
        data_string += str(logging_data[i])

    data_string += '\n'

    file_handle.write(data_string)
    file_handle.flush()


def finalize_log_file(file_handle, logging_caption, logging_data):
    data_string = logging_caption

    for i in range(len(logging_data)):
        data_string += ','
        data_string += str(logging_data[i])

    data_string += '\n'

    file_handle.write(data_string)
    file_handle.flush()
