from collections import deque
from typing import Any, List


class BinaryTree:
    def __init__(self) -> None:
        self.size = 100
        self.array = [None] * self.size

    def insert(self, value: Any) -> None:
        if self.array[0] is None:
            self.array[0] = value
        else:
            self._insert(value, 0)

    def _insert(self, value: Any, current_index: int) -> None:
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if left_index < self.size and self.array[left_index] is None:
            self.array[left_index] = value

        elif right_index < self.size and self.array[right_index] is None:
            self.array[right_index] = value

        else:
            self._insert(value, left_index)

    def search(self, value: Any) -> bool:
        return self._search(value, 0)

    def _search(self, value: Any, current_index: int) -> bool:
        if current_index < self.size and self.array[current_index] is not None:
            if self.array[current_index] == value:
                return True
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            return self._search(value, left_index) or self._search_recursive(
                value, right_index
            )
        return False

    def preorder(self) -> List[Any]:
        traversal_result = []
        self._preorder(0, traversal_result)
        return traversal_result

    def _preorder(self, current_index: int, traversal_result: List[Any]) -> None:

        if current_index < self.size and self.array[current_index] is not None:
            traversal_result.append(self.array[current_index])
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            self._preorder(left_index, traversal_result)
            self._preorder(right_index, traversal_result)

    def inorder(self) -> List[Any]:

        traversal_result = []
        self._inorder(0, traversal_result)
        return traversal_result

    def _inorder(self, current_index: int, traversal_result: List[Any]) -> None:
        if current_index < self.size and self.array[current_index] is not None:
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            self._inorder(left_index, traversal_result)
            traversal_result.append(self.array[current_index])
            self._inorder(right_index, traversal_result)

    def postorder(self) -> List[Any]:
        traversal_result = []
        self._postorder(0, traversal_result)
        return traversal_result

    def _postorder(self, current_index: int, traversal_result: List[Any]) -> None:

        if current_index < self.size and self.array[current_index] is not None:
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            self._postorder(left_index, traversal_result)
            self._postorder(right_index, traversal_result)
            traversal_result.append(self.array[current_index])

    def level_order_traversal(self) -> List[Any]:
        traversal_result = []
        if self.array[0] is None:
            return traversal_result
        queue = deque([0])
        while queue:
            current_index = queue.popleft()
            traversal_result.append(self.array[current_index])
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            if left_index < self.size and self.array[left_index] is not None:
                queue.append(left_index)
            if right_index < self.size and self.array[right_index] is not None:
                queue.append(right_index)
        return traversal_result

    def delete(self, value: Any) -> None:
        if self.array[0] == value:
            self.array[0] = None
        else:
            self._delete(value, 0)

    def _delete(self, value: Any, current_index: int) -> None:
        if current_index < self.size and self.array[current_index] is not None:
            if self.array[current_index] == value:
                left_index = 2 * current_index + 1
                right_index = 2 * current_index + 2
                if left_index < self.size and self.array[left_index] is not None:
                    self.array[current_index] = self.array[left_index]
                    self._delete(value, left_index)
                elif right_index < self.size and self.array[right_index] is not None:
                    self.array[current_index] = self.array[right_index]
                    self._delete(value, right_index)
                else:
                    self.array[current_index] = None
            else:
                left_index = 2 * current_index + 1
                right_index = 2 * current_index + 2
                self._delete(value, left_index)
                self._delete(value, right_index)
