def main_function(input: str):
    if not isinstance(input, str):
        raise Exception('Invalid input')
    all_digits = list(input)
    possible_numbers = []
    for index, digit in enumerate(all_digits):
        if len(all_digits) - 2 < index:
            break
        possible_numbers.append(int(f'{digit}{all_digits[index + 1]}'))
    # TODO: finish exercise
    return possible_numbers


print(main_function('3434534534'))
