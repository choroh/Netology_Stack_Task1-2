import os
import sys

sys.path.append(os.getcwd())  # getcwd() возвращает текущую рабочую дерикторию
import main


# Тестирование класса работы со стеком Stack
class Test_Stack:

    def test_isEmpty(self):
        temp_list = []
        temp_object = main.Stack(temp_list)
        assert temp_object.isEmpty() is True

    def test_is_not_Empty(self):
        temp_list = [5]
        temp_object = main.Stack(temp_list)
        assert temp_object.isEmpty() is False

    def test_push(self):
        temp_list = []
        push_element = 'a'
        temp_object = main.Stack(temp_list)
        assert temp_object.push(push_element) is None
        assert temp_list == ['a']

    def test_pop_empty(self):
        temp_list = []
        temp_object = main.Stack(temp_list)
        assert temp_object.pop() == 'Стек пуст'

    def test_pop(self):
        temp_list = ['a', 'b']
        temp_object = main.Stack(temp_list)
        assert temp_object.pop() == 'b'
        assert temp_list == ['a']

    def test_peek_empty(self):
        temp_list = []
        temp_object = main.Stack(temp_list)
        assert temp_object.peek() == 'Стек пуст'

    def test_size(self):
        temp_list = ['a', 'b', 'c']
        temp_object = main.Stack(temp_list)
        assert temp_object.size() == 3

    # Тестирование проверки на сбалансированный список скобок
    def test_normal_empty(self):
        assert main.chack_balance('') == 'Сбалансированно'

    def test_normal1(self):
        assert main.chack_balance('()') == 'Сбалансированно'

    def test_normal2(self):
        assert main.chack_balance('[([])((([[[]]])))]{()}') == 'Сбалансированно'

    def test_wrong1(self):
        assert main.chack_balance('}{}') == 'Несбалансированно'

    def test_wrong1(self):
        assert main.chack_balance('{{[(])]}') == 'Несбалансированно'
