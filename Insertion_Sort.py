import unittest


def insertion_sort(seq):
    flag = 0
    if not seq:
        return seq
    if len(seq) == 1:
        return seq
    for i in range(1, len(seq)):
        count = i
        while count == 0:
            count -= 1
            if min(seq[i], seq[count]):
                flag = 1
            elif flag == 0:
                break
            else:
                seq[i], seq[count] = seq[count], seq[i]
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
