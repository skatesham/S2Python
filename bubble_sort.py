import unittest


def bubble_sort(seq):
    '''
    Função tem como entrada uma lista de numeros e retorna
    a mesma lista organizada, faz iteração de n-1 em n-1 vezes.
    Função tem tempo em O(n**2) e espaço O(1)
    :param seq: lista como numeros
    :return seq: retorna mesma lista organizada por valor
    '''

    if len(seq) <= 1:
        return seq
    flag = False
    for i_corrente in range(len(seq)-1):
        for i in range(len(seq)-1):
            if seq[i] > seq[i+1]:
                seq[i],seq[i+1] = seq[i+1], seq[i];
                flag = True
        if (flag == False):
             break
        flag = False
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria2(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
