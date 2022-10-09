"""
Created on Tue Dec 12 12:10:21 2017

@author: archie
"""

# Instance class for MAB policy simulation, multiple trial runs, and evaluation

import numpy as np

class Instance():
  def __init__(self, arms, policy):
    self.arms = arms
    self.policy = policy

  def sim_policy(self, num_pulls):
    """Simulate num_pulls of given policy."""
    self.policy.initialize(len(self.arms))
    chosen_arms = []
    rewards = []
    for pull in range(num_pulls):
      arm = self.policy.select_arm()
      reward = self.arms[arm].draw()
      self.policy.update(arm, reward)
      chosen_arms.append(arm)
      rewards.append(reward)
      sim_result = np.array([chosen_arms,rewards])
    return sim_result
      