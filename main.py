from PMOEAD import PMOEAD
from PF import get_pf
from store_result import store_result
from controller import *
import time


def main():
    _parallel = True if (input('Parallel?(y/n):') == 'y') else False
    _bytime = True if (input('By time?(y/n):') == 'y') else False
    _print = True if (input('Print result?(y/n):') == 'y') else False
    begin_time = time.time()
    file_name = 'clean1.txt'
    directory = './src/datasets/' + file_name
    feature_num = 166
    population_size = max(100, min(200, feature_num))
    iteration_num = 20
    round_num = 10
    run_time = 3600
    if not _parallel:
        if _bytime:
            population, obj = PMOEAD_bytime(file_name=file_name, dimension=feature_num, population_size=population_size, max_time=run_time, begin=begin, end=end)
        else:
            population, obj = PMOEAD(directory, feature_num, population_size, iteration_num, 0, population_size)
    else:
        if _bytime:
            population, obj = parallel_run_bytime(max_time=run_time, iteration_num=10, cpu_num=12, file_name=directory, dimension=166, population_size=population_size)
        else:
            population, obj = parallel_run(round_num, iteration_num, 12, directory, 166, population_size)
    store_result(obj, file_name, population_size, iteration_num * round_num, _parallel, _bytime)
    if _print:
        get_pf(obj, directory, population_size, iteration_num)
    print(time.time() - begin_time)


if __name__ == '__main__':
    main()
