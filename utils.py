import numpy as np
from itertools import combinations
from parameters import parameters

P = parameters()
# Matriz de correlação
corr = P.corr

#retornos dos ativos
returns = P.returns

#riscos dos ativos
risks = P.risks

# limite minimo da carteira de ativos de baixo risco
bb = P.bb

# index dos ativos de baixo risco
xb = P.xb

def objective(x):
    '''
    x = composição ótima de cada ativo na carteira
    r = retorno de cada ativo
    s =  risco da carteira
    '''
    total_risks =  total_risk(risks, corr, x)
    return total_risks/np.sum(x*returns)

def corr_term(risks, corr, x):
    '''
    corr = matriz de correlação entre os ativos [n x n]
    '''
    comb = combinations(np.arange(len(corr)), 2)
    total_term = 0
    for combination in list(comb):
        corr_ij = corr[combination[0], combination[1]]
        xi = x[combination[0]]
        xj = x[combination[1]]
        si = risks[combination[0]]
        sj = risks[combination[1]]
        i_term = 2*xi*xj*corr_ij*si*sj
        total_term+=i_term
    return total_term

def total_risk(risks, corr, x):
    singular_risks = np.sum((risks*x)**2)
    total_corr_term = corr_term(risks, corr, x)
    return np.sqrt(singular_risks+total_corr_term)

def constraint1(x):
    '''
    total da carteira = 100%
    limite de eq
    '''
    return np.sum(x)-1

def constraint2(x, xb=xb, bb=bb):
    '''
    limita a composição da carteira de alto risco
    xa = ativos de baixo risco
    ba = limite da composição da carteira de ativos de baixo risco
    limite de maior ou igual
    '''
    total = 0
    for i in xb:
        total+=x[i]
    return total-bb
