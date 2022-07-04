from math import ceil


def get_str_char_or_space(input: str, index):
    try:
        return input[index]
    except:
        return ' '


class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []

    def __str__(self) -> str:
        LEN_LINE = 30
        chars_number = LEN_LINE - len(self.name)
        first_line = None
        if chars_number < 0:
            chars_number = 0
            first_line = 30 * '*'
        else:
            chars_middle_len = chars_number / 2
            chars_left = int(chars_middle_len) * '*'
            chars_right = ceil(chars_middle_len) * '*'
            first_line = f'{chars_left}{self.name}{chars_right}'
        rows = [first_line]
        last_line = f'Total: {self.get_balance()}'
        for deposit in self.ledger:
            description = deposit['description']
            amount = deposit['amount']
            len_description = len(description)
            spaces_description = ''
            if len_description > 23:
                description = description[0:23]
            else:
                spaces_description = (23 - len_description) * ' '
                description = f'{description}{spaces_description}'

            amount_str = f'{amount:.2f}'
            len_amount = len(amount_str)
            spaces_amount = ''
            if len_amount > 7:
                amount_str = amount_str[0:7]
            else:
                spaces_amount = (7 - len_amount) * ' '
                amount_str = f'{spaces_amount}{amount_str}'

            rows.append(f'{description}{amount_str}')
        rows.append(last_line)
        return '\n'.join(rows)

    def deposit(self, amount: 'int | float', description: str = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        return sum(map(lambda x: x.get('amount') or 0, self.ledger))

    def withdraw(self, amount: 'int | float', description: str = ''):
        withdraw_result = self.check_funds(amount)
        if not withdraw_result:
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def transfer(self,  amount: 'int | float', destination: 'Category'):
        withdraw_result = self.withdraw(
            amount, f'Transfer to {destination.name}')
        if not withdraw_result:
            return False
        destination.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount: 'int|float'):
        balance = self.get_balance()
        if not balance >= amount:
            return False
        return True

    def get_spent(self):
        spent = 0
        for operation in self.ledger:
            amount = operation['amount']
            if amount < 0:
                spent += (amount * -1)
        return spent


def create_spend_chart(categories: 'list[Category]'):
    categories_data = []
    total_spent = sum(map(lambda x: x.get_spent(), categories))
    rows_num = 12 + max(map(lambda x: len(x.name), categories))
    rows = ['Percentage spent by category']
    for category in categories:
        category_percent = int(
            ((category.get_spent() / total_spent) * 100) / 10) * 10
        category_data = {'name': category.name, 'percent': category_percent}
        categories_data.append(category_data)

    dashes = ((3 * len(categories_data)) + 1) * '-'
    left_spaces_words = 5 * ' '

    for i in range(rows_num):
        n = 100 - i * 10

        if n == -10:
            rows.append(f'    {dashes}')

        elif n >= 0:
            row_bullets = ''
            row_word = ''
            letter_index = i - 12

            for category_data in categories_data:
                amount = category_data.get('percent')
                plus = 'o  '
                if n > amount:
                    plus = '   '
                row_bullets += plus

            str_n = str(n)
            if n < 100 and n >= 10:
                str_n = f' {str_n}'
            elif n < 10:
                str_n = f'  {str_n}'
            rows.append(f'{str_n}| {row_bullets}')
        else:
            row_word = ''
            letter_index = i - 12
            for index, category_data in enumerate(categories_data):
                category_name = category_data.get('name')
                row_word += f'{get_str_char_or_space(category_name, letter_index)}  '
            rows.append(f'{left_spaces_words}{row_word}')
    print(rows)
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
column_one = '0\n1\n'
column_two = '4\n6\n'
