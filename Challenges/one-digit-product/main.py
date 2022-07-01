def find_product_digits(input: int):
    str_input = str(input)
    result = 1
    for digit in str_input:
        result = int(digit) * result
    return result


def main_function(input: int):
    if input >= 100 or input < 0:
        raise Exception('Number must me a positive integer lower than 100')
    result = find_product_digits(input)
    result_len = len(str(result))

    while result_len >= 2:
        result = find_product_digits(result)
        result_len = len(str(result))
    return result
