from PMOEAD import PMOEAD
from PF import get_pf
from store_result import store_result
from controller import parallel_run
import time


def main():
    _parallel = True if (input('Parallel?(y/n):') == 'y') else False
    _print = True if (input('Print result?(y/n):') == 'y') else False
    begin_time = time.time()
    file_name = 'clean1.txt'
    directory = './src/datasets/' + file_name
    feature_num = 166
    population_size = max(100, min(200, feature_num))
    iteration_num = 100
    if not _parallel:
        population, obj = PMOEAD(directory, feature_num, population_size, iteration_num, 0, population_size)
    else:
        population, obj = parallel_run(10, 10, 8, directory, 166, population_size)
    store_result(obj, file_name, population_size, iteration_num, _parallel)
    if _print:
        get_pf(obj, directory, population_size, iteration_num)
    print(time.time() - begin_time)


if __name__ == '__main__':
    main()
