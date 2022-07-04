def main_function(input: str):
    arr = list(input)
    arr.sort(reverse=True)
    return ''.join(arr)


print(main_function('674391'))
