import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging

artifacts_subdirectory = '../artifacts/4.2/'

logging.basicConfig(level=logging.INFO, filename=artifacts_subdirectory+'second_task.log', filemode='w', format="%(message)s")

N_ITERS = 100000

def subintegrate(f, a, b, n_iter, task_id):
    acc = 0
    step = (b - a) / n_iter
    cnt = n_iter // 10
    for i in range(n_iter):
        if i % cnt == 0:
            logging.info(f"Task {task_id} pass through {i} iterations")
        acc += f(a + i * step) * step
    return acc



def integrate_with_multuple_threads(f, a, b, *, n_jobs=1, n_iter=N_ITERS):
    acc = 0
    big_step = (b - a) / n_jobs
    small_n_iter = n_iter // n_jobs
    with ThreadPoolExecutor(max_workers=16) as executor:
        all_futures = []
        for i in range(n_jobs):
            aa = big_step * i
            bb = aa + big_step
            # print(aa, bb)
            future = executor.submit(subintegrate, f, aa, bb, small_n_iter, i)
            all_futures.append(future)
        for future in all_futures:
            acc += future.result()
    return acc


def integrate_with_multuple_processes(f, a, b, *, n_jobs=1, n_iter=N_ITERS):
    acc = 0
    big_step = (b - a) / n_jobs
    small_n_iter = n_iter // n_jobs
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        all_futures = []
        for i in range(n_jobs):
            aa = big_step * i
            bb = aa + big_step
            # print(aa, bb)
            future = executor.submit(subintegrate, f, aa, bb, small_n_iter, i)
            all_futures.append(future)
        
        for future in all_futures:
            acc += future.result()
    return acc


def main():
    integrate_methods = [integrate_with_multuple_threads, integrate_with_multuple_processes]
    measurements_filename = artifacts_subdirectory + "measurements.txt"
    for n_jobs in range(1, 17):
        logging.info(f"\n\nStart of execution for {n_jobs} jobs")
        with open(measurements_filename, "a") as file:
            file.write(f'\n\nTime measurements for {n_jobs} N_JOBS:\n')
        for method_to_integrate in integrate_methods:
            start_time = time.time()
            res = method_to_integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
            # print(res)
            end_time = time.time()
            measured_time = end_time - start_time
            with open(measurements_filename, "a") as file:
                file.write(f'For method {method_to_integrate.__name__}: {measured_time}s\n')
            
if __name__ == "__main__":
    main()