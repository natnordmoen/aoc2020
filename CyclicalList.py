from itertools import cycle, takewhile, dropwhile


class CyclicalList:
    def __init__(self, initial_list):
        self._initial_list = initial_list

    def __getitem__(self, item):
        if isinstance(item, slice):
            if item.stop is None:
                raise ValueError("Cannot slice without stop")
            iterable = enumerate(cycle(self._initial_list))
            if item.start:
                iterable = dropwhile(lambda x: x[0] < item.start, iterable)
            return [
                element
                for _, element in takewhile(lambda x: x[0] < item.stop, iterable)
            ]

        for index, element in enumerate(cycle(self._initial_list)):
            if index == item:
                return element

    def __iter__(self):
        return cycle(self._initial_list)