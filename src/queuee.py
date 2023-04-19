class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        human = Node(data)
        if self.tail is None:
            self.tail = human
            self.head = human
        else:
            self.tail.next_node = human
            self.tail = human

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            last_human = self.head
            self.head = last_human.next_node
            return last_human.data
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        cur = self.head
        res = ''
        while cur != self.tail:
            res += cur.data
            res += '\n'
            cur = cur.next_node
        res += cur.data
        return res


# queue = Queue()
#
# # queue.enqueue('чел 1')
# # queue.enqueue('чел 2')
# # queue.enqueue('чел 3')
# # print(queue.tail.data)
# # print(queue)


