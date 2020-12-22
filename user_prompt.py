import sys


# check candidate for correctness
def try_parse_arg(candidate):
    try:
        result = float(candidate)
        return True, result
    except ValueError:
        return False, 0.0


def prompt_user_agreement(text):
    success = False

    while not success:
        user_prompt = input(text)

        if user_prompt == 'Y':
            return True

        if user_prompt == 'n':
            return False


# input by args
def try_process_args(logger):
    args = sys.argv

    if len(args) == 4:
        data = [try_parse_arg(args[1]), try_parse_arg(args[2]), try_parse_arg(args[3])]

        if data[0][0] and data[1][0] and data[2][0]:
            logger.write('Script args parsed correctly...')
            return [data[0][1], data[1][1], data[2][1]]
        else:
            logger.write('Script args not provided correctly...')
            return []
    else:
        return []


# input by prompt
def infinite_prompt(text):
    success = False

    while not success:
        user_prompt = input(text)
        parsing_result = try_parse_arg(user_prompt)
        success = parsing_result[0]

        if success:
            return parsing_result[1]


# input by prompt
def prompt_manual_input():
    x0 = infinite_prompt("Enter X0 : ")

    x1 = infinite_prompt("Enter X1 : ")

    delta_x = infinite_prompt("Enter delta_x : ")

    return [x0, x1, delta_x]
