import sys

def nl(file=None):
    lines = None
    crop = 1
    if file:
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()
        crop = 2
    for i, line in enumerate(lines, start=1):
        print(f"{i:>6}\t{line[:-crop]}\r\n", end='')
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl()
