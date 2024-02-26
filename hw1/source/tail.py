import sys

def tail(files):
    if not files:
        lines = sys.stdin.readlines()
        print(''.join(lines[-17:]), end='')
    else:
        for i, file in enumerate(files):
            print(f"==> {file} <==")
            with open(file, 'r') as f:
                lines = list(map(lambda x : x[:-1] + '\r\n', f.readlines()))
                print(''.join(lines[-10:]), end='')
            if i != len(files) - 1:
                print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tail(sys.argv[1:])
    else:
        tail([])
