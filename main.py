from stack_class import Stack




def get_answer(brackets_str, brackets_dict):
    valid_symbols = list(brackets_dict.keys()) + list(brackets_dict.values())
    for symbol in brackets_str:
        if symbol not in valid_symbols:
            return 'Неверный ввод'
    left_brackets_symbols = Stack()
    for symbol in brackets_str:
        if symbol in brackets_dict.values():
            left_brackets_symbols.push(symbol)
        else:
            if left_brackets_symbols.size() == 0:
                return 'Несбалансированно'
            if left_brackets_symbols.peek() != brackets_dict[symbol]:
                return 'Несбалансированно'
            left_brackets_symbols.pop()

    if left_brackets_symbols.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'




brackets_str = input('Ввведите строку скобок: ')
brackets_dict = {
    ']': '[',
    '}': '{',
    ')': '('
}
print(get_answer(brackets_str, brackets_dict))
