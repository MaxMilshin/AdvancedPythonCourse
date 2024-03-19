import time
import threading
import multiprocessing
import codecs
import logging

logging.basicConfig(level=logging.INFO, filename='third_task.log', filemode='w', format="%(asctime)s %(message)s")

def get_log_prefix(process_name, string_data, index):
    return f'{process_name:>5} PROCESS: string \'{string_data}\' (id: {index})'

def handler_for_A(task_queue, out_conn_to_B):
    index = 0
    while True:
        s = task_queue.get()
        prefix = get_log_prefix('A', s, index)
        logging.info(f'{prefix} was extracted from the queue')
        result = s.lower()
        out_conn_to_B.send(result)
        prefix = get_log_prefix('A', result, index)
        logging.info(f'{prefix} was send to process B')
        time.sleep(5)
        index += 1


def handler_for_B(in_conn_to_A, out_conn_to_master):
    index = 0
    while True:
        s = in_conn_to_A.recv()
        prefix = get_log_prefix('B', s, index)
        logging.info(f'{prefix} was received from process A')
        result = codecs.encode(s, "rot-13")
        prefix = get_log_prefix('B', result, index)
        out_conn_to_master.send(result)
        logging.info(f'{prefix} was send to main process')
        index += 1
    

def master_stdin_listener(task_queue):
    index = 0
    while True:
        s = input()
        task_queue.put(s, block=True)
        prefix = get_log_prefix('MAIN', s, index)
        logging.info(f'{prefix} was read from stdin and put in the queue')
        index += 1

def master_B_listener(in_conn_to_B):
    index = 0
    while True:
        s = in_conn_to_B.recv()
        print(s)
        prefix = get_log_prefix('MAIN', s, index)
        logging.info(f'{prefix} was received from process B and printed in the stdout')
        index += 1
        

def main():
    out_conn_to_B, in_conn_to_A = multiprocessing.Pipe()
    out_conn_to_master, in_conn_to_B = multiprocessing.Pipe()

    task_queue = multiprocessing.Queue()

    input_thread = threading.Thread(target=master_stdin_listener, args=(task_queue, ))
    output_thread = threading.Thread(target=master_B_listener, args=(in_conn_to_B, ))

    A = multiprocessing.Process(target=handler_for_A, args=(task_queue, out_conn_to_B, ))
    B = multiprocessing.Process(target=handler_for_B, args=(in_conn_to_A, out_conn_to_master, ))
    
    input_thread.start()
    output_thread.start()
    A.start()
    B.start()

    input_thread.join()
    output_thread.join()

if __name__ == "__main__":
    main()