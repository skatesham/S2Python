class Noh(object):
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __str__(self):
        return str(self.valor)

class ListaEncadeada(object):
    def __init__(self, raiz):
        self.root = Noh(raiz)
        self.leaf = self.root
        
    def add(self, valor):
        '''
        O(1)
        '''
        novo = Noh(valor)
        self.leaf.proximo = novo
        self.leaf = novo

    def read(self):
        '''
        O(n)
        '''
        v = self.root
        while(v != None):
            print(v, end=', ')
            v = v.proximo

if __name__ == '__main__':
    l = ListaEncadeada(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.read()
        
