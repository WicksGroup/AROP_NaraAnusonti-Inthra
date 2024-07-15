from scipy.optimize import least_squares
c = 20
def function(x,cin):
    return cin-x**2

x0=5
result = least_squares(function,x0,c)
print('result=',result.x)