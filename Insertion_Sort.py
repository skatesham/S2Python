import unittest

def insertion_sort(seq):
    if not seq:
        return seq
    if len(seq) == 1:
        return seq
    count = 1
    for point in range(count, len(seq)):
        i = count
        while True:
            if min(seq[i],seq[i - 1]):
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1
            if i==0:
                break
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
