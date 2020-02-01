from utils import constraint1, constraint2, objective
from parameters import parameters
from scipy.optimize import minimize

def main():
    P = parameters()

    # limite máximo da composição de cada ativo na carteira
    bounds = P.bounds

    # distribuição da carteira inicial
    x = P.x

    con1 = {'type':'eq', 'fun':constraint1}
    con2 = {'type':'ineq', 'fun':constraint2}
    cons = [con1, con2]

    results = minimize(objective, x, bounds = bounds, constraints=cons)
    print(results.x)

if __name__ == "__main__":
    main()