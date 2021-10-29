"""
Netology. Stack. Task 1

    1. Необходимо реализовать класс Stack со следующими методами:

    isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    size - возвращает количество элементов в стеке.

    2. Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. Сбалансированность
    скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,
    и пары скобок правильно вложены друг в друга.

    28.10.21
"""

start_stack = []


class Stack:
    """
    Класс воссоздает работу функций согласно заданию
    """

    def __init__(self, my_stack_: list):
        self.my_stack = my_stack_

    def isEmpty(self) -> bool:
        return True if not self.size() else False

    def push(self, i: str):
        self.my_stack.append(i)

    def pop(self):
        if self.isEmpty():
            return 'Стек пуст'
        else:
            last = self.my_stack[-1]
            del self.my_stack[-1]
            return last

    def peek(self):
        if self.isEmpty():
            return 'Стек пуст'
        else:
            return self.my_stack[-1]

    def size(self):
        return len(self.my_stack)


def chack_balance(list_in: list):
    """
        Функци принимает набор скобок. Проверяет на наличие посторонних символов,
    сбалансированность скобок и выдает результат
    :param list_in:
    :return:
    """
    dct = {'(': ')', '{': '}', '[': ']'}
    simbols_list = ['(', ')', '[', ']', '{', '}']  # для проверки посторонних символов
    temp = []
    my_stack = Stack(temp)
    for i in list_in:
        if i in simbols_list:
            if my_stack.isEmpty():
                my_stack.push(i)
            else:
                if dct.get(my_stack.peek()) == i:
                    my_stack.pop()
                else:
                    my_stack.push(i)
        else:
            print('Символ не является скобкой')

    if my_stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


def main():
    #  Проверки
    print(chack_balance('()'))
    print(chack_balance('(((([{}]))))'))
    print(chack_balance('[([])((([[[]]])))]{()}'))
    print(chack_balance('{{[()]}}'))
    print()
    print(chack_balance('}{}'))
    print(chack_balance('{{[(])]}}'))
    print(chack_balance('[[{())}]'))


if __name__ == '__main__':
    main()






