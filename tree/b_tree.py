class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grado mínimo
        self.leaf = leaf
        self.keys = []
        self.children = []

    def __str__(self):
        return f"Keys: {self.keys}, Leaf: {self.leaf}, Children: {len(self.children)}"


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(self.t, False)
            self.root = temp
            temp.children.insert(0, root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t : (2 * t) - 1]
        y.keys = y.keys[0 : t - 1]
        if not y.leaf:
            z.children = y.children[t : 2 * t]
            y.children = y.children[0:t]

    def search(self, k, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return x
        if x.leaf:
            return None
        return self.search(k, x.children[i])

    def delete(self, k):
        self._delete(self.root, k)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, x, k):
        t = self.t
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i] == k:
                x.keys.pop(i)
            return
        if i < len(x.keys) and x.keys[i] == k:
            self._delete_internal_node(x, k, i)
        elif len(x.children[i].keys) >= t:
            self._delete(x.children[i], k)
        else:
            if i != 0 and len(x.children[i - 1].keys) >= t:
                self._borrow_from_prev(x, i)
            elif i != len(x.children) - 1 and len(x.children[i + 1].keys) >= t:
                self._borrow_from_next(x, i)
            else:
                if i != len(x.children) - 1:
                    self._merge(x, i)
                else:
                    self._merge(x, i - 1)
            self._delete(x.children[i], k)

    def _delete_internal_node(self, x, k, i):
        t = self.t
        if x.leaf:
            if x.keys[i] == k:
                x.keys.pop(i)
            return
        if len(x.children[i].keys) >= t:
            x.keys[i] = self._get_predecessor(x.children[i])
            self._delete(x.children[i], x.keys[i])
        elif len(x.children[i + 1].keys) >= t:
            x.keys[i] = self._get_successor(x.children[i + 1])
            self._delete(x.children[i + 1], x.keys[i])
        else:
            self._merge(x, i)
            self._delete(x.children[i], k)

    def _borrow_from_prev(self, x, i):
        child = x.children[i]
        sibling = x.children[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def _borrow_from_next(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def _merge(self, x, i):
        t = self.t
        child = x.children[i]
        sibling = x.children[i + 1]
        child.keys.append(x.keys.pop(i))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        x.children.pop(i + 1)

    def _get_predecessor(self, x):
        while not x.leaf:
            x = x.children[-1]
        return x.keys[-1]

    def _get_successor(self, x):
        while not x.leaf:
            x = x.children[0]
        return x.keys[0]

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, x):
        for i in range(len(x.keys)):
            if not x.leaf:
                self._traverse(x.children[i])
            print(x.keys[i], end=" ")
        if not x.leaf:
            self._traverse(x.children[-1])

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, x, level):
        print(f"Level {level}: {x}")
        if not x.leaf:
            for child in x.children:
                self._print_tree(child, level + 1)


bt = BTree(3)  # Crear un árbol B con grado mínimo t=3
keys = [10, 20, 5, 6, 12, 30, 7, 17]

for key in keys:
    bt.insert(key)

print("Árbol B después de inserciones:")
bt.print_tree()

bt.delete(6)
print("\nÁrbol B después de eliminar 6:")
bt.print_tree()

print("\nRecorrido en orden:")
bt.traverse()

# Uso: El Árbol B se utiliza en bases de datos y sistemas de archivos para
# manejar grandes volúmenes de datos. Es ideal para trabajar con discos o
# memoria secundaria, ya que minimiza el número de accesos a disco.
