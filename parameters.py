import numpy as np

class parameters:
    '''
    classe de parâmetros para a otimização da carteira
    '''
    def __init__(self):
        # Matriz de correlação
        self.corr = np.array([[1, 0.18, .01, .76, -.06], [.18, 1, -.01, .08, -.05], [.01, -.01, 1, -.09, -.3], 
                        [.76, .08, -.09, 1, 0], [-.06, -.05, -.3, 0, 1]])

        #retornos dos ativos
        self.returns = np.array([.071, .059, .1959, .2972, .4185])

        #riscos dos ativos
        self.risks = np.array([.0275, .0025, .1255, .1985, .1456])

        # distribuição da carteira inicial
        self.x = [0, .66, 0, .33, 0]

        # limite minimo da carteira de ativos de baixo risco
        self.bb=.4

        # index dos ativos de baixo risco
        self.xb = [1]

        # limite máximo da composição de cada ativo na carteira
        self.b = (0, .5)
        self.bounds = [self.b]*5