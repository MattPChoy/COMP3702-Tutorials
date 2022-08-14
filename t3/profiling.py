def main(arglist):
    n_trials = 100
    print('== Exercise 3.1 ==============================================================================')
    gridworld = GridWorldEnv()

    print('BFS:')
    t0 = time.time()
    for i in range(n_trials):
        actions_bfs = bfs(gridworld, verbose=(i == 0))
    t_bfs = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_bfs)},\t\tActions: {actions_bfs}')
    print(f'Time: {t_bfs}')
    print('\n')

    print('IDDFS:')
    t0 = time.time()
    for i in range(n_trials):
        actions_iddfs = iddfs(gridworld, verbose=(i == 0))
    t_iddfs = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_iddfs)},\t\tActions: {actions_iddfs}')
    print(f'Time: {t_iddfs}')
    print('\n')

    print('== Exercise 3.2 ==============================================================================')
    print('UCS:')
    t0 = time.time()
    for i in range(n_trials):
        actions_ucs = ucs(gridworld, verbose=(i == 0))
    t_ucs = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_ucs)},\t\tActions: {actions_ucs}')
    print(f'Time: {t_ucs}')
    print('\n')

    print('A*:')
    t0 = time.time()
    for i in range(n_trials):
        actions_a_star = a_star(gridworld, manhattan_dist_heuristic, verbose=(i == 0))
    t_a_star = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_a_star)},\t\tActions: {actions_a_star}')
    print(f'Time: {t_a_star}')
    print('\n')

    print('== Exercise 3.3 ==============================================================================')
    puzzle = EightPuzzleEnv('281463_75', '1238_4765')

    print('BFS:')
    t0 = time.time()
    for i in range(n_trials):
        actions_bfs = bfs(puzzle, verbose=(i == 0))
    t_bfs = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_bfs)},\t\tActions: {actions_bfs}')
    print(f'Time: {t_bfs}')
    print('\n')

    print('A* (num mismatches):')
    t0 = time.time()
    for i in range(n_trials):
        actions_a_star = a_star(puzzle, num_mismatches_heuristic, verbose=(i == 0))
    t_a_star = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_a_star)},\t\tActions: {actions_a_star}')
    print(f'Time: {t_a_star}')
    print('\n')

    print('A* (summed manhattan):')
    t0 = time.time()
    for i in range(n_trials):
        actions_a_star = a_star(puzzle, summed_manhattan_heuristic, verbose=(i == 0))
    t_a_star = (time.time() - t0) / n_trials
    print(f'Num Actions: {len(actions_a_star)},\t\tActions: {actions_a_star}')
    print(f'Time: {t_a_star}')
    print('\n')

if __name__ == '__main__':
    main(sys.argv[1:])