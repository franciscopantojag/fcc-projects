from re import search


def arithmetic_arranger(problems: 'list[str]', calculate_result=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first_row = ''
    second_row = ''
    dashes_row = ''
    result_row = ''
    ONLY_DIGIT_PATTERN = r'^\d+$'

    for index, problem in enumerate(problems):
        operator = '+'
        operands = problem.split(' + ')

        if not len(operands) == 2:
            operands = problem.split(' - ')
            operator = '-'
        if not len(operands) == 2:
            return "Error: Operator must be '+' or '-'."

        for operand in operands:
            operand_len = len(operand)
            if not search(ONLY_DIGIT_PATTERN, operand):
                return 'Error: Numbers must only contain digits.'
            if operand_len > 4:
                return 'Error: Numbers cannot be more than four digits.'

        result = sum(map(lambda x: int(x), operands))
        if operator == '-':
            result = int(operands[0]) - int(operands[1])

        len_result = len(str(result))
        len_first_operand = len(operands[0])
        len_last_operand = len(operands[1])

        len_operands_raw = max(len_first_operand, len_last_operand)
        len_with_result_raw = max(len_operands_raw, len_result)
        len_total_raw = len_with_result_raw if calculate_result else len_operands_raw

        n_spaces = len_total_raw - len_last_operand
        if (n_spaces == 0):
            n_spaces = n_spaces + 1
        poss_last_operand_len = 1 + n_spaces + len_last_operand
        if abs(poss_last_operand_len - len_operands_raw) < 2:
            n_spaces = n_spaces + 1

        test_spaces = ' ' * n_spaces
        last_operand = f'{operator}{test_spaces}{operands[1]}'
        len_last_operand = len(last_operand)

        first_operand_spaces = ' ' * abs(len_last_operand - len_first_operand)
        first_operand_formatted = f'{first_operand_spaces}{operands[0]}'

        result_spaces = ' ' * abs(len_last_operand - len_result)
        result_formatted = f'{result_spaces}{result}'

        dashes = '-' * len_last_operand

        formatted_spaces = ' ' * 4

        if index == 0:
            first_row += first_operand_formatted
            second_row += last_operand
            dashes_row += dashes
            result_row += result_formatted
        else:
            first_row += formatted_spaces + first_operand_formatted
            second_row += formatted_spaces + last_operand
            dashes_row += formatted_spaces + dashes
            result_row += formatted_spaces + result_formatted

    if calculate_result:
        return '\n'.join([first_row, second_row, dashes_row, result_row])

    return '\n'.join([first_row, second_row, dashes_row])


print(arithmetic_arranger(
    ['32 - 698', '9999 - 1', '9999 + 9999', '123 + 49', '988 + 40'], True))
