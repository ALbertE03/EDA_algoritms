class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                # Si es el final de la palabra, marcamos como no final
                if not node.is_end_of_word:
                    return False  # La palabra no existe en el trie
                node.is_end_of_word = False
                # Si el nodo no tiene hijos, se puede eliminar
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False  # La palabra no existe en el trie
            # Llamada recursiva para el siguiente carácter
            should_delete_current_node = _delete(node.children[char], word, depth + 1)
            if should_delete_current_node:
                # Eliminar el nodo hijo si no es necesario
                del node.children[char]
                # Si el nodo actual no tiene hijos y no es el final de otra palabra, se puede eliminar
                return len(node.children) == 0 and not node.is_end_of_word
            return False

        _delete(self.root, word, 0)


trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # Devuelve True
print(trie.search("app"))  # Devuelve True

trie.delete("apple")
print(trie.search("apple"))  # Devuelve False
print(trie.search("app"))  # Devuelve True (porque "app" sigue existiendo)

trie.delete("app")
print(trie.search("app"))  # Devuelve False
