class GridWorld():
    ACTIONS = ['U', 'D', 'L', 'R']
    
    def __init__(self):
        self.obstacles = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.costs = [[1, 1,  1,  5,  5,  5,  5, 1, 1],
                      [1, 1,  1,  5,  5,  5,  5, 1, 1],
                      [1, 1, 10, 10, 10, 10, 10, 1, 1],
                      [1, 1,  1, 10, 10, 10, 10, 1, 1],
                      [1, 1,  1,  1,  1, 10, 10, 1, 1],
                      [1, 1,  1,  1,  1, 10, 10, 1, 1],
                      [1, 1,  1,  1, 10, 10, 10, 1, 1],
                      [1, 1,  1, 10, 10, 10, 10, 1, 1],
                      [1, 1,  1,  1,  1,  1,  1, 1, 1]]
    def step(self, state, action):
        """
        :param state: (row, column) tuple representing the current position of the agent
        :param action: One of 'U', 'D', 'L' or 'R'
        :return: Success (True or False), new state, action cost
        """
        pass # delete this when you start implementing your solution!
        
    def is_goal(self, state):
        """
        :param state: (row, col) tuple
        :return: True or False value, indicating whether the current state is the goal state
        """
        pass # delete this when you start implementing your solution!
       
    def get_state_cost(self, state):