# 10.   Проверить сбалансированы ли скобки в строке.
"""

    isBalanced("{ [ ] } )")  --> False
    isBalanced("{ [ } ]")    --> False
    isBalanced("{ [ ] [] {} }")    --> True

eremeev-dy@crona.ru
"""

CHECK_LIST = ['{ [ ] } )', '{ [ } ]', '{ [ ] [] {} }']


def take_pair(for_pair_str):
    if for_pair_str == '}':
        return '{'
    if for_pair_str == ']':
        return '['
    if for_pair_str == ')':
        return '('


def check_pair(value, list_with_value):
    if len(list_with_value) > 0 and list_with_value[-1] == take_pair(value):
        list_with_value.pop()
    else:
        return False


def is_balansed(str_balanced):
    balance_list = []
    for i in str_balanced:
        if i == '{' or i == '[' or i == '(':
            balance_list.append(i)
        if i == '}' or i == ']' or i == ')':
            if check_pair(i, balance_list) is False:
                return False
    if len(balance_list) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in CHECK_LIST:
        print(is_balansed(i))


