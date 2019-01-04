def store_result(obj, file_name, population_size, iteration_num, parallel):
    para = 'np'
    if parallel:
        para = 'p'
    title = './src/output/{}-popu{}-iter{}-{}'.format(para, population_size, iteration_num, file_name)
    result = open(title, 'w')
    for i in range(len(obj)):
        result.write(str(obj[i][0]))
        result.write(' ')
        result.write(str(obj[i][1]))
        result.write('\n')
    result.close()
