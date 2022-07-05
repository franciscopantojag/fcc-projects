from functools import reduce
from math import ceil


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

        last_line = f'Total: {self.get_balance()}'
        rows.append(last_line)
        return '\n'.join(rows)

    def deposit(self, amount: 'int | float', description: str = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        return sum(x.get('amount') or 0 for x in self.ledger)

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

    def get_spent(self) -> 'int | float':
        return sum(
            operation['amount'] * -1 for operation in self.ledger if operation['amount'] < 0)
