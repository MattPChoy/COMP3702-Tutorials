# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:55:19 2018

@author: archie
"""

## mab_runTestInstance.py
import MAB_arms as ar
from MAB_instance import Instance
import MAB_policies as po

""" 
MAB arm cases
"""
### Uniform arms ###
#arms = [ar.UniformArm(lower,upper) 
#        for lower, upper in zip([0.1, 0.2, 0.5], [2.0, 0.5, 1.0])]
#print "Arms: (lower, upper)"
#for i in range(len(arms)):
#  print i, arms[i].lower, arms[i].upper
          
          
### Bernoulli arms ###
#arms = [ar.BernoulliArm(p) for p in [0.1, 0.7, 1.0]]
#print "Arms: (p)"
#for i in range(len(arms)):
#  print i, arms[i].p


### Normal arms ###
#arms = [ar.NormalArm(mu,sigma) 
#        for mu, sigma in zip([0.1, 0.7, 1.0], [2.0, 0.5, 0.1])]
#print "Arms: (mu, sigma)"
#for i in range(len(arms)):
#  print i, arms[i].mu, arms[i].sigma


### Weibull arms ###
#arms = [ar.WeibullArm(shape,scale) for shape, scale in zip([1.0, 1.7, 2.0], [2.0, 2.0, 2.0])]
#print "Arms: (shape, scale)"
#for i in range(len(arms)):
#  print i, arms[i].shape, arms[i].scale

### All arm types ###
arms = []
arms.append(ar.UniformArm(0.1,2.0))
arms.append(ar.BernoulliArm(0.7))
arms.append(ar.NormalArm(0.7,0.5))
arms.append(ar.WeibullArm(1.7,2.0))

  
""" 
MAB policy cases
"""
policy_list = ['Uniform','eps-greedy','Ann-eps-greedy','Boltzmann','ann-Boltzmann','UCB1']
policies = []
policies.append(po.Uniform())
policies.append(po.EpsilonGreedy(0.2))
policies.append(po.AnnealingEpsilonGreedy())
policies.append(po.Boltzmann(1.0))
policies.append(po.AnnealingBoltzmann(0.2))
policies.append(po.UCB1())


"""
Evaluate each policy in one simulation
"""
for p in range(len(policies)):
    mab = Instance(arms, policies[p])
    num_pulls = 5
    sim_result = mab.sim_policy(num_pulls) 
    print("Simulation result for", policy_list[p])
    print(sim_result)
    print()
    
"""
Plot results
"""
# TODO
# import matplotlib.pyplot as plt
