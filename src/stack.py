class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)
        if self.top is not None:
            node.next_node = self.top
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        last_plate = self.top
        self.top = last_plate.next_node
        return last_plate.data

    def __str__(self):
        res = ''
        cur = self.top
        while cur:
            res += cur.data
            res += '-->'
            cur = cur.next_node
        res += 'None'
        return res

# stack_of_plates = Stack()
# stack_of_plates.push('plate1')
# stack_of_plates.push('plate2')
# stack_of_plates.push('plate3')
# print(stack_of_plates.top.data)
# print(stack_of_plates)
# stack_of_plates.pop()
# stack_of_plates.pop()
# stack_of_plates.pop()
# print(stack_of_plates.top.data)
