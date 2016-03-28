import unittest

def max_min(x):
    '''

    :param seq: uma sequencia
    :return: (min, max)

    Entra com uma lista X, ele retorna o Maior numero e o Menor; Tempo em O(n).
    '''
    def min_max_calculator(maior, menor, lista, count):
        if(count == 0): # condiçãoo de parada
            return lista[menor], lista[maior] #Finalizaçao da funo
        if ((lista[maior]) < (lista[count])): #trabalhando com o indice da lista.
            maior = count   #guarda o maior valor de indice
        if ((lista[menor]) > (lista[count])):#trabalhando com o indice da lista.
            menor = count #guarda o menor valor de indice
        count-=1
        return min_max_calculator(maior, menor, lista, count) #tentando repercutir

    try:            #previnindo erros
        if (type(x)is list):    #Previnindo entradas na lista
            count = (len(x)-1)  #iniciando um contador
            retorno = min_max_calculator(0, 0, x, count) #Calculando
        else:
            return '''COD 1 : Insira uma Lista! ''' #print erros
    except IndexError:
        return (None, None)
    else:
        return retorno


class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), max_min([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), max_min([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), max_min(list(range(501))))


if __name__ == '__main__':
     unittest.main()
