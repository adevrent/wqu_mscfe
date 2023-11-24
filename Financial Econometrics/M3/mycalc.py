def rho(E_X, E_Y, E_XY, E_X2, E_Y2):
    varX = E_X2 - E_X**2
    varY = E_Y2 - E_Y**2
    covXY = E_XY - E_X * E_Y
    rho = covXY / (varX * varY)**0.5
    return rho

print(rho(0.9, 0.75, 0.45, 1.3, 1.05))