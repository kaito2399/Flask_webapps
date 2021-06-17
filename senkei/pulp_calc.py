import pulp


def calc_min_bin(C, A, B, E, F):
    prob = pulp.LpProblem(sense=pulp.LpMinimize)
    n=len(C)
    xs = [pulp.LpVariable('x{}'.format(i), cat=pulp.LpBinary) for i in range(n)]

    prob += pulp.lpSum(C[i]*xs[i] for i in range(n))
    for j in range(len(A)):
        prob += pulp.lpSum(A[j][i]*xs[i] for i in range(n)) <= B[j]
    for j in range(len(E)):
        prob += pulp.lpSum(E[j][i]*xs[i] for i in range(n)) == F[j]
    
    prob.solve()
    status = pulp.LpStatus[prob.status]
    objective = pulp.value(prob.objective)
    kai = [f'{v.name} = {v.varValue}' for v in prob.variables()]
    return status, objective, kai

def calc_min_con(C, A, B, E, F):
    prob = pulp.LpProblem(sense=pulp.LpMinimize)
    n=len(C)
    xs = [pulp.LpVariable('x{}'.format(i), cat=pulp.LpContinuous) for i in range(n)]

    prob += pulp.lpSum(C[i]*xs[i] for i in range(n))
    for j in range(len(A)):
        prob += pulp.lpSum(A[j][i]*xs[i] for i in range(n)) <= B[j]
    for j in range(len(E)):
        prob += pulp.lpSum(E[j][i]*xs[i] for i in range(n)) == F[j]
    
    prob.solve()
    status = pulp.LpStatus[prob.status]
    objective = pulp.value(prob.objective)
    kai = [f'{v.name} = {v.varValue}' for v in prob.variables()]
    return status, objective, kai

def calc_min_int(C, A, B, E, F):
    prob = pulp.LpProblem(sense=pulp.LpMinimize)
    n=len(C)
    xs = [pulp.LpVariable('x{}'.format(i), cat=pulp.LpInteger) for i in range(n)]

    prob += pulp.lpSum(C[i]*xs[i] for i in range(n))
    for j in range(len(A)):
        prob += pulp.lpSum(A[j][i]*xs[i] for i in range(n)) <= B[j]
    for j in range(len(E)):
        prob += pulp.lpSum(E[j][i]*xs[i] for i in range(n)) == F[j]
    
    prob.solve()
    status = pulp.LpStatus[prob.status]
    objective = pulp.value(prob.objective)
    kai = [f'{v.name} = {v.varValue}' for v in prob.variables()]
    return status, objective, kai

def calc_max_bin(C, A, B, E, F):
    prob = pulp.LpProblem(sense=pulp.LpMaximize)
    n=len(C)
    xs = [pulp.LpVariable('x{}'.format(i), cat=pulp.LpBinary) for i in range(n)]

    prob += pulp.lpSum(C[i]*xs[i] for i in range(n))
    for j in range(len(A)):
        prob += pulp.lpSum(A[j][i]*xs[i] for i in range(n)) <= B[j]
    for j in range(len(E)):
        prob += pulp.lpSum(E[j][i]*xs[i] for i in range(n)) == F[j]
    
    prob.solve()
    status = pulp.LpStatus[prob.status]
    objective = pulp.value(prob.objective)
    kai = [f'{v.name} = {v.varValue}' for v in prob.variables()]
    return status, objective, kai

def calc_max_con(C, A, B, E, F):
    prob = pulp.LpProblem(sense=pulp.LpMaximize)
    n=len(C)
    xs = [pulp.LpVariable('x{}'.format(i), cat=pulp.LpContinuous) for i in range(n)]

    prob += pulp.lpSum(C[i]*xs[i] for i in range(n))
    for j in range(len(A)):
        prob += pulp.lpSum(A[j][i]*xs[i] for i in range(n)) <= B[j]
    for j in range(len(E)):
        prob += pulp.lpSum(E[j][i]*xs[i] for i in range(n)) == F[j]
    
    prob.solve()
    status = pulp.LpStatus[prob.status]
    objective = pulp.value(prob.objective)
    kai = [f'{v.name} = {v.varValue}' for v in prob.variables()]
    return status, objective, kai

def calc_max_int(C, A, B, E, F):
    prob = pulp.LpProblem(sense=pulp.LpMaximize)
    n=len(C)
    xs = [pulp.LpVariable('x{}'.format(i), cat=pulp.LpInteger) for i in range(n)]

    prob += pulp.lpSum(C[i]*xs[i] for i in range(n))
    for j in range(len(A)):
        prob += pulp.lpSum(A[j][i]*xs[i] for i in range(n)) <= B[j]
    for j in range(len(E)):
        prob += pulp.lpSum(E[j][i]*xs[i] for i in range(n)) == F[j]
    
    prob.solve()
    status = pulp.LpStatus[prob.status]
    objective = pulp.value(prob.objective)
    kai = [f'{v.name} = {v.varValue}' for v in prob.variables()]
    return status, objective, kai



