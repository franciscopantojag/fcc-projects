from helpers import get_str_char_or_space, build_category_data
from classes import Category


def create_spend_chart(categories: 'list[Category]'):
    total_spent = sum(x.get_spent() for x in categories)

    categories_data = [build_category_data(x, total_spent) for x in categories]
    rows_num = 12 + max(len(x.name) for x in categories)
    rows = ['Percentage spent by category']
    dashes = ((3 * len(categories_data)) + 1) * '-'
    left_spaces_words = 5 * ' '

    for i in range(rows_num):
        n = 100 - i * 10

        if n == -10:
            rows.append(f'    {dashes}')
        else:
            row_bullets = ''
            row_word = ''
            letter_index = i - 12

            for category_data in categories_data:
                category_name = category_data.name
                row_word += f'{get_str_char_or_space(category_name, letter_index)}  '
                amount = category_data.percent
                plus = 'o  '
                if n > amount:
                    plus = '   '
                row_bullets += plus

            if n >= 0:
                str_n = str(n)
                if n < 100 and n >= 10:
                    str_n = f' {str_n}'
                elif n < 10:
                    str_n = f'  {str_n}'
                rows.append(f'{str_n}| {row_bullets}')
            else:
                rows.append(f'{left_spaces_words}{row_word}')
    return '\n'.join(rows)


test = Category('Food')
test.deposit(900)
test.withdraw(105.55)

test_2 = Category('Entertainment')
test_2.deposit(900)
test_2.withdraw(33.40)

test_3 = Category('Business')
test_3.deposit(900)
test_3.withdraw(10.99)

print(create_spend_chart([test_3, test, test_2]))
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
