def main_function(input: str):
    if not isinstance(input, str):
        raise Exception('Invalid input')
    all_digits = list(input)
    possible_numbers = []
    for index, digit in enumerate(all_digits):
        if len(all_digits) - 2 < index:
            break
        possible_numbers.append(int(f'{digit}{all_digits[index + 1]}'))
    max_even_number = max(list(filter(lambda x: x % 2 == 0, possible_numbers)))
    max_odd_number = max(list(filter(lambda x: x % 2 != 0, possible_numbers)))
    return [max_even_number, max_odd_number]


print(main_function('726437856347856837657834'))
