# Sample project for user input processing and computation
#
# Developed by Bondarenko Vladimir Aleksandrovich / user ID 24
#
# Developed in PyCharm 2020.2.3 (Community Edition)
# Build #PC-202.7660.27, built on October 6, 2020
# Runtime version: 11.0.8+10-b944.34 amd64
# VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
# Windows 10 10.0
# GC: ParNew, ConcurrentMarkSweep
#
#
# System Model                      GE73VR 7RF
# System Type	                    x64-based PC
# Processor	Intel(R)                Core(TM) i7-7700HQ CPU @ 2.80GHz, 2801 Mhz, 4 Core(s), 8 Logical Processor(s)
# Installed Physical Memory (RAM)	16.0 GB
# OS Name	                        Microsoft Windows 10 Enterprise
# OS version	                    10.0.19041 Build 19041
#
#
# Tested on Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32

import math

import logging_routines as log_man
import user_prompt as up

user_number = 24
max_iterations = 10000
min_step = 0.00001

numeric_output_format = "{:0.5f}"
row_output_format = "{: <12} {: <12} {: <30}"
row_output_format_v2 = "{: ^10} {: ^10} {: ^30}"
result_file_name = "result_table_log"

print_in_place = True
save_result = True

# Global csv logger
log_file = None


# compute user function
def compute_function(x, number):
    try:
        arg_1 = math.log((1.0 - number) / math.sin(x + number))
    except ValueError:
        return "F_1 error"
    except ZeroDivisionError:
        return "F_1 error"

    try:
        arg_2 = math.fabs(1.0 / (math.tan(x) * number))
    except ValueError:
        return "F_2 error"
    except ZeroDivisionError:
        return "F_2 error"

    result = max(arg_1, arg_2)
    result_string = numeric_output_format.format(result)

    return result_string


def compute_iterations(start, end, step):
    try:
        iterations = (end - start) / step
        return iterations
    except ZeroDivisionError:
        return 0


# process computetion step
def compute_step(iteration_id, x):
    compute_result = compute_function(x, user_number)

    result_row = (iteration_id, numeric_output_format.format(x), compute_result)

    if print_in_place:
        print(row_output_format.format(*result_row))

    # optional result saving
    if save_result:
        log_man.write_to_log_file(log_file, result_row)

    return result_row


# input sata sanity check routine
def check_data_for_sanity(start, end, step):
    iterations = compute_iterations(start, end, step)

    # check if step is too small
    if 0.0 < abs(step) < min_step:
        prompt_text = "Step is too small. Are you sure you want to proceed? [Y/n] "

        if not up.prompt_user_agreement(prompt_text):
            log_file.write('\nUser requested exit. Exiting...')
            return False

    # check for too much iterations and prompt user
    if iterations > max_iterations:
        prompt_text = "Cycle iterations exceed " + str(max_iterations) + ". Are you sure you want to proceed? [Y/n] "

        if not up.prompt_user_agreement(prompt_text):
            log_file.write('\nUser requested exit. Exiting...')
            return False

    # check for valid iterations
    if iterations <= 0:
        print('\nZero or infinite iterations. Cannot proceed')
        log_file.write('\nZero or iterations iterations. Exiting...')
        return False

    return True


# process user data
def process_data(input_data):
    start = input_data[0]
    end = input_data[1]
    step = input_data[2]

    if not check_data_for_sanity(start, end, step):
        return []

    result = []

    iteration_id = 1
    x = start

    # multiplication [x = start + step * iteration_id] is more precise than addition [x = x + step]
    # the error significantly increases if iteration number is high!
    if x <= end:
        while x <= end:
            result_row = compute_step(iteration_id, x)
            result.append(result_row)

            x = start + step * iteration_id
            iteration_id = iteration_id + 1
    else:
        while x >= end:
            result_row = compute_step(iteration_id, x)
            result.append(result_row)
            x = start + step * iteration_id
            iteration_id = iteration_id + 1

    return result


# Main script
if __name__ == '__main__':
    log_file, _ = log_man.make_log_file(result_file_name, 'Iteration, X, Result')
    args_list = up.try_process_args(log_file)

    processing_result = []

    # compute function
    if len(args_list) == 3:
        processing_result = process_data(args_list)
    else:
        args_list = up.prompt_manual_input()
        processing_result = process_data(args_list)

    # optional result output
    if not print_in_place:
        for row in processing_result:
            print(row_output_format.format(*row))

    log_file.close()
