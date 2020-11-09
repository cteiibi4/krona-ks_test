# 10.   Проверить сбалансированы ли скобки в строке.
"""

    isBalanced("{ [ ] } )")  --> False
    isBalanced("{ [ } ]")    --> False
    isBalanced("{ [ ] [] {} }")    --> True

eremeev-dy@crona.ru
"""

CHECK_LIST = ['{ [ ] } )', '{ [ } ]', '{ [ ] [] {} }']


def is_balansed(str_balanced):
    balance_list = []
    for i in str_balanced:
        if i == '{' or i == '[' or i == '(':
            balance_list.append(i)
        elif i == '}':
            if len(balance_list) > 0 and balance_list[-1] == '{':
                balance_list.pop()
            else:
                return False
        elif i == ']':
            if len(balance_list) > 0 and balance_list[-1] == '[':
                balance_list.pop()
            else:
                return False
        elif i == ')':
            if len(balance_list) > 0 and balance_list[-1] == '(':
                balance_list.pop()
            else:
                return False
    if len(balance_list) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in CHECK_LIST:
        print(is_balansed(i))


