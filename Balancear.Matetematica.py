import unittest

class Pilha():
    def __init__(self):
        self.lista = []

    def empilhar(self, valor):
        self.lista.append(valor)

    def vazia(self):
        return not bool(self.lista)

    def topo(self):
        return self.lista[-1]

    def desempilhar(self):

        if (self.lista):
            return self.lista.pop(-1)
        else:
            raise PilhaVaziaErro

def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    A função tem o resultado em O(n)
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    pilha = Pilha()
    abrir = '([{'
    fechar = ')]}'

    if not (len(expressao)) :
        return True
    if len(expressao) == 1 and (expressao in abrir or expressao in fechar):
        return False
    else:
        for caractere in expressao:
            if caractere in abrir:
                if caractere == '(':
                    pilha.empilhar(')')
                if caractere == '[':
                    pilha.empilhar(']')
                if caractere == '{':
                    pilha.empilhar('}')
            else:
                if caractere in fechar:
                    if pilha.vazia():
                        return False
                    if caractere != pilha.topo():
                        return False
        return not (pilha.vazia())






class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))