import unittest
import random

def _quick_recursivo(seq, inicio, final):
    if inicio >= final:
        return seq

    ram = random.randint(inicio, final)
    seq[-1], seq[ram] = seq[ram], seq[-1]

    indice_pivot = final
    pivot = seq[-1]
    i_esquerdo = inicio
    i_direito = indice_pivot - 1

    while i_esquerdo != i_direito:
        if (seq[i_esquerdo] <= pivot):
            i_esquerdo += 1
        else:
            while i_esquerdo != i_direito:
                if (seq[i_direito] >= pivot):
                    i_direito -= 1
                else:
                    seq[i_esquerdo], seq[i_direito] = seq[i_direito], seq[i_esquerdo]
                    break

    if pivot >= seq[i_direito]:
        return _quick_recursivo(seq, inicio, indice_pivot-1) + [seq[indice_pivot]]
    elif pivot < seq[inicio]:
        return [seq[indice_pivot]] + _quick_recursivo(seq,inicio, indice_pivot-1)
    return _quick_recursivo(seq, inicio, i_esquerdo-1) + [seq[indice_pivot]] + _quick_recursivo(seq, i_esquerdo, indice_pivot-1)

def quick_sort(seq):
    return _quick_recursivo(seq, 0, len(seq) - 1)



class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_com_elementos_repetidos(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0, 9, 9]))

    def teste_lista_so_com_elementos_repetidos(self):
        self.assertListEqual([9, 9, 9], quick_sort([9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
