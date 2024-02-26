import sys
import os

def wc(files):
    total_lines = 0
    total_words = 0
    total_symbols = 0
    if not files:
        lines = sys.stdin.readlines()
        words = ' '.join(lines).split()
        symbols = sum(len(line) for line in lines)
        total_lines += len(lines)
        total_words += len(words)
        total_symbols += symbols

        print(f"{total_lines:>7} {total_words:>7} {total_symbols:>7}")
    else:
        for file in files:
            with open(file, 'r') as f:
                lines = f.readlines()
                symbol_count = sum(len(line) + 1 for line in lines)
                words = ' '.join(lines).split()
                total_lines += len(lines)
                total_words += len(words)
                total_symbols += symbol_count

                print(f"{len(lines):>4} {len(words):>4} {symbol_count:>4} {file}")
                
        if len(files) > 1:
            print(f"{total_lines:>4} {total_words:>4} {total_symbols:>4} total")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        wc([])
