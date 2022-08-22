class CrossWord:
  def __init__(self):
    self.constraint_checks = 0
    self.words = { # Set of possible variable allocations
        "AFT", "ALE", "EEL", "HEEL", "HIKE", "HOSES", "KEEL", "KNOT", "LASER", "LEE",
	 "LINE", "SAILS", "SHEET", "STEER", "TIE"
    }
   
    self.vars = { # Variables and their current assignments;
                  # a map of variable names -> variable assignments
                  # (assignment from self.words)
        "1A": "", "2D": "", "3D": "", "4A": "",
        "5D": "", "6D": "", "7A": "", "8A": ""
    }

    self.length_constraints = {
        "1A": 5, "2D": 5, "3D": 5, "4A": 4,
        "5D": 4, "6D": 3, "7A": 3, "8A": 5
    }
    self.intersect_constraints = {
        "1A": [("1A", 2, "2D", 0), ("1A", 4, "3D", 0)],
        "2D": [("2D", 0, "1A", 2), ("2D", 2, "4A", 1),
               ("2D", 3, "7A", 0), ("2D", 4, "8A", 2)],
        "3D": [("3D", 0, "1A", 4), ("3D", 2, "4A", 3),
               ("3D", 3, "7A", 2), ("3D", 4, "8A", 4)],
        "4A": [("4A", 1, "2D", 2), ("4A", 2, "5D", 0), ("4A", 3, "3D", 2)],
        "5D": [("5D", 0, "4A", 2), ("5D", 1, "7A", 1), ("5D", 2, "8A", 3)],
        "6D": [("6D", 1, "8A", 0)],
        "7A": [("7A", 0, "2D", 3), ("7A", 1, "5D", 1), ("7A", 2, "3D", 3)],
        "8A": [("8A", 0, "6D", 1), ("8A", 2, "2D", 4),
               ("8A", 3, "5D", 2), ("8A", 4, "3D", 4)]
    }
   
    self.domains = {
        k: [word for word in self.words if len(word) == self.length_constraints[k]]
        for k, v in self.vars.items()
    }

    def recursive_backtracking(env, assignment, expanded=0, verbose=False):
    unassigned = None # Locate an empty assignment
    for key, val in assignment.items():
        if val == "": # The variable hasn't been assigned;
            unassigned = key
            break
    if unassigned is None: # All variables have been assigned
        return assignment, expanded   
    for word in env.domains[unassigned]:
        # Select a potential assignment
        assignment[unassigned] = word
        # Check assignments validity
        if not env.check_constraints(assignment):
                        # Find another assignment;
            continue       
        # lock in current value and expand other nodes
        result, expanded = recursive_backtracking(env, {k: v for k, v in assignment.items()}, expanded + 1)
        if result is not None:
            if verbose:
                print("Number of backtracks", expanded)
            return result, expanded
    return None, expanded

    def arc_consistency(env, verbose=False):
    constraint_checks = 0
    domains = {
        k: [word for word in env.words if len(word) == env.length_constraints[k]]
        for k, v in env.vars.items()
    }   
    container = [x for k, v in env.intersect_constraints.items() for x in v]
    while container != []:
        constraint_checks += 1
        n1, i1, n2, i2  = container.pop(0)         # Revise the CSP
        prior_len = len(domains[n1])
        avail_letters1 = set(word[i1] for word in domains[n1])
        avail_letters2 = set(word[i2] for word in domains[n2])
        result = avail_letters1.intersection(avail_letters2)
        # Update the domain based on the revision
        domains[n1] = [word for word in domains[n1] if word[i1] in result]
        if domains[n1] == []:  # No solution exists
            return None
        elif len(domains[n1]) != prior_len:
            # If domain changes, reconsider constraints for neighbouring nodes
            for n, i, m, j in env.intersect_constraints[n1]:
                if m != n2:
                    # We shedule neighbour m to be updated with
                    # the new domain of n (our current node)
                    container.append((m, j, n, i))  
   
    if verbose:
        print(f"Number of arc constraint checks: {constraint_checks}")  
       
    return domains

env = CrossWord()

recursive_backtracking(env, {k: v for k, v in env.vars.items()}, verbose=True)
arc_consistency(env, verbose=True)

print("Number of backtracking constraint checks", env.constraint_checks)


import time
samples = 1000
env = CrossWord()
start = time.time()
for i in range(samples):
    recursive_backtracking(env, {k: v for k, v in env.vars.items()})
print("backtracking", (time.time() - start) / samples)
start = time.time()
for i in range(samples):
    arc_consistency(env)
print("arc", (time.time() - start) / samples)
