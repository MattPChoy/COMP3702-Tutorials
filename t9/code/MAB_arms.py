"""
Created on Tue Dec 12 12:55:49 2017

@author: archie
"""

# Random test arms for MABs 

import numpy.random as r


class UniformArm():
  def __init__(self, lower=None, upper=None):
      if lower is None:
          lower = 0.0
      if upper is None:
          upper = 1.0
      self.lower = lower
      self.upper = upper

  def draw(self):
      return (self.upper - self.lower) * r.random() + self.lower
    

class BernoulliArm():
  def __init__(self, p):
    self.p = p

  def draw(self):
    return 1.0 if r.random() <= self.p else 0.0
    
    
class NormalArm():
  def __init__(self, mu, sigma):
    self.mu = mu
    self.sigma = sigma

  def draw(self):
    return r.normal(self.mu, self.sigma)


class WeibullArm():
  def __init__(self, shape, scale):
    self.shape = shape
    self.scale = scale
    
  def draw(self):
    return self.scale * r.weibull(self.shape)