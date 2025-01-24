class Node:
    def __init__(self, info, priority) -> None:
        self.info = info
        self.priority = priority

    def __repr__(self):
        return f"({self.info}, {self.priority})"


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return not self.elements

    def put(self, info, priority) -> None:

        new_node = Node(info, priority)

        for index in range(len(self.elements)):
            if self.elements[index].priority > priority:
                self.elements.insert(index, new_node)
                return
        self.elements.append(new_node)

    def get(self):
        if self.is_empty():
            return
        return self.elements.pop(0).info

    def __repr__(self) -> str:
        return f"{self.elements}"
