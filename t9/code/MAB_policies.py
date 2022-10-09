"""
Created on Tue Oct  24 15:33:07 2017

@author: archie
Fixed some bugs, Alex 2020.
"""

# Policies for MAB sampling
import numpy as np
import numpy.random as r


class BasePolicy:
    """
    Abstract policy class.
    Descendant classes instantiated with method 'select_arm()'.
    """

    def __init__(self, plays, means):
        self.plays = plays
        self.means = means

    def initialize(self, n_arms):
        self.plays = [0 for _ in range(n_arms)]
        self.means = [0.0 for _ in range(n_arms)]

    @staticmethod
    def ind_max(values):
        return values.index(max(values))

    def update(self, chosen_arm, reward):
        self.plays[chosen_arm] += 1
        arm_plays = self.plays[chosen_arm]
        arm_payoff = self.means[chosen_arm]
        self.means[chosen_arm] = (arm_payoff * (arm_plays - 1) + reward) / float(arm_plays)


class Uniform(BasePolicy):
    """
    Pulls a random arm with uniform probability.
    """

    def __init__(self, plays=None, means=None):
        if means is None:
            means = []
        if plays is None:
            plays = []
        self.name = 'Uniform'
        BasePolicy.__init__(self, plays, means)

    def select_arm(self):
        return r.randint(len(self.means))


class EpsilonGreedy(BasePolicy):
    """
    Exploits the best arm with probability 1-epsilon.
    Explores a random arm with probability epsilon.
    """

    def __init__(self, epsilon, plays=None, means=None):
        if means is None:
            means = []
        if plays is None:
            plays = []
        self.epsilon = epsilon
        self.name = 'EpsilonGreedy: %s' % epsilon
        BasePolicy.__init__(self, plays, means)

    def select_arm(self):
        if r.random() <= self.epsilon:
            # exploration
            return r.randint(len(self.means))
        else:
            # exploitation of best arm so far
            return self.ind_max(self.means)


class AnnealingEpsilonGreedy(BasePolicy):
    """Epsilon Greedy policy where epsilon approaches 0.0 over time."""

    def __init__(self, plays=None, means=None):
        if plays is None:
            plays = []
        if means is None:
            means = []
        self.name = 'AnnealingEpsilonGreedy'
        BasePolicy.__init__(self, plays, means)

    def select_arm(self):
        # start at 1, then decrease to 0 as #plays increases
        epsilon = min(1, 1 / np.log(sum(self.plays) + 0.0000001))
        if r.random() <= epsilon:
            return r.randint(len(self.means))
        else:
            return self.ind_max(self.means)


class Boltzmann(BasePolicy):
    """Selects arm based on observed payoff rates."""

    def __init__(self, temperature, plays=None, means=None):
        if means is None:
            means = []
        if plays is None:
            plays = []
        self.temperature = temperature
        self.name = 'Boltzmann: %s' % temperature
        BasePolicy.__init__(self, plays, means)

    def select_arm(self):
        denominator = sum([np.exp(v / self.temperature) for v in self.means])
        probs = [np.exp(v / self.temperature) / denominator for v in self.means]
        z = r.random()
        cum_prob = 0.0
        for i, prob in enumerate(probs):
            cum_prob += prob
            if cum_prob > z:
                return i
        return len(probs) - 1


class AnnealingBoltzmann(BasePolicy):
    """Boltzmann policy with temperature annealing to 0.0 logarithmically over time."""

    def __init__(self, plays=None, means=None):
        if means is None:
            means = []
        if plays is None:
            plays = []
        self.name = 'AnnealingBoltzmann'
        BasePolicy.__init__(self, plays, means)

    def select_arm(self):
        temperature = 1 / np.log(sum(self.plays) + 1.0000001)
        denominator = sum([np.exp(v / temperature) for v in self.means])
        probs = [np.exp(v / temperature) / denominator for v in self.means]
        z = r.random()
        cum_prob = 0.0
        for i, prob in enumerate(probs):
            cum_prob += prob
            if cum_prob > z:
                return i
        return len(probs) - 1


class UCB1(BasePolicy):
    """Selects arm according to upper confidence bound on mean rewards"""

    def __init__(self, plays=None, means=None, k=1, c=2):
        if means is None:
            means = []
        if plays is None:
            plays = []
        self.name = 'UCB1'
        BasePolicy.__init__(self, plays, means)
        self.k = k
        self.C = c

    def select_arm(self):
        n_arms = len(self.plays)
        for arm in range(n_arms):
            if self.plays[arm] == 1:
                return arm
        uc_bounds = [0.0 for _ in range(n_arms)]
        total_counts = sum(self.plays)
        for arm in range(n_arms):
            if self.plays[arm] > self.k:
                interval = np.sqrt((self.C * np.log(total_counts)) / float(self.plays[arm]))
                uc_bounds[arm] = self.means[arm] + interval
            else:
                return arm
        return self.ind_max(uc_bounds)
