import multiprocessing

def get_result(num):
    process_name = multiprocessing.current_process().name
    print("Process name: ", process_name, " Input number: ", num)
    return 10 * num

if __name__ == '__main__':
    numbers = [2, 4, 6, 8]
    pool = multiprocessing.Pool(2)
    result_list = pool.map(func = get_result, iterable = numbers)
    pool.close()
    pool.join()
    print("Final results: ", result_list)