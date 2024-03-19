import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sync(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time

def fibonacci_threading(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    return end_time - start_time

def fibonacci_multiprocessing(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end_time = time.time()
    return end_time - start_time

def main():
    n = 33
    with open("../artifacts/4.1/fibonacci_results.txt", "w") as file:
        file.write(f"Measurements for n={n}:\n")
        file.write("Synchronous Execution: {}\n".format(fibonacci_sync(n)))
        file.write("Threading Execution: {}\n".format(fibonacci_threading(n)))
        file.write("Multiprocessing Execution: {}\n".format(fibonacci_multiprocessing(n)))

if __name__ == "__main__":
    main()