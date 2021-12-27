import numpy as np
from scipy.integrate import solve_ivp

__all__ = [
    'solve_diffeq'
]

def solve_diffeq(func, t, tspan, ic, parameters={}, algorithm='DOP853', stepsize=np.inf):
  return solve_ivp(fun=func, t_span=tspan, t_eval=t, y0=ic, method=algorithm, 
                 args=tuple(parameters.values()), atol=1e-8, rtol=1e-5, max_step=stepsize)
