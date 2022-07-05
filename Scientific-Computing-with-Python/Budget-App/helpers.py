from classes import Category, CategoryData


def get_str_char_or_space(input: 'str', index: 'int'):
    try:
        return input[index]
    except:
        return ' '


def build_category_data(category: 'Category', total_spent: 'int|float'):
    category_percent = int(
        ((category.get_spent() / total_spent) * 100) / 10) * 10
    category_data = CategoryData(category.name, category_percent)
    return category_data
