from pNLsys.core.solver import solve_diffeq

import numpy as np
import matplotlib.pyplot as plt
from typing import List

__all__ = [
  "phasePlane", "DEplot"
]


def phasePlane(x1, x2, func, params): 
  X1, X2 = np.meshgrid(x1, x2)  # create grid
  u, v = np.zeros(X1.shape), np.zeros(X2.shape)
  NI, NJ = X1.shape
  for i in range(NI):
    for j in range(NJ):
      x = X1[i, j]
      y = X2[i, j]
      dx = func(0, (x, y), *params.values())  # compute values on grid
      u[i, j] = dx[0]
      v[i, j] = dx[1]
  M = np.hypot(u, v)
  u /= M
  v /= M
  return X1, X2, u, v, M


def DEplot(sys: object, tspan: tuple, x0: List[List[float]],
           x: np.ndarray, y: np.ndarray, params: dict):
  if len(tspan) != 3:
    raise Exception(
        'tspan should be tuple of size 3: (min, max, number of points).')
  # Set up the figure the way we want it to look
  plt.figure(figsize=(12, 9))

  X1, X2, dx1, dx2, M = phasePlane(
      x, y, sys, params
  )

  # Quiver plot
  plt.quiver(X1, X2, dx1, dx2, M, scale=None, pivot='mid')
  plt.grid()

  if tspan[0] < 0:
    t1 = np.linspace(0, tspan[0], tspan[2])
    t2 = np.linspace(0, tspan[1], tspan[2])
    if min(tspan) < 0:
      t_span1 = (np.max(t1), np.min(t1))
    else:
      t_span1 = (np.min(t1), np.max(t1))
    t_span2 = (np.min(t2), np.max(t2))
    for x0i in x0:
      sol1 = solve_diffeq(sys, t1, t_span1, x0i, params)
      plt.plot(sol1.y[0, :], sol1.y[1, :], '-r')
      sol2 = solve_diffeq(sys, t2, t_span2, x0i, params)
      plt.plot(sol2.y[0, :], sol2.y[1, :], '-r')
  else:
    t = np.linspace(tspan[0], tspan[1], tspan[2])
    t_span = (np.min(t), np.max(t))
    for x0i in x0:
      sol = solve_diffeq(sys, t, t_span, x0i, params)
      plt.plot(sol.y[0, :], sol.y[1, :], '-r')

  plt.xlim([np.min(x), np.max(x)])
  plt.ylim([np.min(y), np.max(y)])
  plt.show()
