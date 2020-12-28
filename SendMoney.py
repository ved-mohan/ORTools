from ortools.sat.python import cp_model


def SimpleSatProgram():
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    s = model.NewIntVar(0, 9, 's')
    e = model.NewIntVar(0, 9, 'e')
    n = model.NewIntVar(0, 9, 'n')
    d = model.NewIntVar(0, 9, 'd')
    m = model.NewIntVar(0, 9, 'm')
    o = model.NewIntVar(0, 9, 'o')
    r = model.NewIntVar(0, 9, 'r')
    n = model.NewIntVar(0, 9, 'n')
    y = model.NewIntVar(0, 9, 'y')
    r1 = model.NewIntVar(0, 9, 'r1')
    r2 = model.NewIntVar(0, 9, 'r2')
    r3 = model.NewIntVar(0, 9, 'r3')
    r4 = model.NewIntVar(0, 9, 'r4')

    # Creates the constraints.
    model.Add(d + e == y + 10*r1)
    model.Add(n + r  + r1 == e + 10*r2)
    model.Add(e + o  + r2 == n + 10*r3)
    model.Add(s + m  + r3 == o + 10*r4)
    model.Add(r4 == m)

    model.Add(s != 0)
    model.Add(m != 0)


    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        print('s = %i' % solver.Value(s))
        print('e = %i' % solver.Value(e))
        print('n = %i' % solver.Value(n))
        print('d = %i' % solver.Value(d))
        print('m = %i' % solver.Value(m))
        print('o = %i' % solver.Value(o))
        print('r = %i' % solver.Value(r))
        print('n = %i' % solver.Value(n))
        print('y = %i' % solver.Value(y))
        print('r1 = %i' % solver.Value(r1))
        print('r2 = %i' % solver.Value(r2))
        print('r3 = %i' % solver.Value(r3))
        print('r4 = %i' % solver.Value(r4))
   
SimpleSatProgram()
